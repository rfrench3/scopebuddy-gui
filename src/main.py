#!/usr/bin/env python3

'''
This program, scopebuddy GUI, was created by Robert French (rfrench3, TealMango).
It is licensed under the GPLv3.0 exclusively.
'''

'''
If a function returns a bool to indicate success or failure, False means success and True means there was an error.

Each page gets its own dedicated logic file, every "ui_filename.ui" comes with a "ui_filename.py" for logic. 
Any operation regarding reading/writing a scopebuddy config file is done through the fman.ConfigFile class.

Select a file: Welcome page. Select the config file to load for the rest of the program.

Edit that file: Rest of the pages. They all edit aspects of that chosen file, 
    which could be the default scb.conf or the game-specific confs in AppID.
'''

#TODO: Loading and unloading UI elements doesn't seem to free memory. 
# Not a major problem given how lightweight this app is, but figure out why for future projects.

import sys
import os

# PySide6, Qt Designer UI files
from PySide6.QtWidgets import (
    QApplication, QStackedWidget, QStatusBar, QListWidget,
    QListWidgetItem, QTabWidget, QLabel, QPushButton, QDialog,
    QLineEdit, QMessageBox, QMainWindow, QWidget
    )
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtSvg import QSvgRenderer

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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.logic = None  # type: ApplicationLogic | None
        
        # Load the UI from the .ui file
        self.ui_widget = fman.load_widget(ui_main)
        self.setCentralWidget(self.ui_widget)
        self.setWindowTitle("Scopebuddy GUI")
        self.setWindowIcon(fman.icon)
        
    def closeEvent(self, event):
        """This ensures that attempting to close the window while a file is loaded results in a dialog,
        prompting the user to either save changes, discard them, or not close the app."""
        global selected_config
        if selected_config is not None and self.logic:
            confirmation = self.logic.exit_dialog()
            if confirmation == QMessageBox.StandardButton.Cancel:
                event.ignore()
                return
            elif confirmation == QMessageBox.StandardButton.Apply:
                # Save all data before closing
                stop = self.logic.general_settings_logic.save_data() if self.logic.general_settings_logic else False
                if stop:
                    event.ignore()
                    return
                stop = self.logic.env_vars_logic.save_data() if self.logic.env_vars_logic else False
                if stop:
                    event.ignore()
                    return
                stop = self.logic.gamescope_logic.save_data() if self.logic.gamescope_logic else False
                if stop:
                    event.ignore()
                    return
            # If Apply succeeded or Discard was chosen, allow close
            event.accept()
        else:
            # No file loaded, close normally
            event.accept()

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
        self.large_logo = self.window.findChild(QWidget, "widget_app_icon")
        
        # Initialize logic references (but don't create widgets yet)
        self.general_settings_logic = None
        self.env_vars_logic = None
        self.gamescope_logic = None
        self.interface_loaded: bool = False # redundancy to ensure ui doesn't load multiple times at once
                

        svg_widget = QSvgWidget(fman.svg_path)
        svg_widget.setFixedSize(128, 128)
        layout = self.large_logo.layout()
        layout.addWidget(svg_widget)

    
        
        self.button_new_config.clicked.connect(self.new_config_pressed)
        self.open_folder.clicked.connect(self.open_folder_clicked)
        self.file_list.itemClicked.connect(self.list_clicked)

        # Add a permanent label and pushButton to the status bar
        self.status_label = QLabel("File: None")
        self.status_button = QPushButton("Exit File")
        self.status_button.clicked.connect(self.unload_selected_file)

        self.statusBar.addWidget(self.status_button)  # Left side
        self.statusBar.addPermanentWidget(self.status_label)  # Right side
        

        # ensure everything starts at its default state
        self.mainFileSelect.setCurrentIndex(0)
        self.mainFileEdit.setCurrentIndex(0)
        self.statusBar.hide()

        # Locate game-specific configs
        self.appid_files = fman.ScopebuddyDirectory()

        # load all configs into UI
        self.reload_file_list()
        
    def reload_file_list(self) -> None:
        """Clears all entries from self.file_list, and then reloads them."""
        self.file_list.clear()

        # Load global config file
        item = QListWidgetItem("Global")
        item.setToolTip(f"File: scb.conf")
        self.file_list.addItem(item)

        # Load config files that have been found into the list widget
        appid_dict = self.appid_files.print_appid_dict()
        for filename, displayname in appid_dict.items():
            item = QListWidgetItem(displayname)
            item.setToolTip(f"File: {os.path.basename(filename)}")
            self.file_list.addItem(item)
        
    def open_folder_clicked(self):
        """Shows a popup window with instructions for opening the Scopebuddy folder."""
        msg = QMessageBox(self.window)
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setWindowTitle("Open Scopebuddy Folder")
        msg.setText(
            "To open the Scopebuddy config folder, run this in a terminal:\n\n"
            f"xdg-open {fman.SCB_DIR}\n\n"
            "In a future update, this button will open the folder automatically."
            )
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()
        return

    def exit_dialog(self) -> QMessageBox.StandardButton:
        """When the user attempts to close the window or exit the file,
        this popup ensures they intended to do so. 
        This dialog is heavily inspired by KDE's System Settings."""
        msg = QMessageBox(self.window)
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setWindowTitle("Exit?")
        msg.setText(
        "Are you certain you wish to exit the file?\n"
        "\"Apply\" double-checks that everything is saved."
        )
        msg.setStandardButtons(QMessageBox.StandardButton.Apply | QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.Cancel)
        result = msg.exec()
        return result # type: ignore

    def unload_selected_file(self) -> None:
        """Prompts the user with a dialog window to be certain they wish to exit.
        Unloads the chosen file and interface, then returns the user to the 'Select a File' page.
        The dialog does not occur if the user is on the main menu, the app simply closes."""
        #if self.general_settings_logic:
            # if the file-editing portion of the app is loaded:
        confirmation = self.exit_dialog()
        if confirmation == QMessageBox.StandardButton.Cancel:
            return
        elif confirmation == QMessageBox.StandardButton.Apply:
            # automatically switches the user to the page they chose
            stop = self.general_settings_logic.save_data() #type: ignore
            if stop:
                self.mainFileEdit.setCurrentIndex(0)
                return
            
            stop = self.env_vars_logic.save_data() #type: ignore
            if stop:
                self.mainFileEdit.setCurrentIndex(1)
                return
            
            stop = self.gamescope_logic.save_data() #type: ignore
            if stop:
                self.mainFileEdit.setCurrentIndex(2)
                return
        
        # else: discard was selected or all applies completed, proceed 
            

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

        self.reload_file_list()

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
                self.general_settings_logic = GeneralSettingsLogic(file, general_settings_widget)
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

            

            #print(f"---FILE LOADED---\n{file}\n-----------------")
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
        """opens a modal that has the user create a new config with a Steam AppID.""" 
        dialog: QDialog = fman.load_widget(dialog_new_file) # type: ignore
        result = dialog.exec()
        
        if result == QDialog.DialogCode.Accepted:  # OK button was clicked
            # Extract data from the LineEdit widgets
            file_name_edit = dialog.findChild(QLineEdit, "file_name")
            display_name_edit = dialog.findChild(QLineEdit, "display_name")
            
            if not file_name_edit.text().endswith(".conf"): # type: ignore
                file_name = file_name_edit.text().strip() + ".conf" # type: ignore
            
            display_name = display_name_edit.text().strip() # type: ignore
                
            # Create a new config file in APPID_DIR with the given file name and display name
            if (file_name and
            not fman.invalid_filename(file_name) and
            file_name != ".conf"
            ):
                # the given file name is valid, make sure it does not already exist
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
                    fman.load_message_box(
                        self.window,
                        "Error",
                        (f"File {file_name} already exists.\n"
                        "Hover over the items in the list to see their file names."),
                        QMessageBox.Icon.Warning,
                        QMessageBox.StandardButton.Ok
                    )
            elif fman.invalid_filename(file_name):
                # The box had invalid characters
                fman.load_message_box(
                    self.window,
                    "Error",
                    "File name contains invalid characters.",
                    QMessageBox.Icon.Warning,
                    QMessageBox.StandardButton.Ok
                )
            elif file_name == ".conf":
                # The box was left empty
                fman.load_message_box(
                    self.window,
                    "Error",
                    "File name is empty.",
                    QMessageBox.Icon.Warning,
                    QMessageBox.StandardButton.Ok
                )
            else:
                fman.load_message_box(
                    self.window,
                    "Error",
                    ("File name is invalid for a reason the developer did not account for.\n"
                    "If you see this, please report your file name to the GitHub issue tracker."),
                    QMessageBox.Icon.Warning,
                    QMessageBox.StandardButton.Ok
                )



# Logic that loads the app
app = QApplication([])
icon = fman.icon

window_main = MainWindow()
logic = ApplicationLogic(window_main.ui_widget)
window_main.logic = logic

window_main.show()
app.exec()