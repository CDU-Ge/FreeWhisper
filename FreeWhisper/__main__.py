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
from pathlib import Path
from typing import Final

from PySide6.QtWidgets import QMainWindow

from FreeWhisper.ui import Ui_MainWindow
from torch_env import torch_env

os.environ['Path'] = f"{torch_env()};" + os.environ['Path']
ROOT: Final = Path(__file__).parent.absolute()


class FreeWhisper(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
