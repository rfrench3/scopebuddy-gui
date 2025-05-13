# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowLeBRNE.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QListView, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QToolButton, QVBoxLayout, QWidget)

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
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
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
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy3)
        self.frame_5.setFrameShape(QFrame.Shape.Box)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_5)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.toolButton_addGame = QToolButton(self.frame_5)
        self.toolButton_addGame.setObjectName(u"toolButton_addGame")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.toolButton_addGame.setIcon(icon)

        self.horizontalLayout.addWidget(self.toolButton_addGame)

        self.toolButton_removeGame = QToolButton(self.frame_5)
        self.toolButton_removeGame.setObjectName(u"toolButton_removeGame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
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
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.scrollArea_settings = QScrollArea(self.stackedWidget_gamesDefault)
        self.scrollArea_settings.setObjectName(u"scrollArea_settings")
        self.scrollArea_settings.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollArea_settings.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 575, 610))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_rW = QWidget(self.scrollAreaWidgetContents)
        self.widget_rW.setObjectName(u"widget_rW")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.widget_rW.sizePolicy().hasHeightForWidth())
        self.widget_rW.setSizePolicy(sizePolicy6)
        self.verticalLayout_3 = QVBoxLayout(self.widget_rW)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_10 = QWidget(self.widget_rW)
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
        sizePolicy4.setHeightForWidth(self.lineEdit_rWidth.sizePolicy().hasHeightForWidth())
        self.lineEdit_rWidth.setSizePolicy(sizePolicy4)
        self.lineEdit_rWidth.setMaxLength(4)

        self.horizontalLayout_4.addWidget(self.lineEdit_rWidth)


        self.verticalLayout_3.addWidget(self.widget_10)

        self.line_3 = QFrame(self.widget_rW)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_3)


        self.verticalLayout_5.addWidget(self.widget_rW)

        self.widget_rH = QWidget(self.scrollAreaWidgetContents)
        self.widget_rH.setObjectName(u"widget_rH")
        sizePolicy6.setHeightForWidth(self.widget_rH.sizePolicy().hasHeightForWidth())
        self.widget_rH.setSizePolicy(sizePolicy6)
        self.verticalLayout_4 = QVBoxLayout(self.widget_rH)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_11 = QWidget(self.widget_rH)
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
        sizePolicy4.setHeightForWidth(self.lineEdit_rHeight.sizePolicy().hasHeightForWidth())
        self.lineEdit_rHeight.setSizePolicy(sizePolicy4)
        self.lineEdit_rHeight.setMaxLength(4)

        self.horizontalLayout_5.addWidget(self.lineEdit_rHeight)


        self.verticalLayout_4.addWidget(self.widget_11)

        self.line_4 = QFrame(self.widget_rH)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_4)


        self.verticalLayout_5.addWidget(self.widget_rH)

        self.widget_fps = QWidget(self.scrollAreaWidgetContents)
        self.widget_fps.setObjectName(u"widget_fps")
        sizePolicy6.setHeightForWidth(self.widget_fps.sizePolicy().hasHeightForWidth())
        self.widget_fps.setSizePolicy(sizePolicy6)
        self.verticalLayout_2 = QVBoxLayout(self.widget_fps)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_9 = QWidget(self.widget_fps)
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
        sizePolicy4.setHeightForWidth(self.lineEdit_fps.sizePolicy().hasHeightForWidth())
        self.lineEdit_fps.setSizePolicy(sizePolicy4)
        self.lineEdit_fps.setMaxLength(4)

        self.horizontalLayout_3.addWidget(self.lineEdit_fps)


        self.verticalLayout_2.addWidget(self.widget_9)

        self.line_2 = QFrame(self.widget_fps)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)


        self.verticalLayout_5.addWidget(self.widget_fps)

        self.widget_oW = QWidget(self.scrollAreaWidgetContents)
        self.widget_oW.setObjectName(u"widget_oW")
        sizePolicy6.setHeightForWidth(self.widget_oW.sizePolicy().hasHeightForWidth())
        self.widget_oW.setSizePolicy(sizePolicy6)
        self.verticalLayout_7 = QVBoxLayout(self.widget_oW)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_15 = QWidget(self.widget_oW)
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
        sizePolicy4.setHeightForWidth(self.lineEdit_oWidth.sizePolicy().hasHeightForWidth())
        self.lineEdit_oWidth.setSizePolicy(sizePolicy4)
        self.lineEdit_oWidth.setMaxLength(4)

        self.horizontalLayout_7.addWidget(self.lineEdit_oWidth)


        self.verticalLayout_7.addWidget(self.widget_15)

        self.line_6 = QFrame(self.widget_oW)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_7.addWidget(self.line_6)


        self.verticalLayout_5.addWidget(self.widget_oW)

        self.widget_oH = QWidget(self.scrollAreaWidgetContents)
        self.widget_oH.setObjectName(u"widget_oH")
        sizePolicy6.setHeightForWidth(self.widget_oH.sizePolicy().hasHeightForWidth())
        self.widget_oH.setSizePolicy(sizePolicy6)
        self.verticalLayout_6 = QVBoxLayout(self.widget_oH)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_13 = QWidget(self.widget_oH)
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
        sizePolicy4.setHeightForWidth(self.lineEdit_oHeight.sizePolicy().hasHeightForWidth())
        self.lineEdit_oHeight.setSizePolicy(sizePolicy4)
        self.lineEdit_oHeight.setMaxLength(4)

        self.horizontalLayout_6.addWidget(self.lineEdit_oHeight)


        self.verticalLayout_6.addWidget(self.widget_13)

        self.line_5 = QFrame(self.widget_oH)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line_5)


        self.verticalLayout_5.addWidget(self.widget_oH)

        self.widget_fullscreen = QWidget(self.scrollAreaWidgetContents)
        self.widget_fullscreen.setObjectName(u"widget_fullscreen")
        sizePolicy6.setHeightForWidth(self.widget_fullscreen.sizePolicy().hasHeightForWidth())
        self.widget_fullscreen.setSizePolicy(sizePolicy6)
        self.verticalLayout_10 = QVBoxLayout(self.widget_fullscreen)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_21 = QWidget(self.widget_fullscreen)
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

        self.line_9 = QFrame(self.widget_fullscreen)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_10.addWidget(self.line_9)


        self.verticalLayout_5.addWidget(self.widget_fullscreen)

        self.widget_steam = QWidget(self.scrollAreaWidgetContents)
        self.widget_steam.setObjectName(u"widget_steam")
        sizePolicy6.setHeightForWidth(self.widget_steam.sizePolicy().hasHeightForWidth())
        self.widget_steam.setSizePolicy(sizePolicy6)
        self.verticalLayout_11 = QVBoxLayout(self.widget_steam)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.widget_23 = QWidget(self.widget_steam)
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

        self.line_10 = QFrame(self.widget_steam)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.Shape.HLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_11.addWidget(self.line_10)


        self.verticalLayout_5.addWidget(self.widget_steam)

        self.widget_mangohud = QWidget(self.scrollAreaWidgetContents)
        self.widget_mangohud.setObjectName(u"widget_mangohud")
        sizePolicy6.setHeightForWidth(self.widget_mangohud.sizePolicy().hasHeightForWidth())
        self.widget_mangohud.setSizePolicy(sizePolicy6)
        self.verticalLayout_12 = QVBoxLayout(self.widget_mangohud)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.widget_25 = QWidget(self.widget_mangohud)
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

        self.line_11 = QFrame(self.widget_mangohud)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.Shape.HLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_12.addWidget(self.line_11)


        self.verticalLayout_5.addWidget(self.widget_mangohud)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

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
        sizePolicy4.setHeightForWidth(self.lineEdit_appID.sizePolicy().hasHeightForWidth())
        self.lineEdit_appID.setSizePolicy(sizePolicy4)

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

        self.verticalLayout_8.addWidget(self.widget)

        self.stackedWidget_settingsPanel.addWidget(self.page)

        self.horizontalLayout_9.addWidget(self.stackedWidget_settingsPanel)


        self.verticalLayout_9.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy8.setHorizontalStretch(1)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy8)
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 0, 0, 0)
        self.pushButton_exit = QPushButton(self.frame_4)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        sizePolicy4.setHeightForWidth(self.pushButton_exit.sizePolicy().hasHeightForWidth())
        self.pushButton_exit.setSizePolicy(sizePolicy4)
        self.pushButton_exit.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_2.addWidget(self.pushButton_exit)

        self.scrollArea = QScrollArea(self.frame_4)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy9)
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
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.variable_displayGamescope.sizePolicy().hasHeightForWidth())
        self.variable_displayGamescope.setSizePolicy(sizePolicy10)

        self.gridLayout_2.addWidget(self.variable_displayGamescope, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_2.addWidget(self.scrollArea)

        self.pushButton_about = QPushButton(self.frame_4)
        self.pushButton_about.setObjectName(u"pushButton_about")
        sizePolicy4.setHeightForWidth(self.pushButton_about.sizePolicy().hasHeightForWidth())
        self.pushButton_about.setSizePolicy(sizePolicy4)
        self.pushButton_about.setMaximumSize(QSize(16777215, 40))
        self.pushButton_about.setFlat(False)

        self.horizontalLayout_2.addWidget(self.pushButton_about)

        self.pushButton_apply = QPushButton(self.frame_4)
        self.pushButton_apply.setObjectName(u"pushButton_apply")
        sizePolicy4.setHeightForWidth(self.pushButton_apply.sizePolicy().hasHeightForWidth())
        self.pushButton_apply.setSizePolicy(sizePolicy4)
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
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Steam Overlay", None))
        self.checkBox_steam.setText(QCoreApplication.translate("MainWindow", u"Enable?", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"MangoHUD Overlay", None))
        self.checkBox_mango.setText(QCoreApplication.translate("MainWindow", u"Enable?", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"AppID (Found in game's properties page on Steam)", None))
        self.pushButton_exit.setText(QCoreApplication.translate("MainWindow", u"Exit App", None))
        self.variable_displayGamescope.setText(QCoreApplication.translate("MainWindow", u"currentGamescope", None))
        self.pushButton_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.pushButton_apply.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
    # retranslateUi

