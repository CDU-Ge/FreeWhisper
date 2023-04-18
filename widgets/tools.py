# -*- coding: utf-8 -*-
# Copyright (c) CDU

"""Model Docstrings

"""

from __future__ import absolute_import
from __future__ import annotations
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from typing import Any
from typing import Callable


def test_widget(widget: Callable[[Any], ...]):
    from PySide6.QtWidgets import QMainWindow, QApplication

    class MainWindow(QMainWindow):
        def __init__(self, _widget=widget):
            super().__init__()
            self.test_widget = _widget(self)
            self.setCentralWidget(self.test_widget)

    app = QApplication([])
    window = MainWindow()
    window.show()
    return app.exec()
