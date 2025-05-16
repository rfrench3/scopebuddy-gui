# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowWJwEbP.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QDoubleSpinBox, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListView, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 694)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_9 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, -1, -1, -1)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, -1, 0, 0)
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.listWidget_gamesList = QListWidget(self.frame)
        QListWidgetItem(self.listWidget_gamesList)
        QListWidgetItem(self.listWidget_gamesList)
        self.listWidget_gamesList.setObjectName(u"listWidget_gamesList")
        self.listWidget_gamesList.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(5)
        sizePolicy2.setHeightForWidth(self.listWidget_gamesList.sizePolicy().hasHeightForWidth())
        self.listWidget_gamesList.setSizePolicy(sizePolicy2)
        self.listWidget_gamesList.setFrameShape(QFrame.Shape.Box)
        self.listWidget_gamesList.setFrameShadow(QFrame.Shadow.Raised)
        self.listWidget_gamesList.setLineWidth(0)
        self.listWidget_gamesList.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.listWidget_gamesList.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.listWidget_gamesList.setTabKeyNavigation(True)
        self.listWidget_gamesList.setMovement(QListView.Movement.Static)

        self.verticalLayout.addWidget(self.listWidget_gamesList)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(1)
        sizePolicy3.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy3)
        self.frame_5.setFrameShape(QFrame.Shape.Box)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_5)
        self.horizontalLayout.setSpacing(18)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(18, 18, 18, 18)
        self.toolButton_addGame = QToolButton(self.frame_5)
        self.toolButton_addGame.setObjectName(u"toolButton_addGame")
        self.toolButton_addGame.setEnabled(False)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.toolButton_addGame.sizePolicy().hasHeightForWidth())
        self.toolButton_addGame.setSizePolicy(sizePolicy4)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.toolButton_addGame.setIcon(icon)
        self.toolButton_addGame.setCheckable(False)

        self.horizontalLayout.addWidget(self.toolButton_addGame)

        self.toolButton_removeGame = QToolButton(self.frame_5)
        self.toolButton_removeGame.setObjectName(u"toolButton_removeGame")
        self.toolButton_removeGame.setEnabled(False)
        sizePolicy4.setHeightForWidth(self.toolButton_removeGame.sizePolicy().hasHeightForWidth())
        self.toolButton_removeGame.setSizePolicy(sizePolicy4)
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListRemove))
        self.toolButton_removeGame.setIcon(icon1)

        self.horizontalLayout.addWidget(self.toolButton_removeGame)


        self.verticalLayout.addWidget(self.frame_5)


        self.horizontalLayout_9.addWidget(self.frame)

        self.stackedWidget_settingsPanel = QStackedWidget(self.frame_2)
        self.stackedWidget_settingsPanel.setObjectName(u"stackedWidget_settingsPanel")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Ignored)
        sizePolicy5.setHorizontalStretch(3)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.stackedWidget_settingsPanel.sizePolicy().hasHeightForWidth())
        self.stackedWidget_settingsPanel.setSizePolicy(sizePolicy5)
        self.stackedWidget_settingsPanel.setFrameShape(QFrame.Shape.Box)
        self.stackedWidget_settingsPanel.setFrameShadow(QFrame.Shadow.Raised)
        self.stackedWidget_gamesDefault = QWidget()
        self.stackedWidget_gamesDefault.setObjectName(u"stackedWidget_gamesDefault")
        self.gridLayout_3 = QGridLayout(self.stackedWidget_gamesDefault)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_settings = QScrollArea(self.stackedWidget_gamesDefault)
        self.scrollArea_settings.setObjectName(u"scrollArea_settings")
        self.scrollArea_settings.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollArea_settings.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -139, 570, 960))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget1_rW = QWidget(self.scrollAreaWidgetContents)
        self.widget1_rW.setObjectName(u"widget1_rW")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.widget1_rW.sizePolicy().hasHeightForWidth())
        self.widget1_rW.setSizePolicy(sizePolicy6)
        self.verticalLayout_3 = QVBoxLayout(self.widget1_rW)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_10 = QWidget(self.widget1_rW)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy7)
        self.horizontalLayout_4 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_10)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.horizontalSpacer_3 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.lineEdit_rWidth = QLineEdit(self.widget_10)
        self.lineEdit_rWidth.setObjectName(u"lineEdit_rWidth")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.lineEdit_rWidth.sizePolicy().hasHeightForWidth())
        self.lineEdit_rWidth.setSizePolicy(sizePolicy8)
        self.lineEdit_rWidth.setMaxLength(4)

        self.horizontalLayout_4.addWidget(self.lineEdit_rWidth)


        self.verticalLayout_3.addWidget(self.widget_10)

        self.line_3 = QFrame(self.widget1_rW)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_3)


        self.verticalLayout_5.addWidget(self.widget1_rW)

        self.widget2_rH = QWidget(self.scrollAreaWidgetContents)
        self.widget2_rH.setObjectName(u"widget2_rH")
        sizePolicy6.setHeightForWidth(self.widget2_rH.sizePolicy().hasHeightForWidth())
        self.widget2_rH.setSizePolicy(sizePolicy6)
        self.verticalLayout_4 = QVBoxLayout(self.widget2_rH)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_11 = QWidget(self.widget2_rH)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy7.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy7)
        self.horizontalLayout_5 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget_11)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.horizontalSpacer_4 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.lineEdit_rHeight = QLineEdit(self.widget_11)
        self.lineEdit_rHeight.setObjectName(u"lineEdit_rHeight")
        sizePolicy8.setHeightForWidth(self.lineEdit_rHeight.sizePolicy().hasHeightForWidth())
        self.lineEdit_rHeight.setSizePolicy(sizePolicy8)
        self.lineEdit_rHeight.setMaxLength(4)

        self.horizontalLayout_5.addWidget(self.lineEdit_rHeight)


        self.verticalLayout_4.addWidget(self.widget_11)

        self.line_4 = QFrame(self.widget2_rH)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_4)


        self.verticalLayout_5.addWidget(self.widget2_rH)

        self.widget3_fps = QWidget(self.scrollAreaWidgetContents)
        self.widget3_fps.setObjectName(u"widget3_fps")
        sizePolicy6.setHeightForWidth(self.widget3_fps.sizePolicy().hasHeightForWidth())
        self.widget3_fps.setSizePolicy(sizePolicy6)
        self.verticalLayout_2 = QVBoxLayout(self.widget3_fps)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_9 = QWidget(self.widget3_fps)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy7.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy7)
        self.horizontalLayout_3 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_9)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.horizontalSpacer_2 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.lineEdit_fps = QLineEdit(self.widget_9)
        self.lineEdit_fps.setObjectName(u"lineEdit_fps")
        sizePolicy8.setHeightForWidth(self.lineEdit_fps.sizePolicy().hasHeightForWidth())
        self.lineEdit_fps.setSizePolicy(sizePolicy8)
        self.lineEdit_fps.setMaxLength(4)

        self.horizontalLayout_3.addWidget(self.lineEdit_fps)


        self.verticalLayout_2.addWidget(self.widget_9)

        self.line_2 = QFrame(self.widget3_fps)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)


        self.verticalLayout_5.addWidget(self.widget3_fps)

        self.widget4_oW = QWidget(self.scrollAreaWidgetContents)
        self.widget4_oW.setObjectName(u"widget4_oW")
        sizePolicy6.setHeightForWidth(self.widget4_oW.sizePolicy().hasHeightForWidth())
        self.widget4_oW.setSizePolicy(sizePolicy6)
        self.verticalLayout_7 = QVBoxLayout(self.widget4_oW)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_15 = QWidget(self.widget4_oW)
        self.widget_15.setObjectName(u"widget_15")
        sizePolicy7.setHeightForWidth(self.widget_15.sizePolicy().hasHeightForWidth())
        self.widget_15.setSizePolicy(sizePolicy7)
        self.horizontalLayout_7 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget_15)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.horizontalSpacer_6 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)

        self.lineEdit_oWidth = QLineEdit(self.widget_15)
        self.lineEdit_oWidth.setObjectName(u"lineEdit_oWidth")
        sizePolicy8.setHeightForWidth(self.lineEdit_oWidth.sizePolicy().hasHeightForWidth())
        self.lineEdit_oWidth.setSizePolicy(sizePolicy8)
        self.lineEdit_oWidth.setMaxLength(4)

        self.horizontalLayout_7.addWidget(self.lineEdit_oWidth)


        self.verticalLayout_7.addWidget(self.widget_15)

        self.line_6 = QFrame(self.widget4_oW)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_7.addWidget(self.line_6)


        self.verticalLayout_5.addWidget(self.widget4_oW)

        self.widget5_oH = QWidget(self.scrollAreaWidgetContents)
        self.widget5_oH.setObjectName(u"widget5_oH")
        sizePolicy6.setHeightForWidth(self.widget5_oH.sizePolicy().hasHeightForWidth())
        self.widget5_oH.setSizePolicy(sizePolicy6)
        self.verticalLayout_6 = QVBoxLayout(self.widget5_oH)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_13 = QWidget(self.widget5_oH)
        self.widget_13.setObjectName(u"widget_13")
        sizePolicy7.setHeightForWidth(self.widget_13.sizePolicy().hasHeightForWidth())
        self.widget_13.setSizePolicy(sizePolicy7)
        self.horizontalLayout_6 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget_13)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.horizontalSpacer_5 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.lineEdit_oHeight = QLineEdit(self.widget_13)
        self.lineEdit_oHeight.setObjectName(u"lineEdit_oHeight")
        sizePolicy8.setHeightForWidth(self.lineEdit_oHeight.sizePolicy().hasHeightForWidth())
        self.lineEdit_oHeight.setSizePolicy(sizePolicy8)
        self.lineEdit_oHeight.setMaxLength(4)

        self.horizontalLayout_6.addWidget(self.lineEdit_oHeight)


        self.verticalLayout_6.addWidget(self.widget_13)

        self.line_5 = QFrame(self.widget5_oH)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line_5)


        self.verticalLayout_5.addWidget(self.widget5_oH)

        self.widget6_fullscreen = QWidget(self.scrollAreaWidgetContents)
        self.widget6_fullscreen.setObjectName(u"widget6_fullscreen")
        sizePolicy6.setHeightForWidth(self.widget6_fullscreen.sizePolicy().hasHeightForWidth())
        self.widget6_fullscreen.setSizePolicy(sizePolicy6)
        self.verticalLayout_10 = QVBoxLayout(self.widget6_fullscreen)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_21 = QWidget(self.widget6_fullscreen)
        self.widget_21.setObjectName(u"widget_21")
        sizePolicy7.setHeightForWidth(self.widget_21.sizePolicy().hasHeightForWidth())
        self.widget_21.setSizePolicy(sizePolicy7)
        self.horizontalLayout_10 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget_21)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_10.addWidget(self.label_8)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_9)

        self.checkBox_fullscreen = QCheckBox(self.widget_21)
        self.checkBox_fullscreen.setObjectName(u"checkBox_fullscreen")
        self.checkBox_fullscreen.setChecked(True)
        self.checkBox_fullscreen.setTristate(False)

        self.horizontalLayout_10.addWidget(self.checkBox_fullscreen)


        self.verticalLayout_10.addWidget(self.widget_21)

        self.line_9 = QFrame(self.widget6_fullscreen)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_10.addWidget(self.line_9)


        self.verticalLayout_5.addWidget(self.widget6_fullscreen)

        self.widget7_hdr = QWidget(self.scrollAreaWidgetContents)
        self.widget7_hdr.setObjectName(u"widget7_hdr")
        sizePolicy6.setHeightForWidth(self.widget7_hdr.sizePolicy().hasHeightForWidth())
        self.widget7_hdr.setSizePolicy(sizePolicy6)
        self.verticalLayout_18 = QVBoxLayout(self.widget7_hdr)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.widget_34 = QWidget(self.widget7_hdr)
        self.widget_34.setObjectName(u"widget_34")
        sizePolicy7.setHeightForWidth(self.widget_34.sizePolicy().hasHeightForWidth())
        self.widget_34.setSizePolicy(sizePolicy7)
        self.horizontalLayout_18 = QHBoxLayout(self.widget_34)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.widget_34)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_18.addWidget(self.label_16)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_15)

        self.checkBox_hdr = QCheckBox(self.widget_34)
        self.checkBox_hdr.setObjectName(u"checkBox_hdr")
        self.checkBox_hdr.setTristate(False)

        self.horizontalLayout_18.addWidget(self.checkBox_hdr)


        self.verticalLayout_18.addWidget(self.widget_34)

        self.line_17 = QFrame(self.widget7_hdr)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.Shape.HLine)
        self.line_17.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_18.addWidget(self.line_17)


        self.verticalLayout_5.addWidget(self.widget7_hdr)

        self.widget9_steam = QWidget(self.scrollAreaWidgetContents)
        self.widget9_steam.setObjectName(u"widget9_steam")
        sizePolicy6.setHeightForWidth(self.widget9_steam.sizePolicy().hasHeightForWidth())
        self.widget9_steam.setSizePolicy(sizePolicy6)
        self.verticalLayout_11 = QVBoxLayout(self.widget9_steam)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.widget_23 = QWidget(self.widget9_steam)
        self.widget_23.setObjectName(u"widget_23")
        sizePolicy7.setHeightForWidth(self.widget_23.sizePolicy().hasHeightForWidth())
        self.widget_23.setSizePolicy(sizePolicy7)
        self.horizontalLayout_11 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.widget_23)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_11.addWidget(self.label_9)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_10)

        self.checkBox_steam = QCheckBox(self.widget_23)
        self.checkBox_steam.setObjectName(u"checkBox_steam")
        self.checkBox_steam.setChecked(True)
        self.checkBox_steam.setTristate(False)

        self.horizontalLayout_11.addWidget(self.checkBox_steam)


        self.verticalLayout_11.addWidget(self.widget_23)

        self.line_10 = QFrame(self.widget9_steam)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.Shape.HLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_11.addWidget(self.line_10)


        self.verticalLayout_5.addWidget(self.widget9_steam)

        self.widget__10mangohud = QWidget(self.scrollAreaWidgetContents)
        self.widget__10mangohud.setObjectName(u"widget__10mangohud")
        sizePolicy6.setHeightForWidth(self.widget__10mangohud.sizePolicy().hasHeightForWidth())
        self.widget__10mangohud.setSizePolicy(sizePolicy6)
        self.verticalLayout_12 = QVBoxLayout(self.widget__10mangohud)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.widget_25 = QWidget(self.widget__10mangohud)
        self.widget_25.setObjectName(u"widget_25")
        sizePolicy7.setHeightForWidth(self.widget_25.sizePolicy().hasHeightForWidth())
        self.widget_25.setSizePolicy(sizePolicy7)
        self.horizontalLayout_12 = QHBoxLayout(self.widget_25)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget_25)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_12.addWidget(self.label_10)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_11)

        self.checkBox_mango = QCheckBox(self.widget_25)
        self.checkBox_mango.setObjectName(u"checkBox_mango")
        self.checkBox_mango.setTristate(False)

        self.horizontalLayout_12.addWidget(self.checkBox_mango)


        self.verticalLayout_12.addWidget(self.widget_25)

        self.line_11 = QFrame(self.widget__10mangohud)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.Shape.HLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_12.addWidget(self.line_11)


        self.verticalLayout_5.addWidget(self.widget__10mangohud)

        self.widget_24 = QWidget(self.scrollAreaWidgetContents)
        self.widget_24.setObjectName(u"widget_24")
        sizePolicy6.setHeightForWidth(self.widget_24.sizePolicy().hasHeightForWidth())
        self.widget_24.setSizePolicy(sizePolicy6)
        self.verticalLayout_20 = QVBoxLayout(self.widget_24)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.widget_27 = QWidget(self.widget_24)
        self.widget_27.setObjectName(u"widget_27")
        sizePolicy7.setHeightForWidth(self.widget_27.sizePolicy().hasHeightForWidth())
        self.widget_27.setSizePolicy(sizePolicy7)
        self.horizontalLayout_20 = QHBoxLayout(self.widget_27)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.widget_27)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_20.addWidget(self.label_18)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_18)

        self.checkBox_forceInternalFullscreen = QCheckBox(self.widget_27)
        self.checkBox_forceInternalFullscreen.setObjectName(u"checkBox_forceInternalFullscreen")
        self.checkBox_forceInternalFullscreen.setTristate(False)

        self.horizontalLayout_20.addWidget(self.checkBox_forceInternalFullscreen)


        self.verticalLayout_20.addWidget(self.widget_27)

        self.line_19 = QFrame(self.widget_24)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.Shape.HLine)
        self.line_19.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_20.addWidget(self.line_19)


        self.verticalLayout_5.addWidget(self.widget_24)

        self.widget__11_AdvancedSettings = QWidget(self.scrollAreaWidgetContents)
        self.widget__11_AdvancedSettings.setObjectName(u"widget__11_AdvancedSettings")
        sizePolicy6.setHeightForWidth(self.widget__11_AdvancedSettings.sizePolicy().hasHeightForWidth())
        self.widget__11_AdvancedSettings.setSizePolicy(sizePolicy6)
        self.verticalLayout_16 = QVBoxLayout(self.widget__11_AdvancedSettings)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.widget_30 = QWidget(self.widget__11_AdvancedSettings)
        self.widget_30.setObjectName(u"widget_30")
        sizePolicy7.setHeightForWidth(self.widget_30.sizePolicy().hasHeightForWidth())
        self.widget_30.setSizePolicy(sizePolicy7)
        self.horizontalLayout_16 = QHBoxLayout(self.widget_30)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.widget_30)
        self.label_14.setObjectName(u"label_14")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_14.setFont(font)
        self.label_14.setScaledContents(False)
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_14)


        self.verticalLayout_16.addWidget(self.widget_30)

        self.line_15 = QFrame(self.widget__11_AdvancedSettings)
        self.line_15.setObjectName(u"line_15")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.line_15.sizePolicy().hasHeightForWidth())
        self.line_15.setSizePolicy(sizePolicy9)
        self.line_15.setMinimumSize(QSize(0, 0))
        self.line_15.setMaximumSize(QSize(16777215, 16777215))
        self.line_15.setSizeIncrement(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(10)
        self.line_15.setFont(font1)
        self.line_15.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_15.setMidLineWidth(1)
        self.line_15.setFrameShape(QFrame.Shape.HLine)

        self.verticalLayout_16.addWidget(self.line_15)


        self.verticalLayout_5.addWidget(self.widget__11_AdvancedSettings)

        self.widget__12_maxScaleFactor = QWidget(self.scrollAreaWidgetContents)
        self.widget__12_maxScaleFactor.setObjectName(u"widget__12_maxScaleFactor")
        sizePolicy6.setHeightForWidth(self.widget__12_maxScaleFactor.sizePolicy().hasHeightForWidth())
        self.widget__12_maxScaleFactor.setSizePolicy(sizePolicy6)
        self.verticalLayout_14 = QVBoxLayout(self.widget__12_maxScaleFactor)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.widget_26 = QWidget(self.widget__12_maxScaleFactor)
        self.widget_26.setObjectName(u"widget_26")
        sizePolicy7.setHeightForWidth(self.widget_26.sizePolicy().hasHeightForWidth())
        self.widget_26.setSizePolicy(sizePolicy7)
        self.horizontalLayout_14 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.widget_26)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_14.addWidget(self.label_12)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_13)

        self.lineEdit_maxScaleFactor = QLineEdit(self.widget_26)
        self.lineEdit_maxScaleFactor.setObjectName(u"lineEdit_maxScaleFactor")
        sizePolicy8.setHeightForWidth(self.lineEdit_maxScaleFactor.sizePolicy().hasHeightForWidth())
        self.lineEdit_maxScaleFactor.setSizePolicy(sizePolicy8)
        self.lineEdit_maxScaleFactor.setMaxLength(4)

        self.horizontalLayout_14.addWidget(self.lineEdit_maxScaleFactor)


        self.verticalLayout_14.addWidget(self.widget_26)

        self.line_13 = QFrame(self.widget__12_maxScaleFactor)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.Shape.HLine)
        self.line_13.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_14.addWidget(self.line_13)


        self.verticalLayout_5.addWidget(self.widget__12_maxScaleFactor)

        self.widget__13_upscalerType = QWidget(self.scrollAreaWidgetContents)
        self.widget__13_upscalerType.setObjectName(u"widget__13_upscalerType")
        sizePolicy6.setHeightForWidth(self.widget__13_upscalerType.sizePolicy().hasHeightForWidth())
        self.widget__13_upscalerType.setSizePolicy(sizePolicy6)
        self.verticalLayout_17 = QVBoxLayout(self.widget__13_upscalerType)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.widget_32 = QWidget(self.widget__13_upscalerType)
        self.widget_32.setObjectName(u"widget_32")
        sizePolicy7.setHeightForWidth(self.widget_32.sizePolicy().hasHeightForWidth())
        self.widget_32.setSizePolicy(sizePolicy7)
        self.horizontalLayout_17 = QHBoxLayout(self.widget_32)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.widget_32)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_17.addWidget(self.label_15)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_16)

        self.comboBox_upscalerType = QComboBox(self.widget_32)
        self.comboBox_upscalerType.addItem("")
        self.comboBox_upscalerType.addItem("")
        self.comboBox_upscalerType.addItem("")
        self.comboBox_upscalerType.addItem("")
        self.comboBox_upscalerType.addItem("")
        self.comboBox_upscalerType.setObjectName(u"comboBox_upscalerType")
        sizePolicy8.setHeightForWidth(self.comboBox_upscalerType.sizePolicy().hasHeightForWidth())
        self.comboBox_upscalerType.setSizePolicy(sizePolicy8)

        self.horizontalLayout_17.addWidget(self.comboBox_upscalerType)


        self.verticalLayout_17.addWidget(self.widget_32)

        self.line_16 = QFrame(self.widget__13_upscalerType)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.Shape.HLine)
        self.line_16.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_17.addWidget(self.line_16)


        self.verticalLayout_5.addWidget(self.widget__13_upscalerType)

        self.widget__14_upscalerFilter = QWidget(self.scrollAreaWidgetContents)
        self.widget__14_upscalerFilter.setObjectName(u"widget__14_upscalerFilter")
        sizePolicy6.setHeightForWidth(self.widget__14_upscalerFilter.sizePolicy().hasHeightForWidth())
        self.widget__14_upscalerFilter.setSizePolicy(sizePolicy6)
        self.verticalLayout_19 = QVBoxLayout(self.widget__14_upscalerFilter)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.widget_36 = QWidget(self.widget__14_upscalerFilter)
        self.widget_36.setObjectName(u"widget_36")
        sizePolicy7.setHeightForWidth(self.widget_36.sizePolicy().hasHeightForWidth())
        self.widget_36.setSizePolicy(sizePolicy7)
        self.horizontalLayout_19 = QHBoxLayout(self.widget_36)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.widget_36)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_19.addWidget(self.label_17)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_17)

        self.comboBox_upscalerFilter = QComboBox(self.widget_36)
        self.comboBox_upscalerFilter.addItem("")
        self.comboBox_upscalerFilter.addItem("")
        self.comboBox_upscalerFilter.addItem("")
        self.comboBox_upscalerFilter.addItem("")
        self.comboBox_upscalerFilter.addItem("")
        self.comboBox_upscalerFilter.setObjectName(u"comboBox_upscalerFilter")

        self.horizontalLayout_19.addWidget(self.comboBox_upscalerFilter)


        self.verticalLayout_19.addWidget(self.widget_36)

        self.line_18 = QFrame(self.widget__14_upscalerFilter)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.Shape.HLine)
        self.line_18.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_19.addWidget(self.line_18)


        self.verticalLayout_5.addWidget(self.widget__14_upscalerFilter)

        self.widget__15_upscalerSharpness = QWidget(self.scrollAreaWidgetContents)
        self.widget__15_upscalerSharpness.setObjectName(u"widget__15_upscalerSharpness")
        sizePolicy6.setHeightForWidth(self.widget__15_upscalerSharpness.sizePolicy().hasHeightForWidth())
        self.widget__15_upscalerSharpness.setSizePolicy(sizePolicy6)
        self.verticalLayout_15 = QVBoxLayout(self.widget__15_upscalerSharpness)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.widget_28 = QWidget(self.widget__15_upscalerSharpness)
        self.widget_28.setObjectName(u"widget_28")
        sizePolicy7.setHeightForWidth(self.widget_28.sizePolicy().hasHeightForWidth())
        self.widget_28.setSizePolicy(sizePolicy7)
        self.horizontalLayout_15 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.widget_28)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_15.addWidget(self.label_13)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_14)

        self.lineEdit_upscalerSharpness = QLineEdit(self.widget_28)
        self.lineEdit_upscalerSharpness.setObjectName(u"lineEdit_upscalerSharpness")
        sizePolicy8.setHeightForWidth(self.lineEdit_upscalerSharpness.sizePolicy().hasHeightForWidth())
        self.lineEdit_upscalerSharpness.setSizePolicy(sizePolicy8)
        self.lineEdit_upscalerSharpness.setMaxLength(2)

        self.horizontalLayout_15.addWidget(self.lineEdit_upscalerSharpness)


        self.verticalLayout_15.addWidget(self.widget_28)

        self.line_14 = QFrame(self.widget__15_upscalerSharpness)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.Shape.HLine)
        self.line_14.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_15.addWidget(self.line_14)


        self.verticalLayout_5.addWidget(self.widget__15_upscalerSharpness)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.widget__16_mouseSensitivity = QWidget(self.scrollAreaWidgetContents)
        self.widget__16_mouseSensitivity.setObjectName(u"widget__16_mouseSensitivity")
        sizePolicy6.setHeightForWidth(self.widget__16_mouseSensitivity.sizePolicy().hasHeightForWidth())
        self.widget__16_mouseSensitivity.setSizePolicy(sizePolicy6)
        self.verticalLayout_21 = QVBoxLayout(self.widget__16_mouseSensitivity)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.widget_39 = QWidget(self.widget__16_mouseSensitivity)
        self.widget_39.setObjectName(u"widget_39")
        sizePolicy7.setHeightForWidth(self.widget_39.sizePolicy().hasHeightForWidth())
        self.widget_39.setSizePolicy(sizePolicy7)
        self.horizontalLayout_21 = QHBoxLayout(self.widget_39)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.widget_39)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_21.addWidget(self.label_19)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_19)

        self.doubleSpinBox_mouseSensitivity = QDoubleSpinBox(self.widget_39)
        self.doubleSpinBox_mouseSensitivity.setObjectName(u"doubleSpinBox_mouseSensitivity")
        self.doubleSpinBox_mouseSensitivity.setDecimals(1)
        self.doubleSpinBox_mouseSensitivity.setValue(1.000000000000000)

        self.horizontalLayout_21.addWidget(self.doubleSpinBox_mouseSensitivity)


        self.verticalLayout_21.addWidget(self.widget_39)

        self.line_20 = QFrame(self.widget__16_mouseSensitivity)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShape(QFrame.Shape.HLine)
        self.line_20.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_21.addWidget(self.line_20)


        self.verticalLayout_5.addWidget(self.widget__16_mouseSensitivity)

        self.widget__17_ = QWidget(self.scrollAreaWidgetContents)
        self.widget__17_.setObjectName(u"widget__17_")
        sizePolicy6.setHeightForWidth(self.widget__17_.sizePolicy().hasHeightForWidth())
        self.widget__17_.setSizePolicy(sizePolicy6)
        self.verticalLayout_22 = QVBoxLayout(self.widget__17_)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.widget_41 = QWidget(self.widget__17_)
        self.widget_41.setObjectName(u"widget_41")
        sizePolicy7.setHeightForWidth(self.widget_41.sizePolicy().hasHeightForWidth())
        self.widget_41.setSizePolicy(sizePolicy7)
        self.horizontalLayout_22 = QHBoxLayout(self.widget_41)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.widget_41)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_22.addWidget(self.label_20)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_20)

        self.checkBox_adaptiveSync = QCheckBox(self.widget_41)
        self.checkBox_adaptiveSync.setObjectName(u"checkBox_adaptiveSync")
        self.checkBox_adaptiveSync.setTristate(False)

        self.horizontalLayout_22.addWidget(self.checkBox_adaptiveSync)


        self.verticalLayout_22.addWidget(self.widget_41)

        self.line_21 = QFrame(self.widget__17_)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setFrameShape(QFrame.Shape.HLine)
        self.line_21.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_22.addWidget(self.line_21)


        self.verticalLayout_5.addWidget(self.widget__17_)

        self.scrollArea_settings.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_3.addWidget(self.scrollArea_settings, 0, 0, 1, 1)

        self.stackedWidget_settingsPanel.addWidget(self.stackedWidget_gamesDefault)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_8 = QVBoxLayout(self.page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_2 = QWidget(self.page)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy6.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy6)
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_20 = QWidget(self.widget_2)
        self.widget_20.setObjectName(u"widget_20")
        sizePolicy6.setHeightForWidth(self.widget_20.sizePolicy().hasHeightForWidth())
        self.widget_20.setSizePolicy(sizePolicy6)
        self.verticalLayout_13 = QVBoxLayout(self.widget_20)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.widget_22 = QWidget(self.widget_20)
        self.widget_22.setObjectName(u"widget_22")
        sizePolicy7.setHeightForWidth(self.widget_22.sizePolicy().hasHeightForWidth())
        self.widget_22.setSizePolicy(sizePolicy7)
        self.horizontalLayout_13 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.widget_22)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_13.addWidget(self.label_11)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_12)

        self.lineEdit_appID = QLineEdit(self.widget_22)
        self.lineEdit_appID.setObjectName(u"lineEdit_appID")
        sizePolicy8.setHeightForWidth(self.lineEdit_appID.sizePolicy().hasHeightForWidth())
        self.lineEdit_appID.setSizePolicy(sizePolicy8)

        self.horizontalLayout_13.addWidget(self.lineEdit_appID)


        self.verticalLayout_13.addWidget(self.widget_22)

        self.line_12 = QFrame(self.widget_20)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.Shape.HLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_13.addWidget(self.line_12)


        self.gridLayout.addWidget(self.widget_20, 0, 0, 1, 1)


        self.verticalLayout_8.addWidget(self.widget_2)

        self.widget = QWidget(self.page)
        self.widget.setObjectName(u"widget")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(60, 50, 461, 141))

        self.verticalLayout_8.addWidget(self.widget)

        self.stackedWidget_settingsPanel.addWidget(self.page)

        self.horizontalLayout_9.addWidget(self.stackedWidget_settingsPanel)


        self.verticalLayout_9.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy10.setHorizontalStretch(1)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy10)
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 0, 0, 0)
        self.pushButton_exit = QPushButton(self.frame_4)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        sizePolicy8.setHeightForWidth(self.pushButton_exit.sizePolicy().hasHeightForWidth())
        self.pushButton_exit.setSizePolicy(sizePolicy8)
        self.pushButton_exit.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_2.addWidget(self.pushButton_exit)

        self.scrollArea = QScrollArea(self.frame_4)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy11)
        self.scrollArea.setMaximumSize(QSize(16777215, 40))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 514, 36))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.variable_displayGamescope = QLabel(self.scrollAreaWidgetContents_2)
        self.variable_displayGamescope.setObjectName(u"variable_displayGamescope")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.variable_displayGamescope.sizePolicy().hasHeightForWidth())
        self.variable_displayGamescope.setSizePolicy(sizePolicy12)

        self.gridLayout_2.addWidget(self.variable_displayGamescope, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_2.addWidget(self.scrollArea)

        self.pushButton_about = QPushButton(self.frame_4)
        self.pushButton_about.setObjectName(u"pushButton_about")
        sizePolicy8.setHeightForWidth(self.pushButton_about.sizePolicy().hasHeightForWidth())
        self.pushButton_about.setSizePolicy(sizePolicy8)
        self.pushButton_about.setMaximumSize(QSize(16777215, 40))
        self.pushButton_about.setFlat(False)

        self.horizontalLayout_2.addWidget(self.pushButton_about)

        self.pushButton_apply = QPushButton(self.frame_4)
        self.pushButton_apply.setObjectName(u"pushButton_apply")
        sizePolicy8.setHeightForWidth(self.pushButton_apply.sizePolicy().hasHeightForWidth())
        self.pushButton_apply.setSizePolicy(sizePolicy8)
        self.pushButton_apply.setMaximumSize(QSize(16777215, 40))
        self.pushButton_apply.setCheckable(False)
        self.pushButton_apply.setChecked(False)

        self.horizontalLayout_2.addWidget(self.pushButton_apply)


        self.verticalLayout_9.addWidget(self.frame_4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.listWidget_gamesList.currentRowChanged.connect(self.stackedWidget_settingsPanel.setCurrentIndex)

        self.stackedWidget_settingsPanel.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))

        __sortingEnabled = self.listWidget_gamesList.isSortingEnabled()
        self.listWidget_gamesList.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget_gamesList.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"Default Settings", None));
        ___qlistwidgetitem1 = self.listWidget_gamesList.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"TODO: Game-specific settings", None));
        self.listWidget_gamesList.setSortingEnabled(__sortingEnabled)

