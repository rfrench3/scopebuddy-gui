#!/usr/bin/env python3

import sys
sys.path.insert(0, "/app/share/scopebuddygui") # flatpak path

#PySide6, Qt Designer UI files
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QLineEdit, QCheckBox, QDoubleSpinBox, QComboBox, QPushButton, QLabel
from PySide6.QtGui import QIntValidator, QIcon
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
  
import os
from gui_functions import * 

# Create the directory for /scopebuddy/scb.conf
config_dir = os.path.join(os.environ.get("XDG_CONFIG_HOME", os.path.expanduser("~/.config")), "scopebuddy")
print(f'config_dir: {config_dir}')
os.makedirs(config_dir, exist_ok=True)
scbpath = os.path.join(config_dir, "scb.conf")
print(f'scbpath: {scbpath}') 

def create_config_file(scbpath) -> bool | None: #create scb.conf if it doesn't exist, return True if successful
    try: #generates new config file with default values
        if os.path.exists(scbpath):
            print(f"Config file already exists at {scbpath}, skipping creation.")
            return True
        else:
            print(f"Creating config file at {scbpath}...")
        with open(scbpath,'w') as file:
            # Create scopebuddy's default file (TODO: must be manually updated if ScopeBuddy changes)
            file.write("# This is the config file that let's you assign defaults for gamescope when using the scopebuddy script\n")
            file.write("# lines starting with # are ignored\n")
            file.write("# Conf files matching the games Steam AppID stored in ~/.conf/scopebuddy/AppID/ will be sourced after\n")
            file.write("# ~/.config/scopebuddy/scb.conf or whichever file you specify with SCB_CONF=someotherfile.conf env var in the launch options.\n")
            file.write("# \n")
            file.write("# Example for always exporting specific environment variables for gamescope\n")
            file.write("#export XKB_DEFAULT_LAYOUT=no\n")
            file.write("#export MANGOHUD_CONFIG=preset=2\n")
            file.write("#\n")
            file.write("# Example for providing default gamescope arguments through scopebuddy if no arguments are given to the scopebuddy script, this does not need to be exported.\n")
            file.write("# To not use this default set of arguments, just launch scb with SCB_NOSCOPE=1 or just add any gamescope argument before the '-- %command%' then this variable will be ignored\n")
            file.write("#SCB_GAMESCOPE_ARGS=\"--mangoapp -f -w 2560 -h 1440 -W 2560 -H 1440 -r 180 --force-grab-cursor --hdr-enabled -e\"\n")
            file.write("#\n")
            file.write("# To auto-detect KDE display width, height, refresh, VRR and HDR states, you can use SCB_AUTO_* {RES|HDR|VRR}\n")
            file.write("# These vars will override any previously set values for -W and -H or append --hdr-enabled and --adaptive-sync\n")
            file.write("# automatically depending on the current settings for your active display, or the display chosen with -O /\n")
            file.write("# --prefer-output flags in gamescsope.\n")
            file.write("#SCB_AUTO_RES=1\n")
            file.write("#SCB_AUTO_HDR=1\n")
            file.write("#SCB_AUTO_VRR=1\n")
            file.write("# To debug scopebuddy output, uncomment the following line. After launching games, the executed cmd will be output to ~/.config/scopebuddy/scopebuddy.log\n")
            file.write("#SCB_DEBUG=1\n")
            file.write("###\n")
            file.write("## FOR ADVANCED USE INSIDE AN APPID CONFIG\n")
            file.write("###\n")
            file.write("# The config files are treated as a bash script by scopebuddy, this means you can use bash to do simple tasks before the game runs\n")
            file.write("# or you can check which mode scopebuddy is running in and apply settings accordingly, below are some handy variables for scripting.\n")
            file.write("# $SCB_NOSCOPE will be set to 1 if we are running in no gamescope mode\n")
            file.write("# $SCB_GAMEMODE will be set to 1 if we are running inside steam gamemode (which means SCB_NOSCOPE will also be set to 1 due to nested gamescope not working in gamemode)\n")
            file.write("# $command will contain everything steam expanded %command% into\n")
        return True
    except OSError as e:
        print(f"Error creating config file: {e}")

create_config_file(scbpath) # creates the config file if it does not exist

class SharedLogic:
    def define_widget(self,Type,name:str):
        return self.window.findChild(Type, name)
    

    


