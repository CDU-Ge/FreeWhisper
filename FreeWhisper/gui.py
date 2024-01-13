# -*- coding: utf-8 -*-
# Copyright (c) CDU

"""Model Docstrings

"""

import logging
import sys

from PySide6.QtWidgets import QMainWindow
from PySide6 import QtWidgets, QtCore

from FreeWhisper.ui import Ui_MainWindow
from FreeWhisper import utils


class FreeWhisper(QMainWindow, Ui_MainWindow):
    def __init__(self, **kwargs):
        super().__init__()
        self.setupUi(self)
        self.config = None
        self.logger = kwargs.get('logger', logging)
        self.w_input_select.clicked.connect(self.input_select)

    def load_config(self, config_name: str = 'config'):
        global SUPPORT_LANGUAGE
        from FreeWhisper.runtime import SUPPORT_LANGUAGE as _SUPPORT_LANGUAGE
        SUPPORT_LANGUAGE = _SUPPORT_LANGUAGE
        self.w_lang_lang.addItems(SUPPORT_LANGUAGE)

    @QtCore.Slot()
    def input_select(self):
        utils.logger.info('Click w_input_select')
        QtWidgets.QFileDialog.getOpenFileName(
            self, "选择音频文件",
            filter="",
            options=QtWidgets.QFileDialog.Option.DontUseNativeDialog
        )


def launch_gui(argv):
    from PySide6 import QtWidgets
    app = QtWidgets.QApplication(argv)
    free_whisper = FreeWhisper()
    free_whisper.show()
    free_whisper.load_config()
    sys.exit(app.exec())
