#!/usr/bin/env python3

'''
This program, scopebuddy GUI, was created by Robert French (rfrench3, TealMango).
It is licensed under the GPLv3.0 exclusively.
'''

'''
If a function returns a bool to indicate success or failure, False means success and True means there was an error.

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
from PySide6.QtWidgets import QApplication, QStackedWidget, QStatusBar, QListWidget, QListWidgetItem, QTabWidget, QLabel, QPushButton, QDialog, QLineEdit

# import custom logic
sys.path.insert(0, "/app/share/scopebuddygui") # flatpak path
import file_manager as fman
from env_var import EnvVarLogic
from gamescope import GamescopeLogic
from general_settings import GeneralSettingsLogic


DATA_DIR = fman.DATA_DIR
APPID_DIR = fman.APPID_DIR
GLOBAL_CONFIG = fman.GLOBAL_CONFIG

selected_config: fman.ConfigFile | None = None


ui_main = fman.ui_main # The design of the welcome page was heavily inspired by the welcome page of KATE. 
ui_general_settings = fman.ui_general_settings
ui_env_vars = fman.ui_env_vars
ui_gamescope = fman.ui_gamescope

# Dialog of welcome page
dialog_new_file = os.path.join(DATA_DIR, "dialog_new_file.ui")


fman.create_directory()

# Ensures the global config file will always exist
initialize = fman.ScopebuddyDirectory()
initialize.create_file('scb.conf','Global Config file.',fman.SCB_DIR)
initialize = None

class ApplicationLogic:
    def __init__(self, window): 

        # Load data for the main window
        self.window = window 
        self.mainFileSelect = self.window.findChild(QStackedWidget,"stackedWidget")
        self.mainFileEdit = self.window.findChild(QTabWidget,"tabWidget")
        self.statusBar = self.window.findChild(QStatusBar, "statusBar")
        self.button_new_config = self.window.findChild(QPushButton, 'button_new_config')
        self.open_folder = self.window.findChild(QPushButton, "open_folder")
        self.file_list = self.window.findChild(QListWidget, 'file_list')
        self.large_logo = self.window.findChild(QLabel, "appIcon")
        
        # Initialize logic references (but don't create widgets yet)
        self.general_settings_logic = None
        self.env_vars_logic = None
        self.gamescope_logic = None
        self.interface_loaded: bool = False # redundancy to ensure ui doesn't load multiple times at once
        
        #TODO: Find a clean way to find and render the svg
        pixmap = icon.pixmap(1024, 1024)
        self.large_logo.setPixmap(pixmap)


        self.button_new_config.clicked.connect(self.new_config_pressed)
        self.open_folder.clicked.connect(lambda: os.system(f"xdg-open {fman.SCB_DIR}"))
        self.file_list.itemClicked.connect(self.list_clicked)

        # Add a permanent label and pushButton to the status bar
        self.status_label = QLabel("File: None")
        self.status_button = QPushButton("Exit Without Saving")
        self.status_button.clicked.connect(self.unload_selected_file)

        self.statusBar.addWidget(self.status_button)  # Left side
        self.statusBar.addPermanentWidget(self.status_label)  # Right side
        

        # ensure everything starts at its default state
        self.mainFileSelect.setCurrentIndex(0)
        self.mainFileEdit.setCurrentIndex(0)
        self.statusBar.hide()

        # Locate game-specific configs
        self.appid_files = fman.ScopebuddyDirectory()

        # Load config files that have been found into the list widget
        appid_dict = self.appid_files.print_appid_dict()
        for filename, displayname in appid_dict.items():
            item = QListWidgetItem(displayname)
            item.setToolTip(f"File: {os.path.basename(filename)}")
            self.file_list.addItem(item)
        
        
    
        
    def unload_selected_file(self) -> None:
        """Unloads the chosen file and interface, then returns the user to the 'Select a File' page."""
        def unload_interface(self) -> None:
            """Fully unloads interface elements."""
                
            # Clear all tabs (this will delete the widgets)
            self.mainFileEdit.clear()
            
            # Reset logic references
            self.general_settings_logic = None
            self.env_vars_logic = None
            self.gamescope_logic = None
            self.interface_loaded = False

        global selected_config
        unload_interface(self)
        selected_config = None
        self.mainFileSelect.setCurrentIndex(0)
        self.statusBar.hide()

    def list_clicked(self) -> None:
        """opens the config file the user clicked."""
        def load_with_selected_file(self,selected_file:fman.ConfigFile) -> None:
            """Loads the file selected by the user, then loads the interface with it."""
            def load_interface(self,file:fman.ConfigFile) -> None:
                """Loads interface elements and passes them the path to the file being edited."""
                # Only load if not already loaded
                if self.interface_loaded:
                    print("PROBLEM! THE UI ATTEMPTED TO LOAD WHILE ALREADY LOADED!")
                    return
                    
                general_settings_widget = fman.load_widget(ui_general_settings)
                env_vars_widget = fman.load_widget(ui_env_vars)
                gamescope_widget = fman.load_widget(ui_gamescope)

                # Initialize the logic for the ui pages
                self.general_settings = GeneralSettingsLogic(file, general_settings_widget)
                self.env_vars_logic = EnvVarLogic(file, env_vars_widget)
                self.gamescope_logic = GamescopeLogic(file, gamescope_widget)
                    
                # Clear existing tabs and add new ones
                self.mainFileEdit.clear()
                self.mainFileEdit.addTab(general_settings_widget, "General Settings")
                self.mainFileEdit.addTab(env_vars_widget, "Environment Variables")
                self.mainFileEdit.addTab(gamescope_widget, "Gamescope")
                
                self.interface_loaded = True
            
            
            global selected_config
            selected_config = selected_file
            load_interface(self, selected_config) # load the interface elements given the selected file
            self.mainFileSelect.setCurrentIndex(1)
            self.statusBar.show()

            print(f"---FILE LOADED---\n{file}\n-----------------")
        item = self.file_list.currentItem()
        
        if item.text() == "Global":
            filepath = GLOBAL_CONFIG
        else:
            filename:str = item.toolTip()[6:]
            filepath:str = os.path.join(fman.APPID_DIR,filename)



        file = fman.ConfigFile(filepath)
        load_with_selected_file(self, file)
        self.status_label.setText(f"File ({file.print_filename()}): {file.print_displayname()}")

    def new_config_pressed(self) -> None:
        """opens a modal that has the user create a new config with a Steam AppID.""" #TODO:TODO: update the link in the modal to my docs, update docs
        dialog: QDialog = fman.load_widget(dialog_new_file) # type: ignore
        result = dialog.exec()
        
        if result == QDialog.DialogCode.Accepted:  # OK button was clicked
            # Extract data from the LineEdit widgets
            file_name_edit = dialog.findChild(QLineEdit, "file_name")
            display_name_edit = dialog.findChild(QLineEdit, "display_name")
            
            if not file_name_edit.text().endswith(".conf"): # type: ignore
                file_name = file_name_edit.text().strip() + ".conf" # type: ignore
            
            display_name = display_name_edit.text().strip() # type: ignore
                
            print(f"File name: {file_name}")
            print(f"Display name: {display_name}")
                
            # Create a new config file in APPID_DIR with the given file name and display name
            if file_name:
                new_file_path = os.path.join(fman.APPID_DIR, file_name)
                if not os.path.exists(new_file_path):
                    # Create the config file using file_manager logic
                    logic = fman.ScopebuddyDirectory()
                    logic.create_file(file_name,display_name)
                    
                    # Add the new file to the list widget
                    item = QListWidgetItem(display_name)
                    item.setToolTip(f"File: {file_name}")
                    self.file_list.addItem(item)
                else:
                    print(f"File {file_name} already exists.")
            else:
                print("File name is empty.")


# Logic that loads the app
app = QApplication([])
icon = fman.icon

window_main = fman.load_widget(ui_main,"Scopebuddy GUI")
logic = ApplicationLogic(window_main)

window_main.show()
app.exec()