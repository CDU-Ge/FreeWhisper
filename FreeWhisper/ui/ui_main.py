# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainxcuGNV.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QProgressBar,
    QPushButton, QSizePolicy, QStatusBar, QTextBrowser,
    QVBoxLayout, QWidget)

from widgets import CircleWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(646, 558)
        MainWindow.setStyleSheet(u"")
        MainWindow.setAnimated(True)
        self.actionabout = QAction(MainWindow)
        self.actionabout.setObjectName(u"actionabout")
        self.actioncopyright = QAction(MainWindow)
        self.actioncopyright.setObjectName(u"actioncopyright")
        self.actionclear = QAction(MainWindow)
        self.actionclear.setObjectName(u"actionclear")
        self.actionexit = QAction(MainWindow)
        self.actionexit.setObjectName(u"actionexit")
        self.actionreboot = QAction(MainWindow)
        self.actionreboot.setObjectName(u"actionreboot")
        self.actionfile = QAction(MainWindow)
        self.actionfile.setObjectName(u"actionfile")
        self.actioncheck = QAction(MainWindow)
        self.actioncheck.setObjectName(u"actioncheck")
        self.actioninstall = QAction(MainWindow)
        self.actioninstall.setObjectName(u"actioninstall")
        self.actionupdate = QAction(MainWindow)
        self.actionupdate.setObjectName(u"actionupdate")
        self.actionuninstall = QAction(MainWindow)
        self.actionuninstall.setObjectName(u"actionuninstall")
        self.actionversion = QAction(MainWindow)
        self.actionversion.setObjectName(u"actionversion")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.gridLayout.setObjectName(u"gridLayout")
        self.StatusIndicator = QGroupBox(self.centralwidget)
        self.StatusIndicator.setObjectName(u"StatusIndicator")
        self.horizontalLayout = QHBoxLayout(self.StatusIndicator)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.state_lable = QLabel(self.StatusIndicator)
        self.state_lable.setObjectName(u"state_lable")
        self.state_lable.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.state_lable)

        self.state_indicator = CircleWidget(self.StatusIndicator)
        self.state_indicator.setObjectName(u"state_indicator")
        self.state_indicator.setMinimumSize(QSize(67, 32))
        self.state_indicator.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.state_indicator)


        self.gridLayout.addWidget(self.StatusIndicator, 2, 6, 1, 1)

        self.w_main_paste = QPushButton(self.centralwidget)
        self.w_main_paste.setObjectName(u"w_main_paste")

        self.gridLayout.addWidget(self.w_main_paste, 10, 6, 1, 1)

        self.wg_models = QWidget(self.centralwidget)
        self.wg_models.setObjectName(u"wg_models")
        self.verticalLayout_3 = QVBoxLayout(self.wg_models)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_6 = QLabel(self.wg_models)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_3.addWidget(self.label_6)

        self.w_models_model = QComboBox(self.wg_models)
        self.w_models_model.setObjectName(u"w_models_model")

        self.verticalLayout_3.addWidget(self.w_models_model)


        self.gridLayout.addWidget(self.wg_models, 5, 6, 1, 1)

        self.wc_control = QWidget(self.centralwidget)
        self.wc_control.setObjectName(u"wc_control")
        self.verticalLayout = QVBoxLayout(self.wc_control)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.w_control_start = QPushButton(self.wc_control)
        self.w_control_start.setObjectName(u"w_control_start")

        self.verticalLayout.addWidget(self.w_control_start)

        self.w_control_stop = QPushButton(self.wc_control)
        self.w_control_stop.setObjectName(u"w_control_stop")

        self.verticalLayout.addWidget(self.w_control_stop)


        self.gridLayout.addWidget(self.wc_control, 3, 6, 1, 1)

        self.app_title = QLabel(self.centralwidget)
        self.app_title.setObjectName(u"app_title")
        self.app_title.setMaximumSize(QSize(16777215, 100))
        self.app_title.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border: 0px solid;\n"
