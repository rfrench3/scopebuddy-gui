# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aboutBuZRsW.ui'
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
    QTabWidget, QTextBrowser, QVBoxLayout, QWidget)

class Ui_Dialog_About(object):
    def setupUi(self, Dialog_About):
        if not Dialog_About.objectName():
            Dialog_About.setObjectName(u"Dialog_About")
        Dialog_About.resize(454, 472)
        self.verticalLayout = QVBoxLayout(Dialog_About)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 6, 0, 0)
        self.tabWidget = QTabWidget(Dialog_About)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.textBrowser = QTextBrowser(self.tab)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMouseTracking(True)
        self.textBrowser.setFrameShape(QFrame.Shape.StyledPanel)
        self.textBrowser.setFrameShadow(QFrame.Shadow.Sunken)
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setOpenLinks(True)

        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)

        self.line_2 = QFrame(self.tab)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_2 = QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.textBrowser_2 = QTextBrowser(self.tab_2)
        self.textBrowser_2.setObjectName(u"textBrowser_2")

        self.gridLayout_2.addWidget(self.textBrowser_2, 0, 0, 1, 1)

        self.line = QFrame(self.tab_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.widget = QWidget(Dialog_About)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(283, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_okay = QPushButton(self.widget)
        self.pushButton_okay.setObjectName(u"pushButton_okay")

        self.horizontalLayout.addWidget(self.pushButton_okay)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Dialog_About)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog_About)
    # setupUi

    def retranslateUi(self, Dialog_About):
        Dialog_About.setWindowTitle(QCoreApplication.translate("Dialog_About", u"Dialog", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Dialog_About", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog_About", u"Credits", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("Dialog_About", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">For more detailed information, be sure to review the documentation for </span><a href=\"https://github.com/ValveSoftware/gamescope\"><span style=\" text-decoration: underline; color:#bfbce9;\">Gamescope</span></a><span style=\" font-style:italic;\"> and </span><a href=\"https://github.com/HikariKnight/ScopeBuddy\"><span style=\" text-decoration: underline; color:#"
                        "bfbce9;\">Scopebuddy</span></a><span style=\" font-style:italic;\">.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A text field left blank is the same as a checkbox left unchecked \u2013 it will use Gamescope's default setting. Sometimes a field cannot be left blank, such as providing width without height, because Gamescope does not allow for it.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">When the GUI applies a new config, it comments out the old config in <span style=\" font-weight:700;\">~/.config/sco"
                        "pebuddy/</span> while adding a new line with the new config. This means worse-case, you can manually reapply any old configuration! <span style=\" font-weight:700;\">It can build up over time with excessive config editing,</span> but text files are small and it is easy enough to manually clean out if ever necessary.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br />Scopebuddy itself is extremely powerful, and this GUI does not currently aim to cover all of its power \u2013 it <span style=\" font-style:italic;\">does</span> aim to be safe to use alongside any such advanced configuration, however.</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog_About", u"Usage", None))
        self.pushButton_okay.setText(QCoreApplication.translate("Dialog_About", u"Okay", None))
    # retranslateUi

