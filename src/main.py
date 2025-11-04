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


#FIXME: Considerations:
'''
- file saving should have better error detection
- capability for non-english translations should be implemented
- reliance on tooltips and interface text for getting filenames and folder names is a problem
'''

import sys
import os

# PySide6, Qt Designer UI files
from PySide6.QtWidgets import (
    QApplication, QStackedWidget, QStatusBar,
    QTabWidget, QLabel, QPushButton, QDialog,
    QLineEdit, QMessageBox, QMainWindow, QWidget, 
    QVBoxLayout, QTreeWidget, QTreeWidgetItem, 
    QToolButton, QMenu
    )
from PySide6.QtSvgWidgets import QSvgWidget

from PySide6.QtGui import QAction

from PySide6.QtCore import QSignalBlocker, Qt

# import custom logic
sys.path.insert(0, "/app/share/scopebuddygui") # flatpak path
import file_manager as fman
from env_var import EnvVarLogic
from gamescope import GamescopeLogic
from general_settings import GeneralSettingsLogic
from launch_options import LaunchOptionsLogic

import shared_data


DATA_DIR = fman.DATA_DIR
APPID_DIR = fman.APPID_DIR
GLOBAL_CONFIG = fman.GLOBAL_CONFIG

selected_config: fman.ConfigFile | None = None


ui_main = fman.ui_main # The design of the welcome page was heavily inspired by the welcome page of KATE. 
ui_general_settings = fman.ui_general_settings
ui_env_vars = fman.ui_env_vars
ui_gamescope = fman.ui_gamescope
ui_launch_options = fman.ui_launch_options

# Dialog of welcome page
#dialog_new_file = os.path.join(DATA_DIR, "dialog_new_file.ui")
dialog_new_file = os.path.join(DATA_DIR, "new_file_create.ui")
dialog_new_launcher = os.path.join(DATA_DIR, "new_folder_create.ui")
dialog_about = os.path.join(DATA_DIR, "dialog_about.ui")


