# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aboutmkcHCE.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QPushButton, QSizePolicy, QSpacerItem, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(454, 453)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser = QTextBrowser(Dialog)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMouseTracking(True)
        self.textBrowser.setFrameShape(QFrame.Shape.StyledPanel)
        self.textBrowser.setFrameShadow(QFrame.Shadow.Sunken)
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setOpenLinks(True)

        self.verticalLayout.addWidget(self.textBrowser)

        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(283, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_okay = QPushButton(self.widget)
        self.pushButton_okay.setObjectName(u"pushButton_okay")

        self.horizontalLayout.addWidget(self.pushButton_okay)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Gamescope</span> is a micro-compositor made by ValveSoftware that is used to simplify running games and other software. It can handle a lot of things many games struggle with such as extreme resolutions, entering fullscreen, extremely wide monitors, and more! This can greatly reduce glitchy behavior, improving the gaming experience. </p>\n"
"<p style=\" margin-top:0"
                        "px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/ValveSoftware/gamescope\"><span style=\" text-decoration: underline; color:#bfbce9;\">Here's its github page!</span></a><br /><br /><span style=\" font-weight:700;\">Scopebuddy</span> is a tool made by HikariKnight that makes it easier to use Gamescope. It allows you to do many things, which includes creating a general Gamescope configuration for all of your games. </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/HikariKnight/ScopeBuddy\"><span style=\" text-decoration: underline; color:#bfbce9;\">Here's its github page!</span></a></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /><span style=\" font-weight:700;\">Scopebuddy-gui</span> (this program) was not made by HikariKnight. It is lacks man"
                        "y of the features present in Scopebuddy itself, but provides an easy to use UI for the more basic features of scopebuddy.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/rfrench3/scopebuddy-gui\"><span style=\" text-decoration: underline; color:#bfbce9;\">Here's its github page!</span></a></p></body></html>", None))
        self.pushButton_okay.setText(QCoreApplication.translate("Dialog", u"Okay", None))
    # retranslateUi

