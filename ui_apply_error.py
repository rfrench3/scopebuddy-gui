# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'apply_errorTcyvSM.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QPushButton, QSizePolicy, QSpacerItem,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_Dialog_ApplyError(object):
    def setupUi(self, Dialog_ApplyError):
        if not Dialog_ApplyError.objectName():
            Dialog_ApplyError.setObjectName(u"Dialog_ApplyError")
        Dialog_ApplyError.setWindowModality(Qt.WindowModality.WindowModal)
        Dialog_ApplyError.resize(400, 248)
        self.verticalLayout = QVBoxLayout(Dialog_ApplyError)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(Dialog_ApplyError)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.Shape.Box)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.frame_2)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.textBrowser = QTextBrowser(self.widget_3)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setFrameShape(QFrame.Shape.NoFrame)

        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.widget_3)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(Dialog_ApplyError)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(193, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_Ok = QPushButton(self.frame)
        self.pushButton_Ok.setObjectName(u"pushButton_Ok")

        self.horizontalLayout.addWidget(self.pushButton_Ok)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog_ApplyError)

        QMetaObject.connectSlotsByName(Dialog_ApplyError)
    # setupUi

    def retranslateUi(self, Dialog_ApplyError):
        Dialog_ApplyError.setWindowTitle(QCoreApplication.translate("Dialog_ApplyError", u"Dialog", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Dialog_ApplyError", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Error: Your set of arguments are incompatible!</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />TODO: provide exact error, highlight conflicting input boxes until user interacts with them again<br /><br />Some common issues are:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0p"
                        "x; -qt-block-indent:0; text-indent:0px;\">- setting Rendered Width without setting Rendered Height</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- setting Output Width without setting Output Height</p></body></html>", None))
        self.pushButton_Ok.setText(QCoreApplication.translate("Dialog_ApplyError", u"Ok", None))
    # retranslateUi