class MainWindowLogic(SharedLogic):
    def __init__(self, window):
        self.window = window

        #Only numbers are valid for these entries, so block non-numbers
        self.accept_only_numbers = [
            "lineEdit_rWidth","lineEdit_oWidth","lineEdit_rHeight",
            "lineEdit_oHeight","lineEdit_fps","lineEdit_maxScaleFactor",
            "lineEdit_upscalerSharpness"]
        for object in self.accept_only_numbers:
            widget = self.window.findChild(QLineEdit, object)
            if widget:
                widget.setValidator(QIntValidator())

        #Define all of the widgets
        #self. = self.define_widget(,"")
        self.rWidth = self.define_widget(QLineEdit,"lineEdit_rWidth")
        self.rHeight = self.define_widget(QLineEdit,"lineEdit_rHeight")
        self.oWidth = self.define_widget(QLineEdit,"lineEdit_oWidth")
        self.oHeight = self.define_widget(QLineEdit,"lineEdit_oHeight")
        self.fps = self.define_widget(QLineEdit,"lineEdit_fps")
        self.maxScale = self.define_widget(QLineEdit,"lineEdit_maxScaleFactor")
        self.upscalerSharpness = self.define_widget(QLineEdit,"lineEdit_upscalerSharpness")
        self.fullscreen = self.define_widget(QCheckBox,"checkBox_fullscreen")
        self.bWindow = self.define_widget(QCheckBox,"checkBox_borderless")
        self.hdr = self.define_widget(QCheckBox,"checkBox_hdr")
        self.steam = self.define_widget(QCheckBox,"checkBox_steam")
        self.mangoHUD = self.define_widget(QCheckBox,"checkBox_mango")
        self.fgCursor = self.define_widget(QCheckBox,"checkBox_forceGrabCursor")
        self.fullscreenInGamescope = self.define_widget(QCheckBox,"checkBox_forceInternalFullscreen")
        self.mouseSensitivity = self.define_widget(QDoubleSpinBox,"doubleSpinBox_mouseSensitivity")
        self.vrr = self.define_widget(QCheckBox,"checkBox_adaptiveSync")
        self.upscalerType = self.define_widget(QComboBox,"comboBox_upscalerType")
        self.upscalerFilter = self.define_widget(QComboBox,"comboBox_upscalerFilter")
        self.unimplemented = self.define_widget(QLineEdit,"lineEdit_unimplementedSettings")
        self.exitApp = self.define_widget(QPushButton,"pushButton_exit")
        self.apply = self.define_widget(QPushButton,"pushButton_apply")
        self.displayGamescope = self.define_widget(QLabel,"variable_displayGamescope")

            
        self.exitApp.clicked.connect(self.handle_exit)
        self.apply.clicked.connect(self.handle_apply)
    
    def handle_exit(self):
        print("Exiting application...")
        QApplication.quit()

    def handle_apply(self):
        print("Apply button clicked...")
        dialog = ApplyWindowLogic(self.window)
        dialog.exec()

    def ensure_valid_args(self) -> tuple:
        #TODO: Before adding more checks, make a general function for checking
        if self.rHeight().text() == '' and self.rWidth.text() != '':
            print("Invalid arguments: -h is empty, but -w is not.")
            return (False,'-w','-h')
        
        if self.oHeight.text() == '' and self.oWidth.text() != '':
            print("Invalid arguments: -H is empty, but -W is not.")
            return (False,'-W','-H')
        
        return (True,) #nothing went wrong        

        

class ApplyWindowLogic(QDialog, SharedLogic):
    def __init__(self, parent=None):
        super().__init__(parent)
        loader = QUiLoader()
        ui_apply = QFile("./src/apply_confirmation.ui")
        ui_apply.open(QFile.ReadOnly)
        loaded = loader.load(ui_apply, self)
        ui_apply.close()
        self.setWindowTitle("Apply Changes?")
        # Set the layout of the dialog to the loaded widget's layout
        if loaded.layout():
            self.setLayout(loaded.layout())
        # Connect the Cancel button to close the dialog
        self.cancel = self.findChild(QPushButton, "pushButton_Cancel")
        if self.cancel:
            self.cancel.clicked.connect(self.close)
        #
        self.apply = self.findChild(QPushButton, "pushButton_Apply")
        if self.apply:
            self.apply.clicked.connect(self.close)



class ApplyErrorWindowLogic(QDialog):
    def __init__(self, window):
        self.window = window




# Logic that loads the main window
app = QApplication([])

loader = QUiLoader()
ui_main = QFile("./src/mainwindow.ui")
ui_main.open(QFile.ReadOnly)
window_main = loader.load(ui_main)
ui_main.close()

logic = MainWindowLogic(window_main)

# Set main window attributes
window_main.setWindowTitle("Scopebuddy GUI")  
window_main.setWindowIcon(QIcon("./src/img/io.github.rfrench3.scopebuddy-gui.svg"))

window_main.show()
app.exec()

'''
class MainWindow(QMainWindow,Mixins): 
    def __init__(self):
        super().__init__()
        if self.read_gamescope_args().strip() != '':
            self.ui.variable_displayGamescope.setText(f'Current Gamescope Config: {self.read_gamescope_args()}') #display the current gamescope args
        else:
            self.ui.variable_displayGamescope.setText(f'No Gamescope arguments active!') #display the current lack of gamescope args
        # Button actions
        self.ui.pushButton_apply.clicked.connect(self.apply_clicked)
        self.ui.pushButton_exit.clicked.connect(self.exit_app)

        self.apply_current_to_ui()

    # ON-CLICK METHODS

    def apply_clicked(self):
        print("Apply button clicked...")
        if not self.ensure_valid_args()[0]:
            dialog = Dialog_ApplyError()
            dialog.exec()
            raise ValueError
        dialog = DialogApply()
        dialog.exec()
        if dialog.answer:
            print('Applying changes...')
            self.apply_global_config()

    def exit_app(self):
        print("Exiting application...")
        sys.exit()

class Dialog_ApplyError(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog_ApplyError()
        self.ui.setupUi(self)
        self.setWindowTitle("Error!")  
        self.ui.pushButton_Ok.clicked.connect(self.close)

class DialogApply(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog_Apply()
        self.ui.setupUi(self)
        self.setWindowTitle("Apply Changes?") 
        self.ui.var_currentConfig.setText(MainWindow.read_gamescope_args(window))
        self.ui.var_newConfig.setText(MainWindow.generate_new_config(window))

        #button actions
        self.ui.pushButton_Cancel.clicked.connect(self.close)
        self.ui.pushButton_Apply.clicked.connect(self.apply_changes)
        self.answer = False #changes will not be applied unless explictly confirmed
        
    
    def apply_changes(self):
        self.answer = True #changes have been explicitly confirmed
        self.close()

app = QApplication([]) # pass the arguments to the QApplication constructor
window = MainWindow()
window.show()
app.exec()
'''