fman.create_directory()
fman.ScopebuddyDirectory.create_file('scb.conf','Global Config file.',fman.SCB_DIR)

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

        
        if not shared_data.unsaved_changes: 
            event.accept() # there are no unsaved changes
            return 

        global selected_config
        if selected_config is not None and self.logic:

            confirmation = self.logic.confirm_before_proceed()

            # Close unless closing was cancelled
            if confirmation == QMessageBox.StandardButton.Cancel:
                event.ignore()
                return
            
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
        self.about = self.window.findChild(QPushButton, "button_about")
        self.file_tree:QTreeWidget = self.window.findChild(QTreeWidget, 'file_tree')
        self.large_logo = self.window.findChild(QWidget, "widget_app_icon")

        self.file_tree.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.file_tree.customContextMenuRequested.connect(self.show_context_menu)

        # Initialize logic references (but don't create widgets yet)
        self.general_settings_logic = None
        self.env_vars_logic = None
        self.gamescope_logic = None
        self.launch_options_logic = None
        self.interface_loaded: bool = False # redundancy to ensure ui doesn't load multiple times at once
                

        svg_widget = QSvgWidget(fman.svg_path)
        svg_widget.setFixedSize(128, 128)
        layout = self.large_logo.layout()
        layout.addWidget(svg_widget)

        # Track last index and intercept changes when there are unsaved changes
        self._last_tab_index = self.mainFileEdit.currentIndex()
        self.mainFileEdit.currentChanged.connect(self._on_tab_changed)

        
        self.button_new_config.clicked.connect(self.new_config_pressed)
        self.open_folder.clicked.connect(self.open_folder_clicked)
        self.about.clicked.connect(self.about_dialog)
        self.file_tree.itemClicked.connect(self.tree_clicked)

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
        self.reload_file_tree()
        
    def reload_file_tree(self) -> None:
        """Clears all entries from self.file_tree, and then reloads them."""
    
        self.file_tree.clear()

        globalconfig = QTreeWidgetItem()
        globalconfig.setText(0, "Global")
        globalconfig.setToolTip(0, "File: scb.conf")
        self.file_tree.addTopLevelItem(globalconfig)

        directory = fman.ScopebuddyDirectory()
        
        appid_contents = directory.full_directory.get('AppID', {})
        
        launcher_data = []
        
        # for each subfolder of AppID (the launchers), count folder name and number of files to put into a list for sorting
        if appid_contents.get('children'):
            for name, item_data in appid_contents['children'].items():
                configs_list = []
                if item_data['type'] == 'folder' and item_data.get('children'):
                    num_configs = 0
                    
                    for child_name, child_data in item_data['children'].items():
                        if child_data['type'] == 'file':
                            num_configs += 1  
                            configs_list.append((child_data['name'], child_data['displayname']))


                    launcher_data.append((name, num_configs, configs_list))
                elif item_data['type'] == 'folder':
                    launcher_data.append((name, 0, configs_list))
        
        # Sort by number of configs (descending), then by name (ascending)
        launcher_data.sort(key=lambda x: (-x[1], x[0]))
        
        for name, num_configs, filename_displayname in launcher_data:
            launcher = QTreeWidgetItem()
            
            if num_configs == 1:
                launcher.setText(0, f"{name} (1 config)")
            else:
                launcher.setText(0, f"{name} ({num_configs} configs)")

            self.file_tree.addTopLevelItem(launcher)

            # add configs to tree widget
            for filename, displayname in filename_displayname:
                config_item = QTreeWidgetItem(launcher)
                config_item.setText(0, displayname)
                config_item.setToolTip(0, f"File: {filename}")
        
    def _on_tab_changed(self) -> None:
        """Notifies user if they leave the tab with unsaved changes."""

        current_index: int = self.mainFileEdit.currentIndex()

        if not shared_data.unsaved_changes:
            self._last_tab_index = current_index
            return

        self.confirm_before_proceed(tab_changed=True)
        
    def confirm_before_proceed(self, tab_changed:bool=False) -> QMessageBox.StandardButton:  #type:ignore
        """Prompt the user if there are unsaved changes. Revert to the previous
        tab if the user cancels or if saving fails."""
        current_index: int = self.mainFileEdit.currentIndex()
        
        if not shared_data.unsaved_changes:
            self._last_tab_index = current_index
            return QMessageBox.StandardButton.Apply # all changes are applied
        
        # there are unsaved changes
        if tab_changed:
            unsaved_index = self._last_tab_index
        else:
            unsaved_index = current_index

        with QSignalBlocker(self.mainFileEdit):
            self.mainFileEdit.setCurrentIndex(unsaved_index)

        result = fman.load_message_box(
            self.window,
            "Apply Settings",
            "The current page has unsaved changes.",
            QMessageBox.Icon.Warning,
            QMessageBox.StandardButton.Apply | QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.Cancel
            )
        if result == QMessageBox.StandardButton.Cancel:
            return QMessageBox.StandardButton.Cancel
        
        elif result == QMessageBox.StandardButton.Discard:
            shared_data.unsaved_changes = False
            self.mainFileEdit.setCurrentIndex(current_index)
            self._last_tab_index = current_index
            return QMessageBox.StandardButton.Discard
        
        elif result == QMessageBox.StandardButton.Apply:
            match unsaved_index:
                case 0:
                    self.general_settings_logic.save_data() #type:ignore
                case 1:
                    self.env_vars_logic.save_data() #type:ignore
                case 2:
                    self.gamescope_logic.save_data() #type:ignore
                case 3:
                    self.launch_options_logic.save_data() #type:ignore

            shared_data.unsaved_changes = False
            self.mainFileEdit.setCurrentIndex(current_index)
            self._last_tab_index = current_index
            return QMessageBox.StandardButton.Apply

    def open_folder_clicked(self):
        """Shows a popup window with instructions for opening the Scopebuddy folder."""
        fman.load_message_box(
            self.window,
            "Open Scopebuddy Folder",
            (
            "To open the Scopebuddy config folder, run this in a terminal:\n\n"
            f"xdg-open {os.path.join(os.path.expanduser("~/.config"), "scopebuddy")}\n\n" #FIXME: fman.SCB_DIR was causing this to point inside the flatpak sandbox, though everything else works fine
            "This will allow you to directly edit, create, or delete config files without relying on the GUI."
            ),
            QMessageBox.Icon.Information,
            QMessageBox.StandardButton.Ok
        )
        return

    def unload_selected_file(self) -> None:
        """Prompts the user with a dialog window to be certain they wish to exit.
        Unloads the chosen file and interface, then returns the user to the 'Select a File' page.
        The dialog does not occur if the user is on the main menu, the app simply closes."""
        #if self.general_settings_logic:
            # if the file-editing portion of the app is loaded:
        confirmation = self.confirm_before_proceed()
        if confirmation == QMessageBox.StandardButton.Cancel:
            return    

        def unload_interface(self) -> None:
            """Fully unloads interface elements."""
                
            # Clear all tabs (this will delete the widgets)
            self.mainFileEdit.clear()
            
            # Reset logic references
            self.general_settings_logic = None
            self.env_vars_logic = None
            self.gamescope_logic = None
            self.launch_options_logic = None
            self.interface_loaded = False

        global selected_config
        unload_interface(self)
        selected_config = None

        self.reload_file_tree()

        self.mainFileSelect.setCurrentIndex(0)
        self.statusBar.hide()

    def tree_clicked(self) -> None:
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
                launch_options_widget = fman.load_widget(ui_launch_options)

                # Initialize the logic for the ui pages
                self.general_settings_logic = GeneralSettingsLogic(file, general_settings_widget)
                self.env_vars_logic = EnvVarLogic(file, env_vars_widget)
                self.gamescope_logic = GamescopeLogic(file, gamescope_widget)
                self.launch_options_logic = LaunchOptionsLogic(file, launch_options_widget)
                    
                # Clear existing tabs and add new ones
                self.mainFileEdit.clear()
                self.mainFileEdit.addTab(general_settings_widget, "General Settings")
                self.mainFileEdit.addTab(env_vars_widget, "Environment Variables")
                self.mainFileEdit.addTab(gamescope_widget, "Gamescope")
                self.mainFileEdit.addTab(launch_options_widget, "Launch Options")
                
                self.interface_loaded = True
            
            
            global selected_config
            selected_config = selected_file
            load_interface(self, selected_config) # load the interface elements given the selected file
            self.mainFileSelect.setCurrentIndex(1)
            self.statusBar.show()
        
        item = self.file_tree.currentItem()
        
        # Check if this is a top-level item
        parent = item.parent()
        
        if parent is None:
            # Top-level item clicked
            if item.text(0) == "Global":
                filepath = GLOBAL_CONFIG
            else:
                # Non-Global top-level item - expand/collapse it
                item.setExpanded(not item.isExpanded())
                return
        else:
            # Sub-item clicked - get launcher folder from parent

            # launcher' ('# configs), split off the ' (# configs)' part
            launcher_folder = parent.text(0).rsplit(' (', 1)[0]
            filename = item.toolTip(0)[6:]  # Remove "File: " prefix
            filepath = os.path.join(fman.APPID_DIR, launcher_folder, filename)

        file = fman.ConfigFile(filepath)
        load_with_selected_file(self, file)
        self.status_label.setText(f"File ({file.print_filename()}): {file.print_displayname()}")

    def new_config_pressed(self) -> None:
        """opens a modal that has the user create a new config with a Steam AppID.""" 
        dialog = NewFileDialog(self.window)
        result = dialog.exec()

        if result != QDialog.DialogCode.Accepted:  
            return

        if not dialog.data['file_name'].endswith(".conf"):
            dialog.data['file_name'] += ".conf"

        directory = os.path.join(APPID_DIR, dialog.data['launcher'])
        full_path = os.path.join(directory, dialog.data['file_name'])

        if os.path.exists(full_path):
            fman.load_message_box(
                self.window,
                "Error",
                (
                    f"File {dialog.data['file_name']} already exists in this location.\n"
                    "Hover over the items in the list to see their file names."
                ),
                QMessageBox.Icon.Warning,
                QMessageBox.StandardButton.Ok
            )
        else:
            fman.ScopebuddyDirectory.create_file(
                dialog.data['file_name'],
                dialog.data['display_name'],
                directory
            )
            self.reload_file_tree()

    def about_dialog(self) -> None:
        """Opens a dialog with information and links to Scopebuddy and the SCBGUI docs."""
        dialog: QDialog = fman.load_widget(dialog_about, window_title="About") #type:ignore
        image: QWidget = dialog.findChild(QWidget, 'image') #type:ignore
        scb_gh: QPushButton = dialog.findChild(QPushButton, 'scb_gh') #type:ignore
        scb_docs: QPushButton = dialog.findChild(QPushButton, 'scb_docs') #type:ignore
        gui_gh: QPushButton = dialog.findChild(QPushButton, 'gui_gh') #type:ignore
        gui_docs: QPushButton = dialog.findChild(QPushButton, 'gui_docs') #type:ignore

        svg_widget = QSvgWidget(fman.svg_path)
        svg_widget.setFixedSize(128, 128)
        layout: QVBoxLayout = image.layout() #type:ignore
        layout.addWidget(svg_widget)

        scb_gh.clicked.connect(lambda: os.system("xdg-open https://github.com/HikariKnight/ScopeBuddy"))
        scb_docs.clicked.connect(lambda: os.system("xdg-open https://docs.bazzite.gg/Advanced/scopebuddy/"))
        gui_gh.clicked.connect(lambda: os.system("xdg-open https://github.com/rfrench3/scopebuddy-gui"))
        gui_docs.clicked.connect(lambda: os.system("xdg-open https://rfrench3.github.io/scopebuddy-gui/"))

        dialog.exec()

    def show_context_menu(self, position) -> None:

        item = self.file_tree.itemAt(position)
        if not item:
            return
        
        menu = QMenu()

        # Check if top-level item or child
        parent = item.parent()
        
        if parent is None:
            # Top-level item (Global or launcher folder)
            if item.text(0) == "Global":
                open_action = QAction("Open", self.window)
                open_action.triggered.connect(lambda: self.tree_clicked())
                delete_action = QAction("Restore Default", self.window)
                delete_action.triggered.connect(self.remake_global)
                menu.addAction(open_action)
                menu.addAction(delete_action)
            else:
                # Launcher folder
                add_config = QAction("Add Config", self.window)
                # run new_config_pressed with the launcher argument passed
                add_config.triggered.connect(lambda: self.new_config_pressed())
                menu.addAction(add_config)
                
                delete_folder = QAction("Delete Launcher", self.window)
                delete_folder.triggered.connect(lambda: self.delete_item(item, 'folder'))
                menu.addAction(delete_folder)
        else:
            # Config file item
            open_action = QAction("Open", self.window)
            open_action.triggered.connect(lambda: self.tree_clicked())
            menu.addAction(open_action)
            
            delete_action = QAction("Delete", self.window)
            delete_action.triggered.connect(lambda: self.delete_item(item, 'file'))
            menu.addAction(delete_action)
        
        menu.exec(self.file_tree.viewport().mapToGlobal(position))
    
    def delete_item(self, item, type):
        """After an "Are you sure" dialog, pass the file/folder to fman for deletion."""

        if item.text(0).rsplit(' (', 1)[0] == 'steam':
            fman.load_message_box(
            self.window,
            "Deletion Not Allowed",
            "The Steam folder is present by\n"
            "default and cannot be deleted.",
            QMessageBox.Icon.Warning,
            QMessageBox.StandardButton.Ok
            )
            return


        if fman.load_message_box(
            self.window,
            "Confirm Deletion",
            f"Are you certain you wish to delete this {type}?\nThis action cannot be undone.",
            QMessageBox.Icon.Question,
            QMessageBox.StandardButton.Apply | QMessageBox.StandardButton.Abort
            ) != QMessageBox.StandardButton.Apply:
            return 

        if type == 'file':
            launcher_folder = item.parent().text(0).rsplit(' (', 1)[0]
            filename = item.toolTip(0)[6:]
            path = os.path.join(fman.APPID_DIR, launcher_folder, filename)
            fman.ScopebuddyDirectory.delete_file(path)
        elif type == 'folder':
            launcher_folder = item.text(0).rsplit(' (', 1)[0]
            path = os.path.join(fman.APPID_DIR, launcher_folder)
            fman.ScopebuddyDirectory.delete_folder(path)
        else:
            raise ValueError
        
        self.reload_file_tree()
    
    def remake_global(self):
        """After an "Are you sure" dialog, have fman reset the global file."""

        if fman.load_message_box(
            self.window,
            "Confirm Deletion",
            "Are you certain you wish to restore the global config\n" 
            "to default settings? This action cannot be undone.",
            QMessageBox.Icon.Question,
            QMessageBox.StandardButton.Apply | QMessageBox.StandardButton.Abort
            ) != QMessageBox.StandardButton.Apply:
            return 
        
        fman.ScopebuddyDirectory.regenerate_global()

