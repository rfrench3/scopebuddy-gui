"""
This is split into two different sections: Managing Qt UI files, and config files within xdg-config/scopebuddy.
It ends with loading constant directories for the app itself and for the scopebuddy config files.
"""

import os, shutil
from re import search

from PySide6.QtGui import QIcon
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile


# Managing Qt UI files

icon = QIcon.fromTheme("io.github.rfrench3.scopebuddy-gui")

def load_widget(ui_file: str, window_title:str='Scopebuddy GUI', icon:QIcon=icon): # type: ignore # icon being None results in no failure
    """Load a widget from a UI file and return it."""
    loader = QUiLoader()
    ui = QFile(ui_file)
    ui.open(QFile.OpenModeFlag.ReadOnly)
    widget = loader.load(ui)
    ui.close()
    if widget.isWindow():
        # set window attributes
        widget.setWindowTitle(window_title)
        widget.setWindowIcon(icon)
    return widget




# Managing scopebuddy config files

def get_data_path():
    """Returns the path to data of the program. This means files such as """
    return os.path.abspath(os.path.dirname(__file__))

    
def create_directory():
    """Create the directory for /scopebuddy/scb.conf, returns full path to scb.conf"""
    CONFIG_DIR = os.path.join(os.environ.get("XDG_CONFIG_HOME", os.path.expanduser("~/.config")), "scopebuddy")
    os.makedirs(CONFIG_DIR, exist_ok=True)
    selected_config_file = os.path.join(CONFIG_DIR, "scb.conf")

def ensure_file(selected_config_file) -> None: 
    """creates config file if it doesn't exist, and calls on ensure_gamescope_line afterwards."""
    def ensure_gamescope_line(): 
        """ if config file doesn't have the gamescope args line, create one in the best place.
        this will be where a commented out line is if one is found, or at the end."""

        # will be used if the correct line isn't already present
        new_line = f'SCB_GAMESCOPE_ARGS=""\n'

        with open(selected_config_file, 'r') as file:
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
                    with open(selected_config_file, 'w') as file: 
                        file.writelines(lines)
                    return

        # Assume the gamescope_args line has no breaking issues at this point.

        # check for the default commented out line in the config file.
        # if found, place the new gamescope line right after it
        for i, line in enumerate(lines):
            if line.startswith('#SCB_GAMESCOPE_ARGS'):
                lines[i:i+1] = [line, new_line]
                # Write the modified lines back to the file
                with open(selected_config_file, 'w') as file:
                    file.writelines(lines)
                return
    
        # no match was found, so create the necessary line at the end of the file
        with open(selected_config_file, 'a') as file:
            if lines and not lines[-1].endswith('\n'):
                file.write('\n')
            file.write('SCB_GAMESCOPE_ARGS=""\n')
        return
            
    try:
        if os.path.exists(selected_config_file):
            #print(f"Config file already exists at {selected_config_file}, ensuring the proper format...")
            ensure_gamescope_line()
            return
        else:
            #print(f"Creating config file at {selected_config_file} from template...")
            shutil.copyfile(TEMPLATE, selected_config_file)
            ensure_gamescope_line()
            return
    except Exception as e:
        print(f"Error creating config file: {e}")


'''
The ConfigFile class:
PURPOSE: store data about the scopebuddy config file given to it and have simple methods for reading/editing that data.
OUTPUT: name of file, first line of file (display name), all export lines in file (env vars), gamescope line.
ALTER: first line of file, all export lines, gamescope line
'''
class ConfigFile:
    def __init__(self,path_to_file:str) -> None:
        self.path_to_file:str = path_to_file
        self.filename: str = os.path.basename(self.path_to_file)
        self.displayname: str = self.print_displayname()
        self.export_lines: list[str] = self.print_export_lines()
        self.gamescope_line: str = self.print_gamescope_line()

    # DATA OUTPUT

    def __str__(self) -> str:
        """Returns all relevant information in the active file."""
        output: str = (
            f"Path to File: {self.path_to_file}\n"
            f"Filename: {self.print_filename()}\n"
            f"Display Name: {self.print_displayname()}\n"
            f"Export Lines: {self.print_export_lines()}\n"
            f"Gamescope Line: {self.print_gamescope_line()}"
        )
        return output
    
    def print_path(self) -> str:
        """Returns the path of the file"""
        return self.path_to_file
    
    def print_filename(self) -> str:
        """Returns the name of the file"""
        return os.path.basename(self.path_to_file)
    
    def print_displayname(self) -> str:
        """Read the display name (the commented out line 1) from the active file."""
        if self.path_to_file == GLOBAL_CONFIG:
            return "Global Config"
        with open(self.path_to_file, 'r') as file:
            first_line = file.readline().strip()
            if first_line.startswith("# "):
                return first_line[2:]
            else:
                return "No display name"
    
    def print_export_lines(self) -> list[str]:
        """Returns a list of export lines (Environment Variables)."""
        export_lines: list[str] = []
        with open(self.path_to_file, 'r') as file:
            lines = file.readlines()

        for line in lines:
            if line.startswith('export '):
                export_lines.append(line[7:-1])
        return export_lines

    def print_gamescope_line(self) -> str:
        """Returns the stored gamescope launch arguments as a string."""
        with open(self.path_to_file, 'r') as file:
            lines = file.readlines()

        for line in lines:
            if line.startswith('SCB_GAMESCOPE_ARGS='):
                match = search(r'SCB_GAMESCOPE_ARGS="([^"]*)"', line)
                if match:
                    return match.group(1)
        return 'No gamescope line'

    
    
    # DATA EDITING
    
    def edit_displayname(self, new_name:str) -> None:
        """Changes the display name (the commented out line 1) inside the file."""
        pass

    def edit_export_lines(self, new_lines:list[str]) -> None:
        """Changes the export lines in the file to the newly listed ones."""
        pass

    def edit_gamescope_line(self, new_line:str) -> None:
        """Changes the gamescope args in the file to the newly listed ones."""
        pass


DATA_DIR = os.path.abspath(os.path.dirname(__file__))
TEMPLATE = os.path.join(DATA_DIR, "default_scb.conf")

APPID_DIR = os.path.join(os.environ.get("XDG_CONFIG_HOME", os.path.expanduser("~/.config")), "scopebuddy", "AppID") #folder
GLOBAL_CONFIG = os.path.join(os.environ.get("XDG_CONFIG_HOME", os.path.expanduser("~/.config")), "scopebuddy", "scb.conf") #file

#SVG_PATH = QIcon.themeSearchPaths()[0] + "/io.github.rfrench3.scopebuddy-gui.svg"


ui_main = os.path.join(DATA_DIR, "main.ui")
ui_env_vars = os.path.join(DATA_DIR, "environment_variables.ui")
ui_gamescope = os.path.join(DATA_DIR, "gamescope.ui")
ui_apply_changes = os.path.join(DATA_DIR, "apply.ui")

ui_env_vars_entry = os.path.join(DATA_DIR, "env_var.ui")