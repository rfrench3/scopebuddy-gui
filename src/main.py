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
                Any code that sets the index of main window's QStackedWidget to 0 must UNLOAD the loaded
                file and reset the interface to its original state.
'''

#TODO: Loading and unloading UI elements doesn't seem to free memory. 
# Not a major problem given how lightweight this app is, but figure out why for future projects.

import sys
import os

# PySide6, Qt Designer UI files
from PySide6.QtWidgets import QApplication, QStackedWidget, QStatusBar, QListWidget, QTabWidget, QLabel, QPushButton
from PySide6.QtGui import QIcon
#from PySide6.QtUiTools import QUiLoader
#from PySide6.QtCore import QFile
#from PySide6.QtCore import Qt

# import custom logic
sys.path.insert(0, "/app/share/scopebuddygui") # flatpak path
import file_manager as fman
from env_var import EnvVarLogic
from gamescope import GamescopeLogic
from apply import ApplyChangesLogic


DATA_DIR = fman.DATA_DIR
APPID_DIR = fman.APPID_DIR
GLOBAL_CONFIG = fman.GLOBAL_CONFIG

selected_config: fman.ConfigFile | None = None


ui_main = fman.ui_main
ui_env_vars = fman.ui_env_vars
ui_gamescope = fman.ui_gamescope
ui_apply_changes = fman.ui_apply_changes

# Dialog of welcome page
dialog_new_file = os.path.join(DATA_DIR, "dialog_new_file.ui")


fman.create_directory()
fman.ensure_file(GLOBAL_CONFIG) # makes sure the scb.conf file exists and works properly


class ApplicationLogic:
    def __init__(self, window): 

        # Load data for the main window
        self.window = window 
        self.mainFileSelect = self.window.findChild(QStackedWidget,"stackedWidget")
        self.mainFileEdit = self.window.findChild(QTabWidget,"tabWidget")
        self.statusBar = self.window.findChild(QStatusBar, "statusBar")
        self.button_new_config = self.window.findChild(QPushButton, 'button_new_config')
        self.file_list = self.window.findChild(QListWidget, 'file_list')
        self.large_logo = self.window.findChild(QLabel, "appIcon")
        
        # Initialize logic references (but don't create widgets yet)
        self.env_vars_logic = None
        self.gamescope_logic = None
        self.apply_logic = None
        self.interface_loaded: bool = False # redundancy to ensure ui doesn't load multiple times at once
        
        #TODO: Find a clean way to find and render the svg
        pixmap = icon.pixmap(1024, 1024)
        self.large_logo.setPixmap(pixmap)


        self.button_new_config.clicked.connect(self.new_config_pressed)
        self.file_list.itemClicked.connect(self.list_clicked)

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
        
    
        
    def unload_selected_file(self) -> None:
        """Unloads the chosen file and interface, then returns the user to the 'Select a File' page."""
        def unload_interface(self) -> None:
            """Fully unloads interface elements."""
                
            # Clear all tabs (this will delete the widgets)
            self.mainFileEdit.clear()
            
            # Reset logic references
            self.env_vars_logic = None
            self.gamescope_logic = None
            self.apply_logic = None
            self.interface_loaded = False

        global selected_config
        unload_interface(self)
        selected_config = None
        self.mainFileSelect.setCurrentIndex(0)
        self.statusBar.hide()

    def list_clicked(self) -> None:
        """opens the config file the user clicked."""
        def load_selected_file(self,selected_file:fman.ConfigFile) -> None:
            """Loads the file selected by the user into the interface. Then, sets the StackedWidget index to 1 (File Editing mode)."""
            def load_interface(self,file:fman.ConfigFile) -> None:
                """Loads interface elements and passes them the path to the file being edited."""
                # Only load if not already loaded
                if self.interface_loaded:
                    print("PROBLEM! THE UI ATTEMPTED TO LOAD WHILE ALREADY LOADED!")
                    return
                    
                env_vars_widget = fman.load_widget(ui_env_vars)
                gamescope_widget = fman.load_widget(ui_gamescope)
                apply_widget = fman.load_widget(ui_apply_changes)

                # Initialize the logic for the ui pages
                self.env_vars_logic = EnvVarLogic(file, env_vars_widget)
                self.gamescope_logic = GamescopeLogic(file, gamescope_widget)
                self.apply_logic = ApplyChangesLogic(file, apply_widget)
                    
                # Clear existing tabs and add new ones
                self.mainFileEdit.clear()
                self.mainFileEdit.addTab(env_vars_widget, "Environment Variables")
                self.mainFileEdit.addTab(gamescope_widget, "Gamescope")
                self.mainFileEdit.addTab(apply_widget, "Confirmation")
                
                self.interface_loaded = True
            
            
            global selected_config
            selected_config = selected_file
            load_interface(self, selected_config) # load the interface elements given the selected file
            self.mainFileSelect.setCurrentIndex(1)
            self.statusBar.show()

            print(f"---FILE LOADED---\n{file}\n-----------------")
        item = self.file_list.currentItem()
        if item:
            print("List item clicked:", item.text())
        #TODO: Determine path to file
        filepath = GLOBAL_CONFIG #TODO: Make this work with more than the global config
        file = fman.ConfigFile(filepath)
        load_selected_file(self, file)

    def new_config_pressed(self) -> None:
        """opens a modal that has the user create a new config with a Steam AppID."""
        dialog:QDialog = fman.load_widget(dialog_new_file) # type: ignore
        dialog.show()
        dialog.exec()
        #TODO: use the information within the modal to create a new file


# Logic that loads the app
app = QApplication([])
icon = QIcon.fromTheme("io.github.rfrench3.scopebuddy-gui")

window_main = fman.load_widget(ui_main,"Scopebuddy GUI")
logic = ApplicationLogic(window_main)

window_main.show()
app.exec()