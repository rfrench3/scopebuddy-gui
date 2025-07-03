import sys
import os
sys.path.insert(0, "/app/share/scopebuddygui") # flatpak path

from PySide6.QtWidgets import (
    QLineEdit, QCheckBox, QDoubleSpinBox, QComboBox, QPushButton,
    QStatusBar, QDialogButtonBox, QToolButton, QWidget
    )

from file_manager import ConfigFile

class GamescopeLogic:
    def __init__(self, file:ConfigFile, parent_widget:QWidget) -> None:
            self.parent_logic = None  # Will be set by main.py
            self.file = file  # Store the file path
            
            # Widget mapping for efficient initialization
            self.widget_mapping = {
                # QLineEdit widgets
                'rWidth': ('lineEdit_rWidth', QLineEdit, '-w'),
                'rHeight': ('lineEdit_rHeight', QLineEdit, '-h'),
                'oWidth': ('lineEdit_oWidth', QLineEdit, '-W'),
                'oHeight': ('lineEdit_oHeight', QLineEdit, '-H'),
                'fps': ('lineEdit_fps', QLineEdit, '-r'),
                'maxScale': ('lineEdit_maxScaleFactor', QLineEdit, '-m'),
                'upscalerSharpness': ('lineEdit_upscalerSharpness', QLineEdit, '--sharpness'),
                'unimplemented': ('lineEdit_unimplementedSettings', QLineEdit, '--placeholder-value'),
                
                # QCheckBox widgets
                'fullscreen': ('checkBox_fullscreen', QCheckBox, '-f'),
                'bWindow': ('checkBox_borderless', QCheckBox, '-b'),
                'hdr': ('checkBox_hdr', QCheckBox, '--hdr-enabled'),
                'steam': ('checkBox_steam', QCheckBox, '-e'),
                'mangoHUD': ('checkBox_mango', QCheckBox, '--mangoapp'),
                'fgCursor': ('checkBox_forceGrabCursor', QCheckBox, '--force-grab-cursor'),
                'fullscreenInGamescope': ('checkBox_forceInternalFullscreen', QCheckBox, '--force-windows-fullscreen'),
                'vrr': ('checkBox_adaptiveSync', QCheckBox, '--adaptive-sync'),
                
                # Other widgets
                'mouseSensitivity': ('doubleSpinBox_mouseSensitivity', QDoubleSpinBox, '-s'),
                'upscalerType': ('comboBox_upscalerType', QComboBox, '-S'),
                'upscalerFilter': ('comboBox_upscalerFilter', QComboBox, '-F'),
                'exitApp': ('pushButton_exit', QPushButton, ''),
                'proceed': ('pushButton_continue', QPushButton, ''),
                'statusBar': ('statusBar', QStatusBar, ''),
                'buttonBox': ('buttonBox', QDialogButtonBox, ''),
                'toolButton_renderedResolution': ('toolButton_renderedResolution', QToolButton, ''),
                'toolButton_outputResolution': ('toolButton_outputResolution', QToolButton, ''),
                'toolButton_fps': ('toolButton_fps', QToolButton, ''),
            }
            
            # Initialize all widgets using the mapping TODO: re-implement QIntValidator
            for attr_name, (object_name, widget_class, arg) in self.widget_mapping.items():
                widget = parent_widget.findChild(widget_class, object_name)
                setattr(self, attr_name, widget)

            self.apply_button = self.buttonBox.button(QDialogButtonBox.StandardButton.Apply) # type: ignore
            self.help_button = self.buttonBox.button(QDialogButtonBox.StandardButton.Help) # type: ignore
            self.reset_button = self.buttonBox.button(QDialogButtonBox.StandardButton.Reset) # type: ignore
            self.defaults_button = self.buttonBox.button(QDialogButtonBox.StandardButton.RestoreDefaults) # type: ignore

            # Initialize and connect inputs  (type: ignore comments prevent pyLance false positives)
            #self. = parent_widget.findChild(Q, '')  # type: ignore


            self.apply_button.clicked.connect(self.print_new_config)



            self.load_data(file.print_gamescope_line())

