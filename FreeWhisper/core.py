# -*- coding: utf-8 -*-
# Copyright (c) CDU

"""Model Docstrings

"""

from __future__ import absolute_import
from __future__ import annotations
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import warnings
from collections import namedtuple
from typing import List
from typing import Optional
from typing import TYPE_CHECKING
from typing import Tuple
from typing import TypedDict
from typing import Union

import torch

import whisper
from FreeWhisper.utils import logger
from whisper import DecodingResult
from whisper import utils as whisper_utils
from whisper.audio import FRAMES_PER_SECOND
from whisper.audio import HOP_LENGTH
from whisper.audio import N_FRAMES
from whisper.audio import N_SAMPLES
from whisper.audio import SAMPLE_RATE
from whisper.timing import add_word_timestamps
from whisper.tokenizer import LANGUAGES

if TYPE_CHECKING:
    import numpy as np
    from whisper import Whisper


class _StreamResult(TypedDict):
    start: str
    end: str
    text: str


_StreamResultTuple = namedtuple('StreamResultTuple', ('start', 'end', 'text'))


class StreamResult:
    def __init__(self):
        self.content: List[_StreamResult] = []

    @classmethod
    def decode(cls, segment: dict) -> _StreamResultTuple:
        return _StreamResultTuple(
            start=whisper_utils.format_timestamp(segment.get('start', 0)),
            end=whisper_utils.format_timestamp(segment.get('end', 0)),
            text=str(segment.get('text', '')),
        )

    def add(self, data: _StreamResultTuple):
        self.content.append({
            "start": data.start,
            "end": data.end,
            "text": data.text
        })
        self.callback(self.content[-1])

    def callback(self, _result: _StreamResult):
        index = len(self.content)
        start, end, text = _result['start'], _result['end'], _result['text']
        line = f"[{start} --> {end}] {text}"
        logger.info(line)
        print(line)


