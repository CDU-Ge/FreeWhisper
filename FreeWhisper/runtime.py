# -*- coding: utf-8 -*-
# Copyright (c) CDU

"""Model Docstrings

"""

from __future__ import absolute_import
from __future__ import annotations
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from whisper import tokenizer

LANGUAGES = tokenizer.LANGUAGES
TO_LANGUAGE_CODE = tokenizer.TO_LANGUAGE_CODE
SUPPORT_LANGUAGE = [
    lang for lang in sorted(TO_LANGUAGE_CODE.keys())
]
