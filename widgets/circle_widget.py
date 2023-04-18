# -*- coding: utf-8 -*-
# Copyright (c) CDU

"""Model Docstrings

"""

from __future__ import absolute_import
from __future__ import annotations
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sys

from PySide6.QtGui import QBrush
from PySide6.QtGui import QColor
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QWidget, QLabel


class CircleWidget(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(12, 12)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(QColor(255, 0, 0)))
        painter.drawEllipse(self.rect())


if __name__ == '__main__':
    from widgets.tools import test_widget

    sys.exit(test_widget(CircleWidget))
