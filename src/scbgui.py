#!/usr/bin/env python3

import sys
sys.path.insert(0, "/app/share/scopebuddygui") # flatpak path
import os
from re import search # for searching for gamescope args in the config file
import shutil

#PySide6, Qt Designer UI files
from PySide6.QtWidgets import QApplication, QStatusBar, QDialog, QDialogButtonBox, QMessageBox, QLineEdit, QCheckBox, QDoubleSpinBox, QComboBox, QPushButton, QLabel, QToolButton, QMenu
from PySide6.QtGui import QIntValidator, QIcon, QAction
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtCore import Qt



# used to update paths based on environment. returns True/False result of os.path.exists
in_flatpak = lambda: os.path.exists("/app/share/scopebuddygui/mainwindow.ui")

# bundle of ui-launching code
def launch_window(ui_path:str,window_title:str="WindowTitle",iconpath:str=""):
    # new_window = launch_window(pathToUI,title,pathToIcon)
    loader = QUiLoader()
    ui = QFile(ui_path)
    ui.open(QFile.ReadOnly)
    variable_name = loader.load(ui)
    ui.close()

    #set window attributes
    variable_name.setWindowTitle(window_title)
    if iconpath:#leave as default if unspecified
        variable_name.setWindowIcon(QIcon(iconpath))
    return variable_name

# set directories for testing and compiled into a flatpak
if in_flatpak():
    #print('IN FLATPAK!')
    uipath_main = "/app/share/scopebuddygui/mainwindow.ui"
    uipath_confirm = "/app/share/scopebuddygui/apply_confirmation.ui"
    iconpath_svg = "/app/share/icons/hicolor/scalable/apps/io.github.rfrench3.scopebuddy-gui.svg"
    iconpath_png = "/app/share/icons/hicolor/128x128/apps/io.github.rfrench3.scopebuddy-gui.png"
    templatepath = "/app/share/scopebuddygui/default_scb.conf"
else:
    #print('NOT IN FLATPAK!')
    uipath_main = "./src/mainwindow.ui"
    uipath_confirm = "./src/apply_confirmation.ui"
    iconpath_svg = "./src/img/io.github.rfrench3.scopebuddy-gui.svg"
    iconpath_png = "./src/img/io.github.rfrench3.scopebuddy-gui.png"
    templatepath = "./src/default_scb.conf"

# Create the directory for /scopebuddy/scb.conf
config_dir = os.path.join(os.environ.get("XDG_CONFIG_HOME", os.path.expanduser("~/.config")), "scopebuddy")
#print(f'config_dir: {config_dir}')
os.makedirs(config_dir, exist_ok=True)
scbpath = os.path.join(config_dir, "scb.conf")
#print(f'scbpath: {scbpath}') 

#print(f"Template exists: {os.path.exists(templatepath)}")
#print(f"Template path: {templatepath}")
#print(f"Target directory writable: {os.access(config_dir, os.W_OK)}")

def ensure_file(scbpath) -> bool | None: #create scb.conf if it doesn't exist, return True if successful
    def ensure_gamescope_line(): 
        # if config file doesn't have the gamescope args line, create one in the best place.
        # this will be where a commented out line is if one is found, or at the end.

        # will be used if the correct line isn't already present
        new_line = f'SCB_GAMESCOPE_ARGS=""\n'

        with open(scbpath, 'r') as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            if line.startswith('SCB_GAMESCOPE_ARGS='):
                match = search(r'SCB_GAMESCOPE_ARGS="([^"]*)"', line)
                if match:
                    #the line is exists and is good
                    return 
                else:
                    #the line will be commented out because it will probably cause errors.
                    #a proper line will be placed after it
                    lines[i:i+1] = [f'#SCBGUI_ERROR_PREVENTATION!#{line}', new_line]
                    with open(scbpath, 'w') as file: 
                        file.writelines(lines)
                    return

        # Assume the gamescope_args line has no breaking issues at this point.

        # check for the default commented out line in the config file.
        # if found, place the new gamescope line right after it
        for i, line in enumerate(lines):
            if line.startswith('#SCB_GAMESCOPE_ARGS'):
                lines[i:i+1] = [line, new_line]
                # Write the modified lines back to the file
                with open(scbpath, 'w') as file:
                    file.writelines(lines)
                return
    
        # no match was found, so create the necessary line at the end of the file
        with open(scbpath, 'a') as file:
            if lines and not lines[-1].endswith('\n'):
                file.write('\n')
            file.write('SCB_GAMESCOPE_ARGS=""\n')
        return
            
    try:
        if os.path.exists(scbpath):
            #print(f"Config file already exists at {scbpath}, ensuring the proper format...")
            ensure_gamescope_line()
            return
        else:
            #print(f"Creating config file at {scbpath} from template...")
            shutil.copyfile(templatepath, scbpath)
            ensure_gamescope_line()
            return
    except Exception as e:
        print(f"Error creating config file: {e}")

