#!/usr/bin/env python3

import sys
sys.path.insert(0, "/app/share/scopebuddygui") # flatpak path
import os
import file_manager as fman
from welcome import WelcomeLogic
from env_var import EnvVarLogic
from gamescope import GamescopeLogic

#PySide6, Qt Designer UI files
from PySide6.QtWidgets import QApplication, QStackedWidget, QListWidget, QTabWidget, QStatusBar, QDialog, QDialogButtonBox, QMessageBox, QLineEdit, QCheckBox, QDoubleSpinBox, QComboBox, QPushButton, QLabel, QToolButton, QMenu
from PySide6.QtGui import QIcon
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtCore import Qt

DATA_DIR = fman.get_data_path()

ui_main = os.path.join(DATA_DIR, "main.ui")
ui_welcome = os.path.join(DATA_DIR, "welcome.ui")
ui_env_vars = os.path.join(DATA_DIR, "env_var.ui")
ui_gamescope = os.path.join(DATA_DIR, "gamescope.ui")
template = os.path.join(DATA_DIR, "default_scb.conf")
active_config = os.path.join(os.environ.get("XDG_CONFIG_HOME", os.path.expanduser("~/.config")), "scopebuddy", "scb.conf")

# bundle of ui-launching code
def load_widget(ui_file: str):
    """Load a widget from a UI file and return it."""
    loader = QUiLoader()
    ui = QFile(ui_file)
    ui.open(QFile.OpenModeFlag.ReadOnly)
    widget = loader.load(ui)
    ui.close()
    return widget

def launch_window(ui_file:str,window_title:str="WindowTitle"):
    """Launch a new window of the given ui element, optionally set the window title."""
    window = load_widget(ui_file=ui_file)
    # set window attributes
    window.setWindowTitle(window_title)
    window.setWindowIcon(icon)
    return window

fman.create_directory()
fman.ensure_file(active_config) # makes sure the scb.conf file exists and works properly


class ApplicationLogic(WelcomeLogic,EnvVarLogic,GamescopeLogic):
    def __init__(self, window): # for reference in other classes, self.widget becomes logic.widget
        

        self.window = window # logical to use because it is not a subclass of any Qt class
        self.mainWidget = self.window.findChild(QTabWidget,"tabWidget")

        # Load ui pages into main window, one tab for each widget
        welcome_widget = load_widget(ui_welcome)
        env_vars_widget = load_widget(ui_env_vars)
        gamescope_widget = load_widget(ui_gamescope)

        # Initialize the logic for the ui pages
        super().__init__(welcome_widget)
        #super().__init__(env_vars_widget)
        #super().__init__(gamescope_widget)


        self.mainWidget.addTab(welcome_widget, "Welcome")
        self.mainWidget.addTab(env_vars_widget, "Environment Variables")
        self.mainWidget.addTab(gamescope_widget, "Gamescope")

        self.mainWidget.setCurrentIndex(0)
        
        # Welcome Window

        # Environment Variables Window

        # Gamescope Window

        # Apply Window






# Logic that loads the app
app = QApplication([])
icon = QIcon.fromTheme("io.github.rfrench3.scopebuddy-gui")

window_main = launch_window(ui_main,"Scopebuddy GUI")
logic = ApplicationLogic(window_main)

window_main.show()
app.exec()