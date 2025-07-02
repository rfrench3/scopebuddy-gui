#!/usr/bin/env python3

'''
This program, scopebuddy GUI, was created by Robert French (rfrench3, TealMango).
It is licensed under the GPLv3.0 exclusively.
'''

'''
Each page gets its own dedicated logic file, every "ui_filename.ui" comes with a "ui_filename.py" for logic.

Select a file: Welcome page. Select the config file to load for the rest of the program.

Edit that file: Rest of the pages. They all edit aspects of that chosen file, 
    which could be the default scb.conf or the game-specific confs in AppID.

any way to get to the "Edit that file" section must select a file. 
Any way to get back to "Select a file" must finish and fully clear operations on the loaded file.
    This should minimize the risk of files being loaded unexpectedly.

In logic terms: Any code that sets the index of main window's QStackedWidget to 1 must LOAD a new file.
                Any code that sets the index of main window's QStackedWidget to 0 must UNLOAD the loaded file.
'''
import sys
#import os

# PySide6, Qt Designer UI files
from PySide6.QtWidgets import QApplication, QStackedWidget, QStatusBar, QTabWidget, QLabel, QPushButton
from PySide6.QtGui import QIcon
#from PySide6.QtUiTools import QUiLoader
#from PySide6.QtCore import QFile
#from PySide6.QtCore import Qt

# import custom logic
sys.path.insert(0, "/app/share/scopebuddygui") # flatpak path
import file_manager as fman
from welcome import WelcomeLogic
from env_var import EnvVarLogic
from gamescope import GamescopeLogic
from apply import ApplyChangesLogic


DATA_DIR = fman.DATA_DIR
APPID_DIR = fman.APPID_DIR
GLOBAL_CONFIG = fman.GLOBAL_CONFIG
selected_config = None # later on, either gets set to GLOBAL_CONFIG or APPID_DIR + filename


ui_main = fman.ui_main
ui_welcome = fman.ui_welcome
ui_env_vars = fman.ui_env_vars
ui_gamescope = fman.ui_gamescope
ui_apply_changes = fman.ui_apply_changes


fman.create_directory()
fman.ensure_file(GLOBAL_CONFIG) # makes sure the scb.conf file exists and works properly


class ApplicationLogic:
    def __init__(self, window): 

        # Load data for the main window
        self.window = window 
        self.mainFileSelect = self.window.findChild(QStackedWidget,"stackedWidget")
        self.mainFileEdit = self.window.findChild(QTabWidget,"tabWidget")
        self.statusBar = self.window.findChild(QStatusBar, "statusBar")


        # Load data for ui pages
        welcome_widget = fman.load_widget(ui_welcome)
        env_vars_widget = fman.load_widget(ui_env_vars)
        gamescope_widget = fman.load_widget(ui_gamescope)
        apply_widget = fman.load_widget(ui_apply_changes)

        # Initialize the logic for the ui pages
        self.welcome_logic = WelcomeLogic(welcome_widget)
        self.env_vars_logic = EnvVarLogic(env_vars_widget)
        self.gamescope_logic = GamescopeLogic(gamescope_widget)
        self.apply_logic = ApplyChangesLogic(apply_widget)

        #TODO: heavily consider simply merging welcome.py/ui into  main.py/ui
        # Gives a path for main window functions to be called from each page 
        # Call main window functions using self.parent_logic.function
        self.welcome_logic.parent_logic = self # type: ignore
        #self.gamescope_logic.parent_logic = self


        self.mainFileSelect.insertWidget(0, welcome_widget)
        self.mainFileSelect.insertWidget(1, self.mainFileEdit)
        self.mainFileEdit.addTab(env_vars_widget, "Environment Variables")
        self.mainFileEdit.addTab(gamescope_widget, "Gamescope")
        self.mainFileEdit.addTab(apply_widget, "Confirmation")


        # Add a permanent label and pushButton to the status bar

        self.status_label = QLabel("Currently loaded file: IMPLEMENT_FILE_NAME_HERE")
        self.status_button = QPushButton("Exit Without Saving")
        self.status_button.clicked.connect(self.unload_selected_file)

        self.statusBar.addPermanentWidget(self.status_label)
        self.statusBar.addPermanentWidget(self.status_button)

        # ensure everything starts at its default state
        self.mainFileSelect.setCurrentIndex(0)
        self.mainFileEdit.setCurrentIndex(0)
        self.statusBar.hide()
        
    def load_selected_file(self,selected_file):
        """Loads the file selected by the user. Then, sets the StackedWidget index to 1 (File Editing mode)."""
        global selected_config
        selected_config = selected_file
        self.env_vars_logic.load_data(selected_config)
        self.gamescope_logic.load_data(selected_config)
        self.apply_logic.load_data(selected_config)
        self.mainFileSelect.setCurrentIndex(1)
        self.statusBar.show()
        
    def unload_selected_file(self):
        """Unloads the chosen file and returns the user to the 'Select a File' page."""
        global selected_config
        #TODO: ensure everything closes properly. Input fields, variables, etc.
        self.reset_interface()
        selected_config = None
        self.mainFileSelect.setCurrentIndex(0)
        self.statusBar.hide()

    def reset_interface(self):
        pass


# Logic that loads the app
app = QApplication([])
icon = QIcon.fromTheme("io.github.rfrench3.scopebuddy-gui")

window_main = fman.load_widget(ui_main,"Scopebuddy GUI")
logic = ApplicationLogic(window_main)

window_main.show()
app.exec()