"border-radius: 8px;\n"
"padding-top: 8px;\n"
"padding-bottom: 8px;\n"
"padding-left: 8px;\n"
"padding-right: 8px;\n"
"box-sizing: border-box;")

        self.gridLayout.addWidget(self.app_title, 1, 0, 1, 1)

        self.w_main_result = QTextBrowser(self.centralwidget)
        self.w_main_result.setObjectName(u"w_main_result")

        self.gridLayout.addWidget(self.w_main_result, 3, 0, 8, 6)

        self.w_main_copy = QPushButton(self.centralwidget)
        self.w_main_copy.setObjectName(u"w_main_copy")

        self.gridLayout.addWidget(self.w_main_copy, 9, 6, 1, 1)

        self.wg_lang = QWidget(self.centralwidget)
        self.wg_lang.setObjectName(u"wg_lang")
        self.verticalLayout_2 = QVBoxLayout(self.wg_lang)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.wg_lang)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.w_lang_lang = QComboBox(self.wg_lang)
        self.w_lang_lang.setObjectName(u"w_lang_lang")

        self.verticalLayout_2.addWidget(self.w_lang_lang)


        self.gridLayout.addWidget(self.wg_lang, 6, 6, 1, 1)

        self.wg_zh = QWidget(self.centralwidget)
        self.wg_zh.setObjectName(u"wg_zh")
        self.verticalLayout_4 = QVBoxLayout(self.wg_zh)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.wg_zh)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.w_zh_method = QComboBox(self.wg_zh)
        self.w_zh_method.setObjectName(u"w_zh_method")

        self.verticalLayout_4.addWidget(self.w_zh_method)

        self.w_zh_convert = QPushButton(self.wg_zh)
        self.w_zh_convert.setObjectName(u"w_zh_convert")

        self.verticalLayout_4.addWidget(self.w_zh_convert)


        self.gridLayout.addWidget(self.wg_zh, 7, 6, 2, 1)

        self.wg_progress = QWidget(self.centralwidget)
        self.wg_progress.setObjectName(u"wg_progress")
        self.horizontalLayout_4 = QHBoxLayout(self.wg_progress)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.wg_progress)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.w_progress_bar = QProgressBar(self.wg_progress)
        self.w_progress_bar.setObjectName(u"w_progress_bar")
        self.w_progress_bar.setValue(0)
        self.w_progress_bar.setTextVisible(False)

        self.horizontalLayout_4.addWidget(self.w_progress_bar)


        self.gridLayout.addWidget(self.wg_progress, 2, 0, 1, 6)

        self.wc_input = QWidget(self.centralwidget)
        self.wc_input.setObjectName(u"wc_input")
        self.horizontalLayout_2 = QHBoxLayout(self.wc_input)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.wc_input)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.w_input_file = QLineEdit(self.wc_input)
        self.w_input_file.setObjectName(u"w_input_file")

        self.horizontalLayout_2.addWidget(self.w_input_file)

        self.w_input_select = QPushButton(self.wc_input)
        self.w_input_select.setObjectName(u"w_input_select")

        self.horizontalLayout_2.addWidget(self.w_input_select)


        self.gridLayout.addWidget(self.wc_input, 1, 2, 1, 1)

        self.wc_jion = QWidget(self.centralwidget)
        self.wc_jion.setObjectName(u"wc_jion")
        self.horizontalLayout_3 = QHBoxLayout(self.wc_jion)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.wc_jion)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.w_jion_key = QLineEdit(self.wc_jion)
        self.w_jion_key.setObjectName(u"w_jion_key")

        self.horizontalLayout_3.addWidget(self.w_jion_key)


        self.gridLayout.addWidget(self.wc_jion, 1, 5, 1, 2)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 1, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 646, 22))
        self.menu_about = QMenu(self.menubar)
        self.menu_about.setObjectName(u"menu_about")
        self.menu_file = QMenu(self.menubar)
        self.menu_file.setObjectName(u"menu_file")
        self.menu_file_open = QMenu(self.menu_file)
        self.menu_file_open.setObjectName(u"menu_file_open")
        self.menu_edit = QMenu(self.menubar)
        self.menu_edit.setObjectName(u"menu_edit")
        self.menu_py = QMenu(self.menubar)
        self.menu_py.setObjectName(u"menu_py")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_edit.menuAction())
        self.menubar.addAction(self.menu_py.menuAction())
        self.menubar.addAction(self.menu_about.menuAction())
        self.menu_about.addAction(self.actionabout)
        self.menu_about.addSeparator()
        self.menu_about.addAction(self.actioncopyright)
        self.menu_file.addAction(self.menu_file_open.menuAction())
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.actionreboot)
        self.menu_file.addAction(self.actionexit)
        self.menu_file_open.addAction(self.actionfile)
        self.menu_edit.addAction(self.actionclear)
        self.menu_py.addAction(self.actioncheck)
        self.menu_py.addAction(self.actioninstall)
        self.menu_py.addAction(self.actionupdate)
        self.menu_py.addAction(self.actionuninstall)
        self.menu_py.addSeparator()
        self.menu_py.addAction(self.actionversion)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FreeWhisper", None))
        self.actionabout.setText(QCoreApplication.translate("MainWindow", u"about", None))
        self.actioncopyright.setText(QCoreApplication.translate("MainWindow", u"copyright", None))
        self.actionclear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664", None))
        self.actionexit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.actionreboot.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u542f", None))
        self.actionfile.setText(QCoreApplication.translate("MainWindow", u"file", None))
        self.actioncheck.setText(QCoreApplication.translate("MainWindow", u"check", None))
        self.actioninstall.setText(QCoreApplication.translate("MainWindow", u"install", None))
        self.actionupdate.setText(QCoreApplication.translate("MainWindow", u"update", None))
        self.actionuninstall.setText(QCoreApplication.translate("MainWindow", u"uninstall", None))
        self.actionversion.setText(QCoreApplication.translate("MainWindow", u"version", None))
        self.StatusIndicator.setTitle("")
        self.state_lable.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u4efb\u52a1\u72b6\u6001:</p></body></html>", None))
        self.state_indicator.setText("")
        self.w_main_paste.setText(QCoreApplication.translate("MainWindow", u"\u7c98\u8d34", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b", None))
        self.w_control_start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.w_control_stop.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
        self.app_title.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:700;\">FreeWhisper</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u81ea\u7531\u7684\u4eab\u53d7\u79d1\u6280\u6210\u679c</p></body></html>", None))
        self.w_main_copy.setText(QCoreApplication.translate("MainWindow", u"\u590d\u5236", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u8bed\u8a00", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u7b80\u7e41\u4e92\u8f6c", None))
        self.w_zh_convert.setText(QCoreApplication.translate("MainWindow", u"\u8f6c\u5316", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5904\u7406\u8fdb\u5ea6", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u97f3\u9891\u6587\u4ef6", None))
        self.w_input_select.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u65ad\u53e5\u5206\u5272\u7b26", None))
#if QT_CONFIG(tooltip)
        self.w_jion_key.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u65ad\u53e5\u5206\u5272\u7b26\u53f7</p><p>\u7531\u4e8e\u6a21\u578bAI\u6a21\u578b\u4e0d\u4f1a\u5728\u65ad\u53e5\u5904\u52a0\u5165\u5206\u5272\u7b26\uff0c\u6240\u4ee5\u9700\u8981\u4f60\u81ea\u884c\u6dfb\u52a0\u7b26\u53f7</p><p>\u5982\u4f55\u9700\u8981\u4f7f\u7528\u7a7a\u683c\u8bf7\u7528: [SPACE]\u4ee3\u66ff</p><p>\u5982\u679c\u9700\u8981\u4f7f\u7528\u6362\u884c\u8bf7\u7528: [LINE]\u4ee3\u66ff</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.menu_about.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_file_open.setTitle(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.menu_edit.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None))
        self.menu_py.setTitle(QCoreApplication.translate("MainWindow", u"Python", None))
    # retranslateUi

