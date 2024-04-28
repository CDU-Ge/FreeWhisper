# -*- coding: utf-8 -*-
# Copyright (c) CDU

"""Model Docstrings


Pypi: pip install faster-whisper
"""
import os

from faster_whisper import WhisperModel

os.environ['HTTP_PROXY'] = 'http://127.0.0.1:10809'
os.environ['HTTPS_PROXY'] = os.environ['HTTP_PROXY']

model_size = "large-v3"

import torch

print(torch.cuda.is_available())
# display cuda cudnn version info
print(torch.__version__)
print(torch.version.cuda)
print(torch.cuda.__file__)
print(torch.backends.cudnn.version())




# Run on GPU with FP16
model = WhisperModel(model_size, device="cuda", compute_type="float16")

# or run on GPU with INT8
# model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
# or run on CPU with INT8
# model = WhisperModel(model_size, device="cpu", compute_type="int8")

segments, info = model.transcribe("audio.aac", beam_size=5)

print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

from pathlib import Path

transcript = Path('transcript.txt')

for segment in segments:
    line: str = "[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text)
    print(line)
    with transcript.open('a') as f:
        f.write(line + '\n')