#TODO: this is extremely messy and should probably be redone
    def load_data(self, data: str) -> None:
        """Loads the data from the file into the UI elements."""
        # Split the data string into arguments
        args = data.strip().split()
        arg_map = {}
        skip_next = False

        # Build a map of argument flags to their values (if any)
        for i, arg in enumerate(args):
            if skip_next:
                skip_next = False
                continue
            # If the next argument is not a flag, treat it as a value
            if arg.startswith('-') or arg.startswith('--'):
                if i + 1 < len(args) and not args[i + 1].startswith('-'):
                    arg_map[arg] = args[i + 1]
                    skip_next = True
                else:
                    arg_map[arg] = True  # flag only

        # Set widget values based on the mapping
        for attr_name, (object_name, widget_class, arg) in self.widget_mapping.items():
            widget = getattr(self, attr_name, None)
            if widget is None:
                continue

            if attr_name == "unimplemented":
                # Set unimplemented settings as a string
                widget.setText('')
                continue

            if not arg:
                continue  # Skip widgets without a CLI argument

            if widget_class == QCheckBox:
                widget.setChecked(arg in arg_map)
            elif widget_class == QLineEdit:
                value = arg_map.get(arg, '')
                widget.setText(str(value) if value is not True else '')
            elif widget_class == QComboBox:
                value = arg_map.get(arg, '')
                if value and value is not True:
                    idx = widget.findText(str(value))
                    if idx != -1:
                        widget.setCurrentIndex(idx)
                    else:
                        widget.setCurrentIndex(0)
                else:
                    widget.setCurrentIndex(0)
            elif widget_class == QDoubleSpinBox:
                value = arg_map.get(arg, '')
                try:
                    widget.setValue(float(value))
                except (ValueError, TypeError):
                    widget.setValue(1.0)
        

        

    def print_new_config(self) -> str: #output a new config string based on the user input
        self.config_list = []

        def apply_lineEdit_input(lineEdit, arg):
            if lineEdit.text().isdigit():
                self.config_list.append(f'{arg} {lineEdit.text()} ')                
            
        def apply_combobox_input(comboBox, arg): #appends combobox input to the config list (unless default)
            if comboBox.currentIndex() != 0:
                self.config_list.append(f'{arg} {comboBox.currentText()} ')

        def apply_checkbox_input(checkBox, arg): #appends checkbox input to the config list 
            if checkBox.isChecked():
                self.config_list.append(f'{arg} ')

        def apply_doubleSpinBox_input(doubleSpinBox, arg): #preferred for float values
            if doubleSpinBox.value() != 1.0:
                self.config_list.append(f'{arg} {doubleSpinBox.value()} ')

        def compile_arguments(widget_mapping_items):
            for attr_name, (object_name, widget_class, arg) in widget_mapping_items:
                widget = getattr(self, attr_name, None)  # Get the widget from self
                
                if attr_name == "unimplemented":
                    self.config_list.append(f'{widget.text()} ') # type: ignore
                elif widget_class == QCheckBox:
                    apply_checkbox_input(widget, arg)
                elif widget_class == QLineEdit:
                    apply_lineEdit_input(widget, arg)
                elif widget_class == QComboBox:
                    apply_combobox_input(widget, arg)
                elif widget_class == QDoubleSpinBox:
                    apply_doubleSpinBox_input(widget, arg)

                

        #TODO: input validation for lineEdits is needed
        #TODO: figure out why an additional space is consistently inserted in the middle
        compile_arguments(self.widget_mapping.items())

        generated_config = ''
        for argument in self.config_list:
            generated_config += argument
        
        print(generated_config.strip())

        return generated_config.strip()
    
    