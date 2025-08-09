import sys
import os
sys.path.insert(0, "/app/share/scopebuddygui") # flatpak path

from PySide6.QtWidgets import (
    QLineEdit, QCheckBox, QDoubleSpinBox, QComboBox, QPushButton,
    QStatusBar, QDialogButtonBox, QToolButton, QWidget, QMenu, QMessageBox
    )
from PySide6.QtGui import QAction

from file_manager import ConfigFile
import file_manager as fman

class GamescopeLogic:
    def __init__(self, file:ConfigFile, parent_widget:QWidget) -> None:
            self.parent_logic = None  # Will be set by main.py
            self.file = file  # Store the file path
            self.parent_widget = parent_widget
            
            # Widget mapping for efficient initialization
            self.widget_mapping = {
                # QLineEdit widgets
                'lineEdit_rWidth': (QLineEdit, '-w'),
                'lineEdit_rHeight': (QLineEdit, '-h'),
                'lineEdit_oWidth': (QLineEdit, '-W'),
                'lineEdit_oHeight': (QLineEdit, '-H'),
                'lineEdit_fps': (QLineEdit, '-r'),
                'lineEdit_maxScaleFactor': (QLineEdit, '-m'),
                'lineEdit_upscalerSharpness': (QLineEdit, '--sharpness'),
                
                # QCheckBox widgets
                'checkBox_globalGamescope': (QCheckBox, ''),
                'checkBox_fullscreen': (QCheckBox, '-f'),
                'checkBox_borderless': (QCheckBox, '-b'),
                'checkBox_hdr': (QCheckBox, '--hdr-enabled'),
                'checkBox_steam': (QCheckBox, '-e'),
                'checkBox_mango': (QCheckBox, '--mangoapp'),
                'checkBox_forceGrabCursor': (QCheckBox, '--force-grab-cursor'),
                'checkBox_forceInternalFullscreen': (QCheckBox, '--force-windows-fullscreen'),
                'checkBox_adaptiveSync': (QCheckBox, '--adaptive-sync'),
                
                # Other widgets
                'doubleSpinBox_mouseSensitivity': (QDoubleSpinBox, '-s'),
                'comboBox_upscalerType': (QComboBox, '-S'),
                'comboBox_upscalerFilter': (QComboBox, '-F'),
                'pushButton_exit': (QPushButton, ''),
                'pushButton_continue': (QPushButton, ''),
                'statusBar': (QStatusBar, ''),
                'buttonBox': (QDialogButtonBox, ''),
                'toolButton_renderedResolution': (QToolButton, ''),
                'toolButton_outputResolution': (QToolButton, ''),
                'toolButton_fps': (QToolButton, ''),

                # Non-specified
                'lineEdit_unimplementedSettings': (QLineEdit, '--placeholder-value'),
            }
            
            # Initialize all widgets using the mapping TODO: re-implement QIntValidator
            for object_name, (widget_class, arg) in self.widget_mapping.items():
                widget = parent_widget.findChild(widget_class, object_name)
                setattr(self, object_name, widget)

            self.apply_button = self.buttonBox.button(QDialogButtonBox.StandardButton.Apply) # type: ignore
            self.help_button = self.buttonBox.button(QDialogButtonBox.StandardButton.Help) # type: ignore
            self.reset_button = self.buttonBox.button(QDialogButtonBox.StandardButton.Reset) # type: ignore
            self.defaults_button = self.buttonBox.button(QDialogButtonBox.StandardButton.RestoreDefaults) # type: ignore

            # Set the text of the buttons to be more immediately obvious
            self.reset_button.setText("Clear")
            self.defaults_button.setText("Set to Saved")


            # Initialize and connect inputs  (type: ignore comments prevent pyLance false error flags)
            #self. = parent_widget.findChild(Q, '')  # type: ignore


            self.apply_button.clicked.connect(self.save_data)
            self.help_button.clicked.connect(lambda: os.system("xdg-open https://wiki.archlinux.org/title/Gamescope"))
            self.reset_button.clicked.connect(self.clear_data)
            self.defaults_button.clicked.connect(self.reset_data)

            self.load_data(file.print_gamescope_line())




            # Set up the menus
            self.menu_rendered = QMenu()
            self.action_1080p_r = QAction("Render at 1920x1080 (Best for compatibility)", self.menu_rendered)
            self.action_1440p_r = QAction("Render at 2560x1440", self.menu_rendered)
            self.action_4k_r = QAction("Render at 3840x2160 (4K UHD)", self.menu_rendered)
            self.menu_rendered.addActions([self.action_1080p_r,self.action_1440p_r,self.action_4k_r])
            
            self.menu_output = QMenu()
            self.action_1080p_o = QAction("Output to 1920x1080", self.menu_output)
            self.action_1440p_o = QAction("Output to 2560x1440", self.menu_output)
            self.action_4k_o = QAction("Output to 3840x2160 (4K UHD)", self.menu_output)
            self.menu_output.addActions([self.action_1080p_o,self.action_1440p_o,self.action_4k_o])

            self.menu_fps = QMenu()
            self.action_0 = QAction("Monitor refresh rate (default)", self.menu_fps)
            self.action_30 = QAction("Set 30fps cap (Low)", self.menu_fps)
            self.action_60 = QAction("Set 60fps cap (Medium)", self.menu_fps)
            self.action_120 = QAction("Set 120fps cap (High)", self.menu_fps)
            self.menu_fps.addActions([self.action_0,self.action_30,self.action_60,self.action_120])



            self.toolButton_renderedResolution.setMenu(self.menu_rendered) # type: ignore
            self.toolButton_renderedResolution.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup) # type: ignore
            self.toolButton_renderedResolution.setStyleSheet("QToolButton::menu-indicator { image: none; }") # type: ignore

            self.toolButton_outputResolution.setMenu(self.menu_output) # type: ignore
            self.toolButton_outputResolution.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup) # type: ignore
            self.toolButton_outputResolution.setStyleSheet("QToolButton::menu-indicator { image: none; }") # type: ignore

            self.toolButton_fps.setMenu(self.menu_fps) # type: ignore
            self.toolButton_fps.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup) # type: ignore
            self.toolButton_fps.setStyleSheet("QToolButton::menu-indicator { image: none; }") # type: ignore


            # Connect actions to slots or functions

            self.action_1080p_r.triggered.connect(self.handle_menu_renderedResolution_1)
            self.action_1440p_r.triggered.connect(self.handle_menu_renderedResolution_2)
            self.action_4k_r.triggered.connect(self.handle_menu_renderedResolution_3)

            self.action_1080p_o.triggered.connect(self.handle_menu_outputResolution_1)
            self.action_1440p_o.triggered.connect(self.handle_menu_outputResolution_2)
            self.action_4k_o.triggered.connect(self.handle_menu_outputResolution_3)

            self.action_0.triggered.connect(lambda: self.lineEdit_fps.setText('')) # type: ignore
            self.action_30.triggered.connect(lambda: self.lineEdit_fps.setText('30')) # type: ignore
            self.action_60.triggered.connect(lambda: self.lineEdit_fps.setText('60')) # type: ignore
            self.action_120.triggered.connect(lambda: self.lineEdit_fps.setText('120')) # type: ignore

    def load_data(self, data: str) -> None:
        """Loads the data from the file into the UI elements."""
        # Split the data string into arguments
        args:list[str] = data.strip().split()
        arg_map: dict[str, str | bool] = {}
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

        # Track which arguments have been processed
        processed_args = set()
        
        # Set widget values based on the mapping
        for object_name, (widget_class, arg) in self.widget_mapping.items():
            widget = getattr(self, object_name, None)
            if widget is None:
                continue

            if object_name == "lineEdit_unimplementedSettings":
                continue  # Handle this separately after processing other widgets

            if not arg:
                continue  # Skip widgets without a CLI argument

            if widget_class == QCheckBox:
                widget.setChecked(arg in arg_map)
                if arg in arg_map:
                    processed_args.add(arg)
            elif widget_class == QLineEdit:
                value = arg_map.get(arg, '')
                widget.setText(str(value) if value is not True else '')
                if arg in arg_map:
                    processed_args.add(arg)
            elif widget_class == QComboBox:
                value = arg_map.get(arg, '')
                if value and value is not True:
                    index = widget.findText(str(value))
                    if index != -1:
                        widget.setCurrentIndex(index)
                    else:
                        widget.setCurrentIndex(0)
                else:
                    widget.setCurrentIndex(0)
                if arg in arg_map:
                    processed_args.add(arg)
            elif widget_class == QDoubleSpinBox:
                value = arg_map.get(arg, '')
                try:
                    widget.setValue(float(value))
                except (ValueError, TypeError):
                    widget.setValue(1.0)
                if arg in arg_map:
                    processed_args.add(arg)
        
        # Collect unprocessed arguments for the unimplemented widget
        unimplemented_args = []
        skip_next = False
        for i, arg in enumerate(args):
            if skip_next:
                skip_next = False
                continue
            
            if arg.startswith('-') or arg.startswith('--'):
                if arg not in processed_args:
                    if i + 1 < len(args) and not args[i + 1].startswith('-'):
                        unimplemented_args.append(f"{arg} {args[i + 1]}")
                        skip_next = True
                    else:
                        unimplemented_args.append(arg)
        
        # Set the unimplemented widget with remaining arguments
        unimplemented_widget = getattr(self, 'lineEdit_unimplementedSettings', None)
        if unimplemented_widget:
            unimplemented_widget.setText(' '.join(unimplemented_args))
        
    def save_data(self) -> bool:
        """Does a few checks to ensure certain known incompatibilities are explained to the user,
        then saves to the config file."""

        parent_window = self.parent_widget.window() if self.parent_widget else None

        if self.checkBox_globalGamescope.isChecked(): #type:ignore
            # ensure no gamescope line is present so the global config is not overridden
            self.file.edit_exact_lines(["SCB_GAMESCOPE_ARGS="],["#SCBGUI#SCB_GAMESCOPE_ARGS="])
            fman.load_message_box(
                parent_window,
                "Success!",
                ("New Gamescope settings saved!\n"
                "The Gamescope settings in the global file will now apply to this game!"),
                QMessageBox.Icon.Information,
                QMessageBox.StandardButton.Ok
            )
            return False

        

        new_config = self.print_new_config()

        # Ensure user is warned if they are combining regular mangohud with gamescope
        gamescope_active:bool = False if (
            self.file.check_for_exact_line("SCB_NOSCOPE=1") or
            self.file.check_for_exact_line("export SCB_NOSCOPE=1")
            ) else True
        
        regular_mangohud:bool = True if (
            self.file.check_for_exact_line("export mangohud") or 
            self.file.check_for_exact_line("export MANGOHUD")
            ) else False
        
        # determines whether the file will be saved after all error dialogs
        do_not_save:bool = False

        if gamescope_active and regular_mangohud:
            result = fman.load_message_box(
                parent_window,
                "Warning!",
                ("You have gamescope enabled and are attempting to use regular MangoHUD!\n"
                "You should either disable Gamescope or use the \"MangoHUD Overlay\" checkbox inside of Gamescope!"),
                QMessageBox.Icon.Warning,
                QMessageBox.StandardButton.Ignore | QMessageBox.StandardButton.Cancel
            )
            if result != QMessageBox.StandardButton.Ignore:
                do_not_save = True

        # Gamescope does not allow -w or -W to be set without -h or -H being set as well.
        if (
            ("-w" in new_config and "-h" not in new_config) or
            ("-W" in new_config and "-H" not in new_config)
        ):
            result = fman.load_message_box(
                parent_window,
                "Warning!",
                ("You have specified a width (-w or -W) without a corresponding height (-h or -H)!\n"
                 "Gamescope will not launch unless only height or both are specified."),
                QMessageBox.Icon.Warning,
                QMessageBox.StandardButton.Cancel | QMessageBox.StandardButton.Ignore
            )
            if result != QMessageBox.StandardButton.Ignore:
                do_not_save = True

            

        if not gamescope_active:
            fman.load_message_box(
                parent_window,
                "Notice!",
                (
                    "You are changing the settings for Gamescope, but Gamescope is disabled!\n"
                    "These settings will have no effect unless you go to General Settings and re-enable Gamescope!"
                ),
                QMessageBox.Icon.Information,
                QMessageBox.StandardButton.Ok
            )
            
        if do_not_save:
            return True

        if new_config.strip() != self.file.print_gamescope_line().strip():
            self.file.edit_gamescope_line(new_config)
        fman.load_message_box(
            parent_window,
            "Success!",
            ("New Gamescope settings saved!\n"
            "Your active Gamescope flags are:\n\n"
            f"gamescope {self.print_new_config()} -- %command%\n\n"
            "(you can copy-paste that into Steam to use Gamescope directly!)"),
            QMessageBox.Icon.Information,
            QMessageBox.StandardButton.Ok
        )
        return False
        
    def clear_data(self):
        """Empties all input fields."""
        for object_name, (widget_class, arg) in self.widget_mapping.items():
            widget = getattr(self, object_name, None)
            if arg:
                if widget_class == QCheckBox:
                    widget.setChecked(False) # type: ignore
                elif widget_class == QLineEdit:
                    widget.setText('') # type: ignore
                elif widget_class == QComboBox:
                    widget.setCurrentIndex(0) # type: ignore
                elif widget_class == QDoubleSpinBox:
                    widget.setValue(1.0) # type: ignore
                else:
                    raise RuntimeError # this should never happen


    def reset_data(self) -> None:
        """Empties all input fields. Then, loads data from file into those input fields."""
        self.clear_data()
        self.load_data(self.file.print_gamescope_line())

    def handle_menu_renderedResolution_1(self):
        #print("Set rendered resolution to 1920x1080")
        self.lineEdit_rWidth.setText('1920') # type: ignore
        self.lineEdit_rHeight.setText('1080') # type: ignore
    def handle_menu_renderedResolution_2(self):
        #print("Set rendered resolution to 2560x1440")
        self.lineEdit_rWidth.setText('2560') # type: ignore
        self.lineEdit_rHeight.setText('1440') # type: ignore
    def handle_menu_renderedResolution_3(self):
        #print("Set rendered resolution to 4K UHD")
        self.lineEdit_rWidth.setText('3840') # type: ignore
        self.lineEdit_rHeight.setText('2160') # type: ignore

    def handle_menu_outputResolution_1(self):
        #print("Set output resolution to 1920x1080")
        self.lineEdit_oWidth.setText('1920') # type: ignore
        self.lineEdit_oHeight.setText('1080') # type: ignore
    def handle_menu_outputResolution_2(self):
        #print("Set output resolution to 2560x1440")
        self.lineEdit_oWidth.setText('2560') # type: ignore
        self.lineEdit_oHeight.setText('1440') # type: ignore
    def handle_menu_outputResolution_3(self):
        #print("Set output resolution to 4K UHD")
        self.lineEdit_oWidth.setText('3840') # type: ignore
        self.lineEdit_oHeight.setText('2160') # type: ignore

    def print_new_config(self) -> str: #output a new config string based on the user input
        self.config_list = []

        def apply_lineEdit_input(lineEdit, arg):
            if lineEdit.text().isdigit():
                self.config_list.append(f'{arg} {lineEdit.text()} ')                
            
        def apply_combobox_input(comboBox, arg): #appends combobox input to the config list (unless default)
            if comboBox.currentIndex() != 0:
                self.config_list.append(f'{arg} {comboBox.currentText().lower()} ')

        def apply_checkbox_input(checkBox, arg): #appends checkbox input to the config list 
            if checkBox.isChecked():
                self.config_list.append(f'{arg} ')

        def apply_doubleSpinBox_input(doubleSpinBox, arg): #preferred for float values
            if doubleSpinBox.value() != 1.0:
                self.config_list.append(f'{arg} {doubleSpinBox.value()} ')

        def compile_arguments(widget_mapping_items):
            for object_name, (widget_class, arg) in widget_mapping_items:
                widget = getattr(self, object_name, None)  # Get the widget from self
                
                if object_name == "lineEdit_unimplementedSettings":
                    if widget and widget.text().strip():  # Only add if there's content
                        self.config_list.append(f'{widget.text().strip()} ')
                elif widget_class == QCheckBox:
                    apply_checkbox_input(widget, arg)
                elif widget_class == QLineEdit:
                    apply_lineEdit_input(widget, arg)
                elif widget_class == QComboBox:
                    apply_combobox_input(widget, arg)
                elif widget_class == QDoubleSpinBox:
                    apply_doubleSpinBox_input(widget, arg)

                

        #TODO: input validation for lineEdits is needed
        compile_arguments(self.widget_mapping.items())

        generated_config = ''
        for argument in self.config_list:
            generated_config += argument
        
        print(generated_config.strip())

        return generated_config.strip()