#FIXME: pressing ESC inside the dialog results in a blank window
class NewFileDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.ui_widget = fman.load_widget(dialog_new_file)

        self.data = {
            'launcher': '',
            'file_name': '',
            'display_name': ''
        }
        
        # Create a new layout for the dialog and add the widget to it
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.ui_widget)
        
        self.setWindowTitle("Create New Config")
        self.setWindowIcon(fman.icon)

        self.previous: QPushButton = self.ui_widget.findChild(QPushButton, 'previous')  # type: ignore
        self.next: QPushButton = self.ui_widget.findChild(QPushButton, 'next')  # type: ignore
        self.stack: QStackedWidget = self.ui_widget.findChild(QStackedWidget, 'stackedWidget')  # type: ignore
        self.STACK_FINAL: int = 1
        self.launchers: QTreeWidget = self.ui_widget.findChild(QTreeWidget, 'game_launchers')  # type: ignore
        self.launcher_label: QLabel = self.ui_widget.findChild(QLabel, 'launcher') # type: ignore
        self.filename: QLineEdit = self.ui_widget.findChild(QLineEdit, 'file_name') # type: ignore
        self.displayname: QLineEdit = self.ui_widget.findChild(QLineEdit, 'display_name') # type: ignore
        self.save: QPushButton = self.ui_widget.findChild(QPushButton, 'save')  # type: ignore
        self.discard: QPushButton = self.ui_widget.findChild(QPushButton, 'discard')  # type: ignore
        self.add_folder: QToolButton = self.ui_widget.findChild(QToolButton, 'add_folder')  # type: ignore
        self.appid_link: QToolButton = self.ui_widget.findChild(QToolButton, 'appid_link')  # type: ignore

        self.previous.clicked.connect(self.last_page)
        self.next.clicked.connect(self.next_page)
        self.launchers.itemClicked.connect(self.set_launcher)
        self.filename.textChanged.connect(self.filename_changed)
        self.displayname.textChanged.connect(self.displayname_changed)
        self.discard.clicked.connect(self.close)
        self.save.clicked.connect(self.accept)
        self.add_folder.clicked.connect(self.new_launcher)
        self.appid_link.clicked.connect(lambda: os.system("xdg-open https://rfrench3.github.io/scopebuddy-gui/#appid"))

        self.reload_launcher_widget()

    def last_page(self):
        new = self.stack.currentIndex() - 1
        self.stack.setCurrentIndex(new)

        if new == 0:
            self.previous.setEnabled(False)
        self.next.setEnabled(True)

    def next_page(self):
        new = self.stack.currentIndex() + 1
        self.stack.setCurrentIndex(new)

        if new == self.STACK_FINAL:
            self.next.setEnabled(False)
        self.previous.setEnabled(True)

    ### Launchers Page ###

    def set_launcher(self):            
        self.data['launcher'] = self.launchers.currentItem().text(0)

        self.launcher_label.setText(self.data['launcher'])
        self.update_save_button()
        self.next_page()

    def reload_launcher_widget(self):
        self.launchers.clear()

        directory = fman.ScopebuddyDirectory()
        
        appid_contents = directory.full_directory.get('AppID', {})
        
        launcher_data = []
        
        # for each subfolder of AppID (the launchers), count folder name and number of files to put into a list for sorting
        if appid_contents.get('children'):
            for name, item_data in appid_contents['children'].items():
                if item_data['type'] == 'folder' and item_data.get('children'):
                    num_configs = 0
                    for child_name, child_data in item_data['children'].items():
                        if child_data['type'] == 'file':
                            num_configs += 1  

                    launcher_data.append((name, num_configs))
                elif item_data['type'] == 'folder':
                    launcher_data.append((name, 0))
        
        # Sort by number of configs (descending), then by name (ascending)
        launcher_data.sort(key=lambda x: (-x[1], x[0]))
        
        for name, num_configs in launcher_data:
            launcher = QTreeWidgetItem()
            launcher.setText(0, name)
            
            if num_configs == 1:
                launcher.setText(1, "(1 config)")
            else:
                launcher.setText(1, f"({num_configs} configs)")

            self.launchers.addTopLevelItem(launcher)
                    
    def new_launcher(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Create New Launcher")
        dialog.setWindowIcon(fman.icon)
        
        layout = QVBoxLayout(dialog)
        
        label = QLabel("Enter launcher folder name:")
        layout.addWidget(label)
        
        line_edit = QLineEdit()
        layout.addWidget(line_edit)
        
        button_box = QWidget()
        button_layout = QVBoxLayout(button_box)
        
        save_button = QPushButton("Create")
        cancel_button = QPushButton("Cancel")
        
        save_button.clicked.connect(dialog.accept)
        cancel_button.clicked.connect(dialog.reject)
        
        button_layout.addWidget(save_button)
        button_layout.addWidget(cancel_button)
        
        layout.addWidget(button_box)
        
        result = dialog.exec()
        
        if result == QDialog.DialogCode.Accepted:
            launcher_name = line_edit.text().strip()
            if launcher_name and not fman.is_filename_invalid(launcher_name):
                launcher_path = os.path.join(APPID_DIR, launcher_name)
                os.makedirs(launcher_path, exist_ok=True)
                self.reload_launcher_widget()
            else:
                fman.load_message_box(
                    self,
                    "Error",
                    "Invalid launcher folder name.",
                    QMessageBox.Icon.Warning,
                    QMessageBox.StandardButton.Ok
                )
        

    ### File Page ###

    def filename_changed(self):
        self.data['file_name'] = self.filename.text()

        #TODO: this clearly indicates an invalid filename but looks VERY bad while doing it
        if fman.is_filename_invalid(self.data['file_name']):
            self.filename.setStyleSheet("QLineEdit { background-color: #ff0000; }")
        else:
            self.filename.setStyleSheet("")

        self.update_save_button()
        
    def displayname_changed(self):
        self.data['display_name'] = self.displayname.text()
        
    def update_save_button(self):
        """Requires a launcher and file name to be set before allowing you to try saving."""
        if (self.data['launcher'] and not fman.is_filename_invalid(self.data['file_name'])):
            self.save.setEnabled(True)
        else:
            self.save.setEnabled(False)

# Logic that loads the app
app = QApplication([])
icon = fman.icon

window_main = MainWindow()
logic = ApplicationLogic(window_main.ui_widget)
window_main.logic = logic

window_main.show()
app.exec()