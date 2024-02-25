# -*- coding: utf-8 -*-
# Copyright (c) CDU

"""Model Docstrings

"""

from __future__ import absolute_import
from __future__ import annotations
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import pysrt

srt = pysrt.open("simple.srt", encoding='utf-8')
print(srt)
for i in srt:
    print(i.text)
    print(i.start)
    print(i.end)
    print(i.duration)
srt.save(r"H:\DATASETS\Animes\jlh1000.srt")