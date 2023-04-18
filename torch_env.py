# -*- coding: utf-8 -*-
# Copyright (c) CDU

"""Model Docstrings

"""

from __future__ import absolute_import
from __future__ import annotations
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os


def torch_env(home: str = None) -> str:
    home = home if home else os.environ.get('CUDA_PATH_PROJECT')
    _bin = os.path.join(home, 'bin')
    _libnvvp = os.path.join(home, 'libnvvp')
    return ';'.join(map(os.path.abspath, [_bin, _libnvvp]))
