# -*- coding: utf-8 -*-
# Copyright (c) CDU

"""Model Docstrings

"""


class AAC:
    def __init__(self, filename: str):
        self._filename = filename

    @property
    def duration(self):
        raise TypeError("AAC can't get duration")
