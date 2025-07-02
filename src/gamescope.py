import sys
import os
sys.path.insert(0, "/app/share/scopebuddygui") # flatpak path

from PySide6.QtWidgets import (
    QLineEdit, QCheckBox, QDoubleSpinBox, QComboBox, QPushButton,
    QStatusBar, QDialogButtonBox, QToolButton, QMainWindow
    )

from file_manager import ConfigFile

class GamescopeLogic:
    def __init__(self, file:ConfigFile, parent_widget:QMainWindow) -> None:
            self.parent_logic = None  # Will be set by main.py
            self.file = file  # Store the file path
            
            # Widget mapping for efficient initialization
            self.widget_mapping = {
                # QLineEdit widgets
                'rWidth': ('lineEdit_rWidth', QLineEdit),
                'rHeight': ('lineEdit_rHeight', QLineEdit),
                'oWidth': ('lineEdit_oWidth', QLineEdit),
                'oHeight': ('lineEdit_oHeight', QLineEdit),
                'fps': ('lineEdit_fps', QLineEdit),
                'maxScale': ('lineEdit_maxScaleFactor', QLineEdit),
                'upscalerSharpness': ('lineEdit_upscalerSharpness', QLineEdit),
                'unimplemented': ('lineEdit_unimplementedSettings', QLineEdit),
                
                # QCheckBox widgets
                'fullscreen': ('checkBox_fullscreen', QCheckBox),
                'bWindow': ('checkBox_borderless', QCheckBox),
                'hdr': ('checkBox_hdr', QCheckBox),
                'steam': ('checkBox_steam', QCheckBox),
                'mangoHUD': ('checkBox_mango', QCheckBox),
                'fgCursor': ('checkBox_forceGrabCursor', QCheckBox),
                'fullscreenInGamescope': ('checkBox_forceInternalFullscreen', QCheckBox),
                'vrr': ('checkBox_adaptiveSync', QCheckBox),
                
                # Other widgets
                'mouseSensitivity': ('doubleSpinBox_mouseSensitivity', QDoubleSpinBox),
                'upscalerType': ('comboBox_upscalerType', QComboBox),
                'upscalerFilter': ('comboBox_upscalerFilter', QComboBox),
                'exitApp': ('pushButton_exit', QPushButton),
                'proceed': ('pushButton_continue', QPushButton),
                'statusBar': ('statusBar', QStatusBar),
                'buttonBox': ('buttonBox', QDialogButtonBox),
                'toolButton_renderedResolution': ('toolButton_renderedResolution', QToolButton),
                'toolButton_outputResolution': ('toolButton_outputResolution', QToolButton),
                'toolButton_fps': ('toolButton_fps', QToolButton),
            }
            
            # Initialize all widgets using the mapping TODO: re-implement QIntValidator
            for attr_name, (object_name, widget_class) in self.widget_mapping.items():
                widget = parent_widget.findChild(widget_class, object_name)
                setattr(self, attr_name, widget)

            self.apply_button = self.buttonBox.button(QDialogButtonBox.StandardButton.Apply) # type: ignore
            self.help_button = self.buttonBox.button(QDialogButtonBox.StandardButton.Help) # type: ignore
            self.reset_button = self.buttonBox.button(QDialogButtonBox.StandardButton.Reset) # type: ignore
            self.defaults_button = self.buttonBox.button(QDialogButtonBox.StandardButton.RestoreDefaults) # type: ignore

            # Initialize and connect inputs  (type: ignore comments prevent pyLance false positives)
            #self. = parent_widget.findChild(Q, '')  # type: ignore

            self.load_data(file.print_gamescope_line())


    def load_data(self, data:str) -> None:
        """Loads the data from the file into the UI elements."""
        
        pass