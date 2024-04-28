# -*- coding: utf-8 -*-
# Copyright (c) CDU

"""Model Docstrings

"""
from pathlib import Path

file = Path('transcript.txt')

result = ''

for line in file.read_text().splitlines():
    _, line = line.split(']')
    line = line.strip()
    result += f' {line}'

print(result)