#if QT_CONFIG(tooltip)
        self.toolButton_addGame.setToolTip(QCoreApplication.translate("MainWindow", u"TODO: adds slot for game-specific settings", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_addGame.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(tooltip)
        self.toolButton_removeGame.setToolTip(QCoreApplication.translate("MainWindow", u"TODO: removes selected game-specific slot", None))
#endif // QT_CONFIG(tooltip)
        self.toolButton_removeGame.setText(QCoreApplication.translate("MainWindow", u"\u2613", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Rendered Width", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Rendered Height", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Refresh Rate (FPS)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Output Width", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Output Height", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Fullscreen", None))
        self.checkBox_fullscreen.setText(QCoreApplication.translate("MainWindow", u"Enable?", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"High Dynamic Range (HDR) Support", None))
        self.checkBox_hdr.setText(QCoreApplication.translate("MainWindow", u"Enable?", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Steam Overlay", None))
        self.checkBox_steam.setText(QCoreApplication.translate("MainWindow", u"Enable?", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"MangoHUD Overlay", None))
        self.checkBox_mango.setText(QCoreApplication.translate("MainWindow", u"Enable?", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Force Fullscreen within Gamescope Window", None))
        self.checkBox_forceInternalFullscreen.setText(QCoreApplication.translate("MainWindow", u"Enable?", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Advanced Settings", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Maximum Scale Factor", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Upscaler Type", None))
        self.comboBox_upscalerType.setItemText(0, QCoreApplication.translate("MainWindow", u"Automatic (Default)", None))
        self.comboBox_upscalerType.setItemText(1, QCoreApplication.translate("MainWindow", u"Integer", None))
        self.comboBox_upscalerType.setItemText(2, QCoreApplication.translate("MainWindow", u"Fit", None))
        self.comboBox_upscalerType.setItemText(3, QCoreApplication.translate("MainWindow", u"Fill", None))
        self.comboBox_upscalerType.setItemText(4, QCoreApplication.translate("MainWindow", u"Stretch", None))

        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Upscaler Filter", None))
        self.comboBox_upscalerFilter.setItemText(0, QCoreApplication.translate("MainWindow", u"Linear (Default)", None))
        self.comboBox_upscalerFilter.setItemText(1, QCoreApplication.translate("MainWindow", u"Nearest", None))
        self.comboBox_upscalerFilter.setItemText(2, QCoreApplication.translate("MainWindow", u"Pixel", None))
        self.comboBox_upscalerFilter.setItemText(3, QCoreApplication.translate("MainWindow", u"AMD FSR 1.0", None))
        self.comboBox_upscalerFilter.setItemText(4, QCoreApplication.translate("MainWindow", u"Nvidia NIS 1.0.3", None))

        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Upscaler Sharpness (minimum of 20 to max of 0)", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Mouse Sensitivity factor", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Adaptive Sync", None))
        self.checkBox_adaptiveSync.setText(QCoreApplication.translate("MainWindow", u"Enable?", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"AppID (Found in game's properties page on Steam)", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"spawn a new instance of the default settings page here, below the AppID", None))
        self.pushButton_exit.setText(QCoreApplication.translate("MainWindow", u"Exit App", None))
        self.variable_displayGamescope.setText(QCoreApplication.translate("MainWindow", u"currentGamescope", None))
        self.pushButton_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.pushButton_apply.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
    # retranslateUi