def transcribe(
        model: 'Whisper', audio: Union[str, 'np.ndarray', 'torch.Tensor'], *,
        verbose: Optional[bool] = None,
        temperature: Union[float, Tuple[float, ...]] = (0.0, 0.2, 0.4, 0.6, 0.8, 1.0),
        compression_ratio_threshold: Optional[float] = 2.4,
        logprob_threshold: Optional[float] = -1.0,
        no_speech_threshold: Optional[float] = 0.6,
        condition_on_previous_text: bool = True,
        initial_prompt: Optional[str] = None,
        word_timestamps: bool = False,
        prepend_punctuations: str = "\"'“¿([{-",
        append_punctuations: str = "\"'.。,，!！?？:：”)]}、",
        stream: StreamResult = None,
        **decode_options,
):
    """

    Args:
        model: The Whisper model instance
        audio: The path to the audio file to open, or the audio waveform

        verbose:
            Whether to display the text being decoded to the console. If True, displays all the details,
            If False, displays minimal details. If None, does not display anything

        temperature: Temperature for sampling. It can be a tuple of temperatures, which will be successively used
        upon failures according to either `compression_ratio_threshold` or `logprob_threshold`.

        compression_ratio_threshold:
            If the gzip compression ratio is above this value, treat as failed.
            如果gzip压缩率高于此值，则视为失败。

        logprob_threshold:
            If the average log probability over sampled tokens is below this value, treat as failed
            如果取样标记的平均对数概率低于这个值，则视为失败。

        no_speech_threshold:
            If the no_speech probability is higher than this value AND the average log probability
        over sampled tokens is below `logprob_threshold`, consider the segment as silent
            如果 no_speech 概率高于这个值，并且平均对数概率
            在取样标记中，如果低于 "logprob_threshold"，则认为该段是无声的。

        condition_on_previous_text:
            if True, the previous output of the model is provided as a prompt for the next window;
        disabling may make the text inconsistent across windows, but the model becomes less prone to
        getting stuck in a failure loop, such as repetition looping or timestamps going out of sync.
            如果为 True，则提供模型的上一个输出作为下一个窗口的提示;
            禁用可能会使文本在窗口之间不一致，但模型变得不那么容易
            陷入故障循环，例如重复循环或时间戳不同步。

        initial_prompt:
            Optional text to provide as a prompt for the first window. This can be used to provide, or
            "prompt-engineer" a context for transcription, e.g. custom vocabularies or proper nouns
            to make it more likely to predict those word correctly.
            要作为第一个窗口的提示提供的可选文本。这可用于提供，或“提示工程师”转录上下文，例如自定义词汇或专有名词使其更有可能正确预测这些单词。

        word_timestamps:
            Extract word-level timestamps using the cross-attention pattern and dynamic time warping,
            and include the timestamps for each word in each segment.
            使用交叉注意力模式和动态时间扭曲提取单词级的时间戳、并包括每个片段中每个单词的时间戳。

        prepend_punctuations:
            If word_timestamps is True, merge these punctuation symbols with the next word.
            如果 word_timestamps 为True，则将这些标点符号与下一个单词合并。

        append_punctuations:
            If word_timestamps is True, merge these punctuation symbols with the previous word
            如果word_timestamps为True，则将这些标点符号与前一个单词合并。

        stream:
            pass

        **decode_options:
            Keyword arguments to construct `DecodingOptions` instances
            构建 "DecodingOptions "实例的关键字参数，包含：
            1. fp16
            2. language

    Returns:
        A dictionary containing the resulting text ("text") and segment-level details ("segments"), and
        the spoken language ("language"), which is detected when `decode_options["language"]` is None.
    """
    dtype = torch.float16 if decode_options.get("fp16", True) else torch.float32
    if model.device == torch.device("cpu"):
        if torch.cuda.is_available():
            warnings.warn("Performing inference on CPU when CUDA is available")
        if dtype == torch.float16:
            warnings.warn("FP16 is not supported on CPU; using FP32 instead")
            dtype = torch.float32

    if dtype == torch.float32:
        decode_options["fp16"] = False

    # Pad 30-seconds of silence to the input audio, for slicing
    # 在输入音频中填充 30 秒静音，用于切片
    mel = whisper.log_mel_spectrogram(audio, padding=N_SAMPLES)

    content_frames = mel.shape[-1] - N_FRAMES
    """音频帧"""

    if decode_options.get("language", None) is None:
        if not model.is_multilingual:
            decode_options["language"] = "en"
        else:
            if verbose:
                print(
                    "Detecting language using up to the first 30 seconds. Use `--language` to specify the language",
                    "最多使用前 30 秒检测语言。使用`--language`指定语言"
                )
            mel_segment = whisper.pad_or_trim(mel, N_FRAMES).to(model.device).to(dtype)
            _, probs = model.detect_language(mel_segment)
            decode_options["language"] = max(probs, key=probs.get)
            if verbose is not None:
                print(
                    f"Detected language: {LANGUAGES[decode_options['language']].title()}"
                )
    language: str = decode_options["language"]

    task: str = decode_options.get("task", "transcribe")
    tokenizer = whisper.tokenizer.get_tokenizer(model.is_multilingual, language=language, task=task)

    if word_timestamps and task == "translate":
        warnings.warn(
            "Word-level timestamps on translations may not be reliable." +
            "\n翻译中的词级时间戳可能不可靠。"
        )

    def decode_with_fallback(segment: torch.Tensor) -> whisper.DecodingResult:
        temperatures = (
            [temperature] if isinstance(temperature, (int, float)) else temperature
        )
        decode_result = None

        for t in temperatures:
            kwargs = {**decode_options}
            if t > 0:
                # disable beam_size and patience when t > 0
                kwargs.pop("beam_size", None)
                kwargs.pop("patience", None)
            else:
                # disable best_of when t == 0
                kwargs.pop("best_of", None)

            options = whisper.DecodingOptions(**kwargs, temperature=t)
            decode_result = model.decode(segment, options)

            needs_fallback = False
            if (
                    compression_ratio_threshold is not None
                    and decode_result.compression_ratio > compression_ratio_threshold
            ):
                needs_fallback = True  # too repetitive
            if (
                    logprob_threshold is not None
                    and decode_result.avg_logprob < logprob_threshold
            ):
                needs_fallback = True  # average log probability is too low

            if not needs_fallback:
                break

        return decode_result

    seek = 0
    input_stride = whisper_utils.exact_div(
        N_FRAMES, model.dims.n_audio_ctx
    )  # mel frames per output token: 2
    time_precision = (
            input_stride * HOP_LENGTH / SAMPLE_RATE
    )  # time per output token: 0.02 (seconds)
    all_tokens = []
    all_segments = []
    prompt_reset_since = 0

    if initial_prompt is not None:
        initial_prompt_tokens = tokenizer.encode(" " + initial_prompt.strip())
        all_tokens.extend(initial_prompt_tokens)
    else:
        initial_prompt_tokens = []

    def new_segment(*, start: float, end: float, tokens: torch.Tensor, result: DecodingResult):
        tokens = tokens.tolist()
        text_tokens = [token for token in tokens if token < tokenizer.eot]
        return {
            "seek": seek,
            "start": start,
            "end": end,
            "text": tokenizer.decode(text_tokens),
            "tokens": tokens,
            "temperature": result.temperature,
            "avg_logprob": result.avg_logprob,
            "compression_ratio": result.compression_ratio,
            "no_speech_prob": result.no_speech_prob,
        }

    while seek < content_frames:
        time_offset = float(seek * HOP_LENGTH / SAMPLE_RATE)
        mel_segment = mel[:, seek: seek + N_FRAMES]
        segment_size = min(N_FRAMES, content_frames - seek)
        segment_duration = segment_size * HOP_LENGTH / SAMPLE_RATE
        mel_segment = whisper.pad_or_trim(mel_segment, N_FRAMES).to(model.device).to(dtype)

        decode_options["prompt"] = all_tokens[prompt_reset_since:]
        result: DecodingResult = decode_with_fallback(mel_segment)
        tokens = torch.tensor(result.tokens)

        if no_speech_threshold is not None:
            # no voice activity check
            should_skip = result.no_speech_prob > no_speech_threshold
            if (
                    logprob_threshold is not None
                    and result.avg_logprob > logprob_threshold
            ):
                # don't skip if the logprob is high enough, despite the no_speech_prob
                should_skip = False

            if should_skip:
                seek += segment_size  # fast-forward to the next segment boundary
                continue

        previous_seek = seek
        current_segments = []

        timestamp_tokens: torch.Tensor = tokens.ge(tokenizer.timestamp_begin)
        single_timestamp_ending = timestamp_tokens[-2:].tolist() == [False, True]

        consecutive = torch.where(timestamp_tokens[:-1] & timestamp_tokens[1:])[0]
        consecutive.add_(1)
        if len(consecutive) > 0:
            # if the output contains two consecutive timestamp tokens
            slices = consecutive.tolist()
            if single_timestamp_ending:
                slices.append(len(tokens))

            last_slice = 0
            for current_slice in slices:
                sliced_tokens = tokens[last_slice:current_slice]
                start_timestamp_pos = (
                        sliced_tokens[0].item() - tokenizer.timestamp_begin
                )
                end_timestamp_pos = (
                        sliced_tokens[-1].item() - tokenizer.timestamp_begin
                )
                current_segments.append(
                    new_segment(
                        start=time_offset + start_timestamp_pos * time_precision,
                        end=time_offset + end_timestamp_pos * time_precision,
                        tokens=sliced_tokens,
                        result=result,
                    )
                )
                last_slice = current_slice

            if single_timestamp_ending:
                # single timestamp at the end means no speech after the last timestamp.
                seek += segment_size
            else:
                # otherwise, ignore the unfinished segment and seek to the last timestamp
                last_timestamp_pos = (
                        tokens[last_slice - 1].item() - tokenizer.timestamp_begin
                )
                seek += last_timestamp_pos * input_stride
        else:
            duration = segment_duration
            timestamps = tokens[timestamp_tokens.nonzero().flatten()]
            if (
                    len(timestamps) > 0
                    and timestamps[-1].item() != tokenizer.timestamp_begin
            ):
                # no consecutive timestamps but it has a timestamp; use the last one.
                last_timestamp_pos = (
                        timestamps[-1].item() - tokenizer.timestamp_begin
                )
                duration = last_timestamp_pos * time_precision

            current_segments.append(
                new_segment(
                    start=time_offset,
                    end=time_offset + duration,
                    tokens=tokens,
                    result=result,
                )
            )
            seek += segment_size

        if not condition_on_previous_text or result.temperature > 0.5:
            # do not feed the prompt tokens if a high temperature was used
            prompt_reset_since = len(all_tokens)

        if word_timestamps:
            add_word_timestamps(
                segments=current_segments,
                model=model,
                tokenizer=tokenizer,
                mel=mel_segment,
                num_frames=segment_size,
                prepend_punctuations=prepend_punctuations,
                append_punctuations=append_punctuations,
            )
            word_end_timestamps = [
                w["end"] for s in current_segments for w in s["words"]
            ]
            if not single_timestamp_ending and len(word_end_timestamps) > 0:
                seek_shift = round(
                    (word_end_timestamps[-1] - time_offset) * FRAMES_PER_SECOND
                )
                if seek_shift > 0:
                    seek = previous_seek + seek_shift

        if verbose:
            for segment in current_segments:
                start, end, text = segment["start"], segment["end"], segment["text"]
                stream.add(stream.decode(segment))

        # if a segment is instantaneous or does not contain text, clear it
        # 如果句段是一个时刻或不包含文本，请将其清除
        for i, segment in enumerate(current_segments):
            if segment["start"] == segment["end"] or segment["text"].strip() == "":
                segment["text"], segment["tokens"], segment["words"] = "", [], []

        all_segments.extend(
            [
                {"id": i, **segment}
                for i, segment in enumerate(
                current_segments, start=len(all_segments)
            )
            ]
        )
        # update tokens
        all_tokens.extend(
            [token for segment in current_segments for token in segment["tokens"]]
        )
    return dict(
        text=tokenizer.decode(all_tokens[len(initial_prompt_tokens):]),
        segments=all_segments,
        language=language,
    )
