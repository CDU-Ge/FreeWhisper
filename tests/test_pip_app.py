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
import optparse

# warnings.filterwarnings(
#     "ignore", category=DeprecationWarning, module=".*packaging\\.version"
# )
from pip._internal.cli.main import main as _main

if __name__ == '__main__':
    _main(['install', '-U', 'pip', '-t', './test_libs'])
