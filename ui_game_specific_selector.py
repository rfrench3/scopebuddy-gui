# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'game-specific-selectorIDxBUv.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(590, 548)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_20 = QWidget(Form)
        self.widget_20.setObjectName(u"widget_20")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_20.sizePolicy().hasHeightForWidth())
        self.widget_20.setSizePolicy(sizePolicy)
        self.verticalLayout_13 = QVBoxLayout(self.widget_20)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.widget_22 = QWidget(self.widget_20)
        self.widget_22.setObjectName(u"widget_22")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_22.sizePolicy().hasHeightForWidth())
        self.widget_22.setSizePolicy(sizePolicy1)
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_appID.sizePolicy().hasHeightForWidth())
        self.lineEdit_appID.setSizePolicy(sizePolicy2)

        self.horizontalLayout_13.addWidget(self.lineEdit_appID)


        self.verticalLayout_13.addWidget(self.widget_22)

        self.line_12 = QFrame(self.widget_20)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.Shape.HLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_13.addWidget(self.line_12)


        self.verticalLayout.addWidget(self.widget_20)

        self.scrollArea_settings = QScrollArea(Form)
        self.scrollArea_settings.setObjectName(u"scrollArea_settings")
        self.scrollArea_settings.setFrameShape(QFrame.Shape.Panel)
        self.scrollArea_settings.setFrameShadow(QFrame.Shadow.Sunken)
        self.scrollArea_settings.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 555, 1009))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget1_rW = QWidget(self.scrollAreaWidgetContents)
        self.widget1_rW.setObjectName(u"widget1_rW")
        sizePolicy.setHeightForWidth(self.widget1_rW.sizePolicy().hasHeightForWidth())
        self.widget1_rW.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.widget1_rW)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_10 = QWidget(self.widget1_rW)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy1.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy1)
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
        sizePolicy2.setHeightForWidth(self.lineEdit_rWidth.sizePolicy().hasHeightForWidth())
        self.lineEdit_rWidth.setSizePolicy(sizePolicy2)
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
        sizePolicy.setHeightForWidth(self.widget2_rH.sizePolicy().hasHeightForWidth())
        self.widget2_rH.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(self.widget2_rH)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_11 = QWidget(self.widget2_rH)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy1.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy1)
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
        sizePolicy2.setHeightForWidth(self.lineEdit_rHeight.sizePolicy().hasHeightForWidth())
        self.lineEdit_rHeight.setSizePolicy(sizePolicy2)
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
        sizePolicy.setHeightForWidth(self.widget3_fps.sizePolicy().hasHeightForWidth())
        self.widget3_fps.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.widget3_fps)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_9 = QWidget(self.widget3_fps)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy1.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy1)
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
        sizePolicy2.setHeightForWidth(self.lineEdit_fps.sizePolicy().hasHeightForWidth())
        self.lineEdit_fps.setSizePolicy(sizePolicy2)
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
        sizePolicy.setHeightForWidth(self.widget4_oW.sizePolicy().hasHeightForWidth())
        self.widget4_oW.setSizePolicy(sizePolicy)
        self.verticalLayout_7 = QVBoxLayout(self.widget4_oW)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.widget_15 = QWidget(self.widget4_oW)
        self.widget_15.setObjectName(u"widget_15")
        sizePolicy1.setHeightForWidth(self.widget_15.sizePolicy().hasHeightForWidth())
        self.widget_15.setSizePolicy(sizePolicy1)
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
        sizePolicy2.setHeightForWidth(self.lineEdit_oWidth.sizePolicy().hasHeightForWidth())
        self.lineEdit_oWidth.setSizePolicy(sizePolicy2)
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
        sizePolicy.setHeightForWidth(self.widget5_oH.sizePolicy().hasHeightForWidth())
        self.widget5_oH.setSizePolicy(sizePolicy)
        self.verticalLayout_6 = QVBoxLayout(self.widget5_oH)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_13 = QWidget(self.widget5_oH)
        self.widget_13.setObjectName(u"widget_13")
        sizePolicy1.setHeightForWidth(self.widget_13.sizePolicy().hasHeightForWidth())
        self.widget_13.setSizePolicy(sizePolicy1)
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
        sizePolicy2.setHeightForWidth(self.lineEdit_oHeight.sizePolicy().hasHeightForWidth())
        self.lineEdit_oHeight.setSizePolicy(sizePolicy2)
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
        sizePolicy.setHeightForWidth(self.widget6_fullscreen.sizePolicy().hasHeightForWidth())
        self.widget6_fullscreen.setSizePolicy(sizePolicy)
        self.verticalLayout_10 = QVBoxLayout(self.widget6_fullscreen)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_21 = QWidget(self.widget6_fullscreen)
        self.widget_21.setObjectName(u"widget_21")
        sizePolicy1.setHeightForWidth(self.widget_21.sizePolicy().hasHeightForWidth())
        self.widget_21.setSizePolicy(sizePolicy1)
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

        self.widget_29 = QWidget(self.scrollAreaWidgetContents)
        self.widget_29.setObjectName(u"widget_29")
        sizePolicy.setHeightForWidth(self.widget_29.sizePolicy().hasHeightForWidth())
        self.widget_29.setSizePolicy(sizePolicy)
        self.verticalLayout_23 = QVBoxLayout(self.widget_29)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.widget_31 = QWidget(self.widget_29)
        self.widget_31.setObjectName(u"widget_31")
        sizePolicy1.setHeightForWidth(self.widget_31.sizePolicy().hasHeightForWidth())
        self.widget_31.setSizePolicy(sizePolicy1)
        self.horizontalLayout_23 = QHBoxLayout(self.widget_31)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.widget_31)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_23.addWidget(self.label_21)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_21)

        self.checkBox_borderless = QCheckBox(self.widget_31)
        self.checkBox_borderless.setObjectName(u"checkBox_borderless")
        self.checkBox_borderless.setTristate(False)

        self.horizontalLayout_23.addWidget(self.checkBox_borderless)


        self.verticalLayout_23.addWidget(self.widget_31)

        self.line_22 = QFrame(self.widget_29)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setFrameShape(QFrame.Shape.HLine)
        self.line_22.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_23.addWidget(self.line_22)


        self.verticalLayout_5.addWidget(self.widget_29)

        self.widget7_hdr = QWidget(self.scrollAreaWidgetContents)
        self.widget7_hdr.setObjectName(u"widget7_hdr")
        sizePolicy.setHeightForWidth(self.widget7_hdr.sizePolicy().hasHeightForWidth())
        self.widget7_hdr.setSizePolicy(sizePolicy)
        self.verticalLayout_18 = QVBoxLayout(self.widget7_hdr)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.widget_34 = QWidget(self.widget7_hdr)
        self.widget_34.setObjectName(u"widget_34")
        sizePolicy1.setHeightForWidth(self.widget_34.sizePolicy().hasHeightForWidth())
        self.widget_34.setSizePolicy(sizePolicy1)
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
        sizePolicy.setHeightForWidth(self.widget9_steam.sizePolicy().hasHeightForWidth())
        self.widget9_steam.setSizePolicy(sizePolicy)
        self.verticalLayout_11 = QVBoxLayout(self.widget9_steam)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.widget_23 = QWidget(self.widget9_steam)
        self.widget_23.setObjectName(u"widget_23")
        sizePolicy1.setHeightForWidth(self.widget_23.sizePolicy().hasHeightForWidth())
        self.widget_23.setSizePolicy(sizePolicy1)
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
        sizePolicy.setHeightForWidth(self.widget__10mangohud.sizePolicy().hasHeightForWidth())
        self.widget__10mangohud.setSizePolicy(sizePolicy)
        self.verticalLayout_12 = QVBoxLayout(self.widget__10mangohud)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.widget_25 = QWidget(self.widget__10mangohud)
        self.widget_25.setObjectName(u"widget_25")
        sizePolicy1.setHeightForWidth(self.widget_25.sizePolicy().hasHeightForWidth())
        self.widget_25.setSizePolicy(sizePolicy1)
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
        sizePolicy.setHeightForWidth(self.widget_24.sizePolicy().hasHeightForWidth())
        self.widget_24.setSizePolicy(sizePolicy)
        self.verticalLayout_20 = QVBoxLayout(self.widget_24)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.widget_27 = QWidget(self.widget_24)
        self.widget_27.setObjectName(u"widget_27")
        sizePolicy1.setHeightForWidth(self.widget_27.sizePolicy().hasHeightForWidth())
        self.widget_27.setSizePolicy(sizePolicy1)
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

        self.widget__16_mouseSensitivity = QWidget(self.scrollAreaWidgetContents)
        self.widget__16_mouseSensitivity.setObjectName(u"widget__16_mouseSensitivity")
        sizePolicy.setHeightForWidth(self.widget__16_mouseSensitivity.sizePolicy().hasHeightForWidth())
        self.widget__16_mouseSensitivity.setSizePolicy(sizePolicy)
        self.verticalLayout_21 = QVBoxLayout(self.widget__16_mouseSensitivity)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.widget_39 = QWidget(self.widget__16_mouseSensitivity)
        self.widget_39.setObjectName(u"widget_39")
        sizePolicy1.setHeightForWidth(self.widget_39.sizePolicy().hasHeightForWidth())
        self.widget_39.setSizePolicy(sizePolicy1)
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
        sizePolicy.setHeightForWidth(self.widget__17_.sizePolicy().hasHeightForWidth())
        self.widget__17_.setSizePolicy(sizePolicy)
        self.verticalLayout_22 = QVBoxLayout(self.widget__17_)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.widget_41 = QWidget(self.widget__17_)
        self.widget_41.setObjectName(u"widget_41")
        sizePolicy1.setHeightForWidth(self.widget_41.sizePolicy().hasHeightForWidth())
        self.widget_41.setSizePolicy(sizePolicy1)
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

        self.widget__11_AdvancedSettings = QWidget(self.scrollAreaWidgetContents)
        self.widget__11_AdvancedSettings.setObjectName(u"widget__11_AdvancedSettings")
        sizePolicy.setHeightForWidth(self.widget__11_AdvancedSettings.sizePolicy().hasHeightForWidth())
        self.widget__11_AdvancedSettings.setSizePolicy(sizePolicy)
        self.verticalLayout_16 = QVBoxLayout(self.widget__11_AdvancedSettings)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.widget_30 = QWidget(self.widget__11_AdvancedSettings)
        self.widget_30.setObjectName(u"widget_30")
        sizePolicy1.setHeightForWidth(self.widget_30.sizePolicy().hasHeightForWidth())
        self.widget_30.setSizePolicy(sizePolicy1)
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
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.line_15.sizePolicy().hasHeightForWidth())
        self.line_15.setSizePolicy(sizePolicy3)
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
        sizePolicy.setHeightForWidth(self.widget__12_maxScaleFactor.sizePolicy().hasHeightForWidth())
        self.widget__12_maxScaleFactor.setSizePolicy(sizePolicy)
        self.verticalLayout_14 = QVBoxLayout(self.widget__12_maxScaleFactor)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.widget_26 = QWidget(self.widget__12_maxScaleFactor)
        self.widget_26.setObjectName(u"widget_26")
        sizePolicy1.setHeightForWidth(self.widget_26.sizePolicy().hasHeightForWidth())
        self.widget_26.setSizePolicy(sizePolicy1)
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
        sizePolicy2.setHeightForWidth(self.lineEdit_maxScaleFactor.sizePolicy().hasHeightForWidth())
        self.lineEdit_maxScaleFactor.setSizePolicy(sizePolicy2)
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
        sizePolicy.setHeightForWidth(self.widget__13_upscalerType.sizePolicy().hasHeightForWidth())
        self.widget__13_upscalerType.setSizePolicy(sizePolicy)
        self.verticalLayout_17 = QVBoxLayout(self.widget__13_upscalerType)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.widget_32 = QWidget(self.widget__13_upscalerType)
        self.widget_32.setObjectName(u"widget_32")
        sizePolicy1.setHeightForWidth(self.widget_32.sizePolicy().hasHeightForWidth())
        self.widget_32.setSizePolicy(sizePolicy1)
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
        sizePolicy2.setHeightForWidth(self.comboBox_upscalerType.sizePolicy().hasHeightForWidth())
        self.comboBox_upscalerType.setSizePolicy(sizePolicy2)

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
        sizePolicy.setHeightForWidth(self.widget__14_upscalerFilter.sizePolicy().hasHeightForWidth())
        self.widget__14_upscalerFilter.setSizePolicy(sizePolicy)
        self.verticalLayout_19 = QVBoxLayout(self.widget__14_upscalerFilter)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.widget_36 = QWidget(self.widget__14_upscalerFilter)
        self.widget_36.setObjectName(u"widget_36")
        sizePolicy1.setHeightForWidth(self.widget_36.sizePolicy().hasHeightForWidth())
        self.widget_36.setSizePolicy(sizePolicy1)
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
        sizePolicy.setHeightForWidth(self.widget__15_upscalerSharpness.sizePolicy().hasHeightForWidth())
        self.widget__15_upscalerSharpness.setSizePolicy(sizePolicy)
        self.verticalLayout_15 = QVBoxLayout(self.widget__15_upscalerSharpness)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.widget_28 = QWidget(self.widget__15_upscalerSharpness)
        self.widget_28.setObjectName(u"widget_28")
        sizePolicy1.setHeightForWidth(self.widget_28.sizePolicy().hasHeightForWidth())
        self.widget_28.setSizePolicy(sizePolicy1)
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
        sizePolicy2.setHeightForWidth(self.lineEdit_upscalerSharpness.sizePolicy().hasHeightForWidth())
        self.lineEdit_upscalerSharpness.setSizePolicy(sizePolicy2)
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

        self.scrollArea_settings.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea_settings)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"AppID (Found in game's properties page on Steam)", None))
