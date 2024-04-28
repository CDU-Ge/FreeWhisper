# -*- coding: utf-8 -*-
# Copyright (c) CDU

"""Model Docstrings

"""

from __future__ import absolute_import
from __future__ import annotations
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os.path
import sys
from dotenv import load_dotenv

if __name__ == '__main__':
    if os.path.exists('.dev.env'):
        load_dotenv('.dev.env')
    from FreeWhisper.__main__ import main

    main(sys.argv)
