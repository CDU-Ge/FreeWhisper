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
import logging
import pathlib

logger = logging.getLogger("FreeWhisper")


def set_debug():
    logger.setLevel(logging.DEBUG)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)


class Time:
    def __init__(self, hour, minute, second, millisecond):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.millisecond = millisecond
        for i in [self.hour, self.minute, self.second]:
            if not (0 <= i <= 59):
                raise ValueError(f"invalid time {self.hour}:{self.minute}:{self.second}")
        # self.millisecond = int(self.millisecond / 1000 * 60)

    @classmethod
    def from_seconds(cls, seconds: float):
        def correct_timestamp(s, fps):
            # 计算总毫秒数
            total_ms = s * 1000

            # 计算修正后的毫秒数
            corrected_ms = total_ms - (total_ms % int(1 / fps * 1000))

            # 计算修正后的小时、分钟、秒和毫秒
            corrected_hour = corrected_ms // 3600000
            corrected_ms %= 3600000

            corrected_minute = corrected_ms // 60000
            corrected_ms %= 60000

            corrected_second = corrected_ms // 1000
            corrected_ms %= 1000

            return corrected_hour, corrected_minute, corrected_second, corrected_ms

        return cls(*map(int, correct_timestamp(seconds, 29.97)))

    def __str__(self):
        return f"{self.hour:02}:{self.minute:02}:{self.second:02},{self.millisecond}"


class Srt:
    def __init__(self):
        self.srt = []

    def add(self, start: float, end: float, text: str):
        self.srt.append((Time.from_seconds(start), Time.from_seconds(end), text))

    def __str__(self):
        s = ""
        for i, (start, end, text) in enumerate(self.srt):
            s += f"{i + 1}\n"
            s += f"{start} --> {end}\n"
            s += f"{text}\n\n"
        return s


class TranslateCache:
    def __init__(self, path: pathlib.Path, translate):
        self.path = path
        self.translate = translate
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
            result = self.translate(text)
            self.add(text, result)
            return result

    def add(self, text: str, result: str):
        key = hashlib.md5(text.encode("utf-8")).hexdigest()
        result = result.replace("\n", "\\n")
        self.cache[key] = result
        with self.path.open('a', encoding='utf-8') as f:
            f.write(f"{key}:{result}\n")

    @staticmethod
    def encode(text: str, seg="<|CDU-NEWLINE|>"):
        """
        make text in one line
        Args:
            seg:
            text:

        Returns:

        """
        return text.replace("\r\n", "\n").replace("\r", "\n").replace("\n", "")
