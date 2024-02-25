# -*- coding: utf-8 -*-
# Copyright (c) CDU

"""Model Docstrings

"""

from __future__ import absolute_import
from __future__ import annotations
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import hashlib
import json
import pathlib

from translate import Translator

from FreeWhisper.utils import Srt


class TranslateCache:
    def __init__(self, path: pathlib.Path):
        self.path = path
        self.cache = {}
        if path.exists():
            for line in path.read_text(encoding='utf-8').splitlines():
                key, value = line.split(":", 1)
                self.cache[key] = value

    def query(self, text: str):
        key = hashlib.md5(text.encode("utf-8")).hexdigest()
        if key in self.cache.keys():
            return self.cache[key].replace("\\n", "\n")
        else:
            result = translate(text)
            self.add(text, result)
            return result

    def add(self, text: str, result: str):
        key = hashlib.md5(text.encode("utf-8")).hexdigest()
        result = result.replace("\n", "\\n")
        self.cache[key] = result
        with self.path.open('a', encoding='utf-8') as f:
            f.write(f"{key}:{result}\n")


translate = Translator(to_lang='zh', from_lang='ja').translate
translate_cache = TranslateCache(pathlib.Path("translate.cache")).query
result = json.loads(pathlib.Path("../result.json").read_text(encoding="utf-8"))

srt_ja = Srt()
srt_zh = Srt()
last_time = 0
for segment in result['segments']:
    text = f"{translate_cache(segment['text'])}"
    d = segment['end'] - segment['start']
    print(text)
    if segment['start'] - last_time < 0:
        raise ValueError
    srt_ja.add(segment['start'], segment['end'], text)
    srt_zh.add(segment['start'], segment['end'], segment['text'])
    last_time = segment['end']
print(srt_ja)
print("========================")
pathlib.Path(r"H:\DATASETS\Animes\jlh1000pp.srt").write_text(str(srt_ja), encoding="utf-8")
# pathlib.Path(r"simple.srt").write_text(str(srt_ja), encoding="utf-8")
