# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'apply_confirmationZlTXkM.ui'
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
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog_Apply(object):
    def setupUi(self, Dialog_Apply):
        if not Dialog_Apply.objectName():
            Dialog_Apply.setObjectName(u"Dialog_Apply")
        Dialog_Apply.setWindowModality(Qt.WindowModality.WindowModal)
        Dialog_Apply.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Dialog_Apply)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(Dialog_Apply)
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
        self.verticalLayout_2.setContentsMargins(12, 0, 12, 0)
        self.widget_3 = QWidget(self.frame_2)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)
        self.label.setWordWrap(True)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.line = QFrame(self.frame_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.widget_4 = QWidget(self.frame_2)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.var_currentConfig = QLabel(self.widget_4)
        self.var_currentConfig.setObjectName(u"var_currentConfig")
        sizePolicy1.setHeightForWidth(self.var_currentConfig.sizePolicy().hasHeightForWidth())
        self.var_currentConfig.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.var_currentConfig)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.line_2 = QFrame(self.frame_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.widget_5 = QWidget(self.frame_2)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.widget_5)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.var_newConfig = QLabel(self.widget_5)
        self.var_newConfig.setObjectName(u"var_newConfig")
        sizePolicy1.setHeightForWidth(self.var_newConfig.sizePolicy().hasHeightForWidth())
        self.var_newConfig.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.var_newConfig)


        self.verticalLayout_2.addWidget(self.widget_5)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(Dialog_Apply)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(193, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_Apply = QPushButton(self.frame)
        self.pushButton_Apply.setObjectName(u"pushButton_Apply")

        self.horizontalLayout.addWidget(self.pushButton_Apply)

        self.pushButton_Cancel = QPushButton(self.frame)
        self.pushButton_Cancel.setObjectName(u"pushButton_Cancel")

        self.horizontalLayout.addWidget(self.pushButton_Cancel)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog_Apply)

        QMetaObject.connectSlotsByName(Dialog_Apply)
    # setupUi

    def retranslateUi(self, Dialog_Apply):
        Dialog_Apply.setWindowTitle(QCoreApplication.translate("Dialog_Apply", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog_Apply", u"Are you sure you want to apply the new config?", None))
        self.label_4.setText(QCoreApplication.translate("Dialog_Apply", u"The current one will remain deactived in the config file.", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_Apply", u"Current Configuration: ", None))
        self.var_currentConfig.setText(QCoreApplication.translate("Dialog_Apply", u"VAR_CURRENT_CONFIG", None))
        self.label_3.setText(QCoreApplication.translate("Dialog_Apply", u"New Configuration: ", None))
        self.var_newConfig.setText(QCoreApplication.translate("Dialog_Apply", u"VAR_NEW_CONFIG", None))
        self.pushButton_Apply.setText(QCoreApplication.translate("Dialog_Apply", u"Apply", None))
        self.pushButton_Cancel.setText(QCoreApplication.translate("Dialog_Apply", u"Cancel", None))
    # retranslateUi