#if QT_CONFIG(tooltip)
        self.widget1_rW.setToolTip(QCoreApplication.translate("Form", u"Width (measured in pixels) that the game will render at", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("Form", u"Rendered Width", None))
        self.lineEdit_rWidth.setPlaceholderText(QCoreApplication.translate("Form", u"1920", None))
#if QT_CONFIG(tooltip)
        self.widget2_rH.setToolTip(QCoreApplication.translate("Form", u"Height (measured in pixels) that the game will render at", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("Form", u"Rendered Height", None))
        self.lineEdit_rHeight.setPlaceholderText(QCoreApplication.translate("Form", u"1080", None))
#if QT_CONFIG(tooltip)
        self.widget3_fps.setToolTip(QCoreApplication.translate("Form", u"Maximum amount of frames per second (FPS) the game will attempt to render", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("Form", u"Refresh Rate (FPS)", None))
        self.lineEdit_fps.setPlaceholderText(QCoreApplication.translate("Form", u"120", None))
#if QT_CONFIG(tooltip)
        self.widget4_oW.setToolTip(QCoreApplication.translate("Form", u"Width (in pixels) of the window you will see", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("Form", u"Output Width", None))
        self.lineEdit_oWidth.setPlaceholderText(QCoreApplication.translate("Form", u"2560", None))
#if QT_CONFIG(tooltip)
        self.widget5_oH.setToolTip(QCoreApplication.translate("Form", u"Height (in pixels) of the window you will see", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("Form", u"Output Height", None))
        self.lineEdit_oHeight.setPlaceholderText(QCoreApplication.translate("Form", u"1440", None))
#if QT_CONFIG(tooltip)
        self.widget6_fullscreen.setToolTip(QCoreApplication.translate("Form", u"Should the game launch in fullscreen? (Toggle with Windows key + F)", None))
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("Form", u"Fullscreen", None))
        self.checkBox_fullscreen.setText(QCoreApplication.translate("Form", u"Enable?", None))
#if QT_CONFIG(tooltip)
        self.widget_29.setToolTip(QCoreApplication.translate("Form", u"Should the game window have borders when not in fullscreen?", None))
#endif // QT_CONFIG(tooltip)
        self.label_21.setText(QCoreApplication.translate("Form", u"Borderless Window", None))
        self.checkBox_borderless.setText(QCoreApplication.translate("Form", u"Enable?", None))
#if QT_CONFIG(tooltip)
        self.widget7_hdr.setToolTip(QCoreApplication.translate("Form", u"Enables support for HDR features supported by some monitors", None))
#endif // QT_CONFIG(tooltip)
        self.label_16.setText(QCoreApplication.translate("Form", u"High Dynamic Range (HDR) Support", None))
        self.checkBox_hdr.setText(QCoreApplication.translate("Form", u"Enable?", None))
#if QT_CONFIG(tooltip)
        self.widget9_steam.setToolTip(QCoreApplication.translate("Form", u"Enables the Steam Overlay when in-game (by default, Shift + Tab opens this menu)", None))
#endif // QT_CONFIG(tooltip)
        self.label_9.setText(QCoreApplication.translate("Form", u"Steam Overlay", None))
        self.checkBox_steam.setText(QCoreApplication.translate("Form", u"Enable?", None))
#if QT_CONFIG(tooltip)
        self.widget__10mangohud.setToolTip(QCoreApplication.translate("Form", u"Enables the MangoHUD performance Overlay", None))
#endif // QT_CONFIG(tooltip)
        self.label_10.setText(QCoreApplication.translate("Form", u"MangoHUD Overlay", None))
        self.checkBox_mango.setText(QCoreApplication.translate("Form", u"Enable?", None))
#if QT_CONFIG(tooltip)
        self.widget_24.setToolTip(QCoreApplication.translate("Form", u"Should every window launched be forced into fullscreen? (Primarily relevant for games with dedicated launchers)", None))
#endif // QT_CONFIG(tooltip)
        self.label_18.setText(QCoreApplication.translate("Form", u"Force Fullscreen within Gamescope Window", None))
        self.checkBox_forceInternalFullscreen.setText(QCoreApplication.translate("Form", u"Enable?", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Mouse Sensitivity factor", None))
#if QT_CONFIG(tooltip)
        self.widget__17_.setToolTip(QCoreApplication.translate("Form", u"Enables support for Variable Refresh Rate features like Gsync and Freesync", None))
#endif // QT_CONFIG(tooltip)
        self.label_20.setText(QCoreApplication.translate("Form", u"Variable Refresh Rate (Adaptive Sync)", None))
        self.checkBox_adaptiveSync.setText(QCoreApplication.translate("Form", u"Enable?", None))
#if QT_CONFIG(tooltip)
        self.widget__11_AdvancedSettings.setToolTip(QCoreApplication.translate("Form", u"These are settings I believe will not be relevant to most users, so they are separated to minimize confusion.", None))
#endif // QT_CONFIG(tooltip)
        self.label_14.setText(QCoreApplication.translate("Form", u"Advanced Settings", None))
#if QT_CONFIG(tooltip)
        self.widget__12_maxScaleFactor.setToolTip(QCoreApplication.translate("Form", u"Maximum factor for the scaling of the game window (the default of 0 means unlimited).\n"
"For example, 1.0 would allow no scaling and 2.0 allows twice the rendered size.", None))
#endif // QT_CONFIG(tooltip)
        self.label_12.setText(QCoreApplication.translate("Form", u"Maximum Scale Factor", None))
        self.lineEdit_maxScaleFactor.setPlaceholderText(QCoreApplication.translate("Form", u"0 (no strict limit)", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Upscaler Type", None))
        self.comboBox_upscalerType.setItemText(0, QCoreApplication.translate("Form", u"Automatic (Default)", None))
        self.comboBox_upscalerType.setItemText(1, QCoreApplication.translate("Form", u"Integer", None))
        self.comboBox_upscalerType.setItemText(2, QCoreApplication.translate("Form", u"Fit", None))
        self.comboBox_upscalerType.setItemText(3, QCoreApplication.translate("Form", u"Fill", None))
        self.comboBox_upscalerType.setItemText(4, QCoreApplication.translate("Form", u"Stretch", None))

        self.label_17.setText(QCoreApplication.translate("Form", u"Upscaler Filter", None))
        self.comboBox_upscalerFilter.setItemText(0, QCoreApplication.translate("Form", u"Linear (Default)", None))
        self.comboBox_upscalerFilter.setItemText(1, QCoreApplication.translate("Form", u"Nearest", None))
        self.comboBox_upscalerFilter.setItemText(2, QCoreApplication.translate("Form", u"Pixel", None))
        self.comboBox_upscalerFilter.setItemText(3, QCoreApplication.translate("Form", u"AMD FSR 1.0", None))
        self.comboBox_upscalerFilter.setItemText(4, QCoreApplication.translate("Form", u"Nvidia NIS 1.0.3", None))

        self.label_13.setText(QCoreApplication.translate("Form", u"Upscaler Sharpness (minimum of 20 to max of 0)", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_upscalerSharpness.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lineEdit_upscalerSharpness.setPlaceholderText("")
    # retranslateUi