ensure_file(scbpath) # makes sure the scb.conf file exists and works properly

class SharedLogic: # for logic used in multiple windows
    def read_gamescope_args(self) -> str: #output gamescope args as string
        with open(scbpath, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith('SCB_GAMESCOPE_ARGS='):
                    match = search(r'SCB_GAMESCOPE_ARGS="([^"]*)"', line)
                    if match:
                        return match.group(1)
                    else:
                        print('Error with config file: Bad SCB_GAMESCOPE_ARGS line detected!') # config file has incorrect format
                        #TODO: comment out the bad line and make a new good line?
            return ''
        
    def display_gamescope_args(self,widget): #for displaying to user, not for logic
        if hasattr(widget, "showMessage"):#TODO: This needs to display more permanently, hovering over a menu makes this text disappear
            if self.read_gamescope_args().strip() != '':
                widget.showMessage(f'Current Gamescope Config: {self.read_gamescope_args()}')
            else:
                widget.showMessage(f'No Gamescope arguments active!')
        else: 
            if self.read_gamescope_args().strip() != '':
                widget.setText(f'Current Gamescope Config: {self.read_gamescope_args()}') #display the current gamescope args
            else:
                widget.setText(f'No Gamescope arguments active!') #display the current lack of gamescope args
    
    def generate_new_config(self) -> str: #output a new config string based on the user input
        self.config_list = []

        def apply_lineEdit_input(lineEdit:int, arg):
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

        def compile_arguments(settings):
            for widget_type, input_widget, arg in settings:
                if widget_type == 'checkbox':
                    apply_checkbox_input(input_widget, arg)
                elif widget_type == 'lineEdit':
                    apply_lineEdit_input(input_widget, arg)
                elif widget_type == 'comboBox':
                    apply_combobox_input(input_widget, arg)
                elif widget_type == 'doubleSpinBox':
                    apply_doubleSpinBox_input(input_widget, arg)
                elif widget_type == 'additionalArgs':
                    self.config_list.append(f'{input_widget.text()} ')
                else:
                    raise NotImplementedError(f"Widget type '{widget_type}' is not implemented.")
                
        # IMPLEMENTED ARGUMENTS
        self.settings = [
            ('checkbox', logic.mangoHUD, '--mangoapp'),
            ('lineEdit', logic.rHeight, '-h'),
            ('lineEdit', logic.rWidth, '-w'),
            ('lineEdit', logic.fps, '-r'),
            ('checkbox', logic.fullscreen, '-f'),
            ('checkbox', logic.bWindow, '-b'),
            ('lineEdit', logic.oHeight, '-H'),
            ('lineEdit', logic.oWidth, '-W'),
            ('checkbox', logic.steam, '-e'),
            ('checkbox', logic.hdr, '--hdr-enabled'),
            ('lineEdit', logic.maxScale, '-m'),
            ('comboBox', logic.upscalerType, '-S'),
            ('comboBox', logic.upscalerFilter, '-F'),
            ('lineEdit', logic.upscalerSharpness, '--sharpness'),
            ('doubleSpinBox', logic.mouseSensitivity, '-s'),
            ('checkbox', logic.vrr, '--adaptive-sync'),
            ('checkbox', logic.fullscreenInGamescope, '--force-windows-fullscreen'),
            ('checkbox', logic.fgCursor, '--force-grab-cursor'),
            ('additionalArgs', logic.unimplemented, '--placeholder-value')
            ]
        
        compile_arguments(self.settings)

        generated_config = ''
        for argument in self.config_list:
            generated_config += argument
        
        #print(f'The generated config file is {generated_config}')
        return generated_config
    
    def apply_current_to_ui(self,clear=False): 
        #checks current config, applies it to the UI. Empties UI if clear=True

        def remove_arg(unimplemented,arg,match):
            # Remove the first instance of the value after the argument (e.g., '-s 1.5')
            try:
                arg_index = unimplemented.index(arg)
                # Ensure the next item exists and matches the value
                if arg_index + 1 < len(unimplemented) and unimplemented[arg_index + 1] == match.group(1):
                    unimplemented.pop(arg_index + 1)
            except ValueError:
                pass
            unimplemented.remove(arg) if arg in unimplemented else None

        def set_lineEdit_input(lineEdit:int, arg,unimplemented,clear):
            if clear:
                lineEdit.setText('')
                return
            args = self.read_gamescope_args()
            match = search(rf'{arg} (\d+)', args)
            if match:
                lineEdit.setText(match.group(1))
                remove_arg(unimplemented,arg,match)
                
            
        def set_combobox_input(comboBox, arg,unimplemented,clear):
            if clear:
                comboBox.setCurrentIndex(0)
                return
            args = self.read_gamescope_args()
            match = search(rf'{arg} ([^\s]+)', args)
            if match:
                value = match.group(1)
                for index in range(comboBox.count()):
                    if comboBox.itemText(index) == value:
                        comboBox.setCurrentIndex(index)
                        remove_arg(unimplemented,arg,match)
                

        def set_checkbox_input(checkBox, arg,unimplemented,clear):
            if clear:
                checkBox.setChecked(False)
                return
            checkBox.setChecked(arg in self.read_gamescope_args()) # set checkbox state based on config
            unimplemented.remove(arg) if arg in unimplemented else None
            

        def set_doubleSpinBox_input(doubleSpinBox, arg,unimplemented,clear): #preferred for float values
            if clear:
                doubleSpinBox.setValue(float(1))
                return
            args = self.read_gamescope_args()
            match = search(rf'{arg} ([\d.]+)', args)
            if match:
                doubleSpinBox.setValue(float(match.group(1)))
                remove_arg(unimplemented,arg,match)

  

        def set_arguments(settings,clear):
            unimplemented = self.read_gamescope_args().split()
            for widget_type, input_widget, arg in settings:
                if widget_type == 'checkbox':
                    set_checkbox_input(input_widget, arg,unimplemented,clear)
                    unimplemented.remove(arg) if arg in unimplemented else None # remove the argument from the unimplemented list
                elif widget_type == 'lineEdit':
                    set_lineEdit_input(input_widget, arg,unimplemented,clear)
                elif widget_type == 'comboBox':
                    set_combobox_input(input_widget, arg,unimplemented,clear)
                elif widget_type == 'doubleSpinBox':
                    set_doubleSpinBox_input(input_widget, arg,unimplemented,clear)
                else:
                    raise NotImplementedError(f"Widget type '{widget_type}' is not implemented.")
                if clear:
                    self.unimplemented.setText('')
                else:
                    self.unimplemented.setText(' '.join(unimplemented)) # set the unimplemented arguments to the line edit
            
        # IMPLEMENTED ARGUMENTS
        self.settings = [
            ('checkbox', self.mangoHUD, '--mangoapp'),
            ('lineEdit', self.rHeight, '-h'),
            ('lineEdit', self.rWidth, '-w'),
            ('lineEdit', self.fps, '-r'),
            ('checkbox', self.fullscreen, '-f'),
            ('checkbox', self.bWindow, '-b'),
            ('lineEdit', self.oHeight, '-H'),
            ('lineEdit', self.oWidth, '-W'),
            ('checkbox', self.steam, '-e'),
            ('checkbox', self.hdr, '--hdr-enabled'),
            ('lineEdit', self.maxScale, '-m'),
            ('comboBox', self.upscalerType, '-S'),
            ('comboBox', self.upscalerFilter, '-F'),
            ('lineEdit', self.upscalerSharpness, '--sharpness'),
            ('doubleSpinBox', self.mouseSensitivity, '-s'),
            ('checkbox', self.vrr, '--adaptive-sync'),
            ('checkbox', self.fullscreenInGamescope, '--force-windows-fullscreen'),
            ('checkbox', self.fgCursor, '--force-grab-cursor'),
            ]
        

        set_arguments(self.settings,clear) # apply the current config to the UI elements

    def apply_global_config(self):
        # set the config
        the_config = self.generate_new_config().strip()

        # Open the config file
        with open(scbpath, 'r') as file:
            lines = file.readlines()

            # Find the line that starts with SCB_GAMESCOPE_ARGS
            for i, line in enumerate(lines):
                if line.startswith('SCB_GAMESCOPE_ARGS'):
                    commented_line = f"# commented out by scopebuddy-gui: {line}"# Comment out the original line
                    new_line = f'SCB_GAMESCOPE_ARGS="{the_config}"\n'# Create the new line
                    lines[i:i+1] = [commented_line, new_line]# Replace with the commented + new line
                    break

            # Write the modified lines back to the file
            with open(scbpath, 'w') as file:
                file.writelines(lines)

class MainWindowLogic(SharedLogic):
    def __init__(self, window): #for reference in other classes, self.widget becomes logic.widget
        self.window = window #logical to use because it is not a subclass of any Qt class

        #Only numbers are valid for these entries, so block non-numbers
        self.accept_only_numbers = [
            "lineEdit_rWidth","lineEdit_oWidth","lineEdit_rHeight",
            "lineEdit_oHeight","lineEdit_fps","lineEdit_maxScaleFactor",
            "lineEdit_upscalerSharpness"]
        for object in self.accept_only_numbers:
            widget = self.window.findChild(QLineEdit, object)
            if widget:
                widget.setValidator(QIntValidator())

        # connect ui elements to code
        #self. = self.window.findChild(,"")
        self.rWidth = self.window.findChild(QLineEdit,"lineEdit_rWidth")
        self.rHeight = self.window.findChild(QLineEdit,"lineEdit_rHeight")
        self.oWidth = self.window.findChild(QLineEdit,"lineEdit_oWidth")
        self.oHeight = self.window.findChild(QLineEdit,"lineEdit_oHeight")
        self.fps = self.window.findChild(QLineEdit,"lineEdit_fps")
        self.maxScale = self.window.findChild(QLineEdit,"lineEdit_maxScaleFactor")
        self.upscalerSharpness = self.window.findChild(QLineEdit,"lineEdit_upscalerSharpness")
        self.fullscreen = self.window.findChild(QCheckBox,"checkBox_fullscreen")
        self.bWindow = self.window.findChild(QCheckBox,"checkBox_borderless")
        self.hdr = self.window.findChild(QCheckBox,"checkBox_hdr")
        self.steam = self.window.findChild(QCheckBox,"checkBox_steam")
        self.mangoHUD = self.window.findChild(QCheckBox,"checkBox_mango")
        self.fgCursor = self.window.findChild(QCheckBox,"checkBox_forceGrabCursor")
        self.fullscreenInGamescope = self.window.findChild(QCheckBox,"checkBox_forceInternalFullscreen")
        self.mouseSensitivity = self.window.findChild(QDoubleSpinBox,"doubleSpinBox_mouseSensitivity")
        self.vrr = self.window.findChild(QCheckBox,"checkBox_adaptiveSync")
        self.upscalerType = self.window.findChild(QComboBox,"comboBox_upscalerType")
        self.upscalerFilter = self.window.findChild(QComboBox,"comboBox_upscalerFilter")
        self.unimplemented = self.window.findChild(QLineEdit,"lineEdit_unimplementedSettings")
        self.exitApp = self.window.findChild(QPushButton,"pushButton_exit")
        self.proceed = self.window.findChild(QPushButton,"pushButton_continue")
        self.statusBar = self.window.findChild(QStatusBar,"statusBar")
        self.buttonBox = self.window.findChild(QDialogButtonBox,"buttonBox")
        self.apply_button = self.buttonBox.button(QDialogButtonBox.Apply)
        self.help_button = self.buttonBox.button(QDialogButtonBox.Help)
        self.reset_button = self.buttonBox.button(QDialogButtonBox.Reset)
        self.defaults_button = self.buttonBox.button(QDialogButtonBox.RestoreDefaults)
        self.toolButton_renderedResolution = self.window.findChild(QToolButton,"toolButton_renderedResolution")
        self.toolButton_outputResolution = self.window.findChild(QToolButton,"toolButton_outputResolution")
        self.toolButton_fps = self.window.findChild(QToolButton,"toolButton_fps")
        # Create a QLabel in the statusBar, aligned to the left and vertically centered
        self.status_label = QLabel()
        self.status_label.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.statusBar.addWidget(self.status_label, 1)

        # Setup UI elements

        self.defaults_button.setText("Clear")
        self.reset_button.setText("Set to saved")
        self.display_gamescope_args(self.status_label)
        self.apply_current_to_ui()

        # Setup menus
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
        self.action_0 = QAction("No fps cap (default)", self.menu_fps)
        self.action_30 = QAction("Set 30fps cap (Low)", self.menu_fps)
        self.action_60 = QAction("Set 60fps cap (Medium)", self.menu_fps)
        self.action_120 = QAction("Set 120fps cap (High)", self.menu_fps)
        self.menu_fps.addActions([self.action_0,self.action_30,self.action_60,self.action_120])



        self.toolButton_renderedResolution.setMenu(self.menu_rendered)
        self.toolButton_renderedResolution.setPopupMode(QToolButton.InstantPopup)
        self.toolButton_renderedResolution.setStyleSheet("QToolButton::menu-indicator { image: none; }")

        self.toolButton_outputResolution.setMenu(self.menu_output)
        self.toolButton_outputResolution.setPopupMode(QToolButton.InstantPopup)
        self.toolButton_outputResolution.setStyleSheet("QToolButton::menu-indicator { image: none; }")

        self.toolButton_fps.setMenu(self.menu_fps)
        self.toolButton_fps.setPopupMode(QToolButton.InstantPopup)
        self.toolButton_fps.setStyleSheet("QToolButton::menu-indicator { image: none; }")


        # Connect actions to slots or functions

        self.action_1080p_r.triggered.connect(self.handle_menu_renderedResolution_1)
        self.action_1440p_r.triggered.connect(self.handle_menu_renderedResolution_2)
        self.action_4k_r.triggered.connect(self.handle_menu_renderedResolution_3)

        self.action_1080p_o.triggered.connect(self.handle_menu_outputResolution_1)
        self.action_1440p_o.triggered.connect(self.handle_menu_outputResolution_2)
        self.action_4k_o.triggered.connect(self.handle_menu_outputResolution_3)

        self.action_0.triggered.connect(lambda: self.fps.setText(''))
        self.action_30.triggered.connect(lambda: self.fps.setText('30'))
        self.action_60.triggered.connect(lambda: self.fps.setText('60'))
        self.action_120.triggered.connect(lambda: self.fps.setText('120'))


        # Connect the buttonBox buttons to actions
        
        self.apply_button.clicked.connect(self.handle_proceed)
        self.help_button.clicked.connect(lambda: os.system('xdg-open "https://rfrench3.github.io/scopebuddy-gui/"'))
        self.reset_button.clicked.connect(self.handle_reset)
        self.defaults_button.clicked.connect(self.handle_defaults)

    def handle_proceed(self):
        #print("Apply button clicked...")

        if not self.ensure_valid_args()[0]:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText(
                "Your set of arguments will not function!\n"
                "You must not:\n"
                "- Set Rendered Width without setting Rendered Height\n"
                "- Set Output Width without setting Output Height"
            )
            msg.setWindowTitle("Error!")
            msg.exec()
        else:
            dialog = ApplyWindowLogic(self.window)
            dialog.exec()

    def handle_reset(self):
        #print('Reset button clicked...')
        self.apply_current_to_ui(clear=True)#cleans out all input fields
        self.apply_current_to_ui()
        pass

    def handle_defaults(self):
        #print('Defaults button clicked...')
        self.apply_current_to_ui(clear=True)
        pass

    def ensure_valid_args(self) -> tuple:
        #TODO: Before adding more checks, make a general function for checking
        if self.rHeight.text() == '' and self.rWidth.text() != '':
            print("Invalid arguments: -h is empty, but -w is not.")
            return (False,'-w','-h')
        
        if self.oHeight.text() == '' and self.oWidth.text() != '':
            print("Invalid arguments: -H is empty, but -W is not.")
            return (False,'-W','-H')
        
        return (True,) #nothing went wrong        

    # Menu handling section

    def handle_menu_renderedResolution_1(self):
        #print("Set rendered resolution to 1920x1080")
        self.rWidth.setText('1920')
        self.rHeight.setText('1080')
    def handle_menu_renderedResolution_2(self):
        #print("Set rendered resolution to 2560x1440")
        self.rWidth.setText('2560')
        self.rHeight.setText('1440')
    def handle_menu_renderedResolution_3(self):
        #print("Set rendered resolution to 4K UHD")
        self.rWidth.setText('3840')
        self.rHeight.setText('2160')

    def handle_menu_outputResolution_1(self):
        #print("Set output resolution to 1920x1080")
        self.oWidth.setText('1920')
        self.oHeight.setText('1080')
    def handle_menu_outputResolution_2(self):
        #print("Set output resolution to 2560x1440")
        self.oWidth.setText('2560')
        self.oHeight.setText('1440')
    def handle_menu_outputResolution_3(self):
        #print("Set output resolution to 4K UHD")
        self.oWidth.setText('3840')
        self.oHeight.setText('2160')

class ApplyWindowLogic(QDialog, SharedLogic):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Establish UI of apply window
        ui_apply = launch_window(uipath_confirm,"Apply Changes?",iconpath_svg)
        if ui_apply.layout():
            self.setLayout(ui_apply.layout())

        # connect ui elements to code
        self.currentConfig = self.findChild(QLabel,"var_currentConfig")
        self.newConfig = self.findChild(QLabel,"var_newConfig")
        self.buttonBox = self.findChild(QDialogButtonBox,"buttonBox")
        self.save_button = self.buttonBox.button(QDialogButtonBox.Save)
        self.abort_button = self.buttonBox.button(QDialogButtonBox.Abort)
        # Add a custom "Edit Config" button to the buttonBox
        self.edit_button = QPushButton("Edit Directly")
        self.buttonBox.addButton(self.edit_button, QDialogButtonBox.ActionRole)
        


        # display changes vs original
        self.currentConfig.setText(self.read_gamescope_args())
        self.newConfig.setText(self.generate_new_config())

        # On-click actions
        self.save_button.clicked.connect(self.apply_clicked)
        self.abort_button.clicked.connect(self.close)
        self.edit_button.clicked.connect(self.open_with_text_editor)


            
    def apply_clicked(self):
        self.apply_global_config()
        self.display_gamescope_args(logic.statusBar)
        self.close()

    def open_with_text_editor(self):
        #TODO: neither xdg-open or the Qt version of it work, or give any sort of error logs...
        # Figure out the issue later and just guide the user there for now.
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(
            "To reach and edit the config file, you must either:\n"
            "- Navigate using the files app into the hidden .config folder, and then into the scopebuddy folder\n"
            "- Enter the following line into a terminal:\n"
            "xdg-open ~/.config/scopebuddy/scb.conf"
        )
        msg.setWindowTitle("Not fully implemented!")
        msg.exec()


# Logic that loads the main window
app = QApplication([])

window_main = launch_window(uipath_main,"Scopebuddy GUI",iconpath_svg)
logic = MainWindowLogic(window_main)

window_main.show()
app.exec()