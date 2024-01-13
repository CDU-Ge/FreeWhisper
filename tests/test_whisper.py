import os
import pprint
import unittest

import whisper

TEST_ROOT = os.path.abspath(os.path.dirname(__file__))
TEST_DATA = os.path.abspath(os.path.join(TEST_ROOT, "data"))
PROJECT_ROOT = os.path.abspath(os.path.join(TEST_ROOT, ".."))
MODEL_ROOT = os.path.abspath(os.path.join(PROJECT_ROOT, "models"))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        audio = whisper.load_audio(os.path.join(TEST_DATA, "test_data_mini.m4a"))
        audio = whisper.pad_or_trim(audio)
        pprint.pp(audio)
        pprint.pp(audio.shape)

        model = whisper.load_model("tiny", download_root=MODEL_ROOT)
        mel = whisper.log_mel_spectrogram(audio).to(model.device)

        _, probs = model.detect_language(mel)
        print(f"Detected language: {max(probs, key=probs.get)}")

        # decode the audio
        options = whisper.DecodingOptions()
        result = whisper.decode(model, mel, options)

        # print the recognized text
        print(result.text)

    def test_free_whisper(self):
        from FreeWhisper.utils import set_debug
        set_debug()
        from FreeWhisper.core import transcribe, StreamResult
        model = whisper.load_model("base", download_root=MODEL_ROOT)
        model.eval()
        r = transcribe(model, os.path.join(TEST_DATA, "test_data_mini.m4a"),
                       language='chinese', verbose=True, stream=StreamResult())
        print(r)


if __name__ == '__main__':
    unittest.main()
