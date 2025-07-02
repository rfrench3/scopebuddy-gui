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




# Managing scopebuddy files

def get_data_path():
    """Returns the path to data of the program. This means files such as """
    if os.path.basename(os.path.dirname(__file__)) == "src":
        return os.path.abspath(os.path.dirname(__file__))
    else:
        return os.path.abspath(os.path.join(os.path.dirname(__file__), "../share/scopebuddygui"))
    
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





DATA_DIR = get_data_path()
TEMPLATE = os.path.join(DATA_DIR, "default_scb.conf")

APPID_DIR = os.path.join(os.environ.get("XDG_CONFIG_HOME", os.path.expanduser("~/.config")), "scopebuddy", "AppID") #folder
GLOBAL_CONFIG = os.path.join(os.environ.get("XDG_CONFIG_HOME", os.path.expanduser("~/.config")), "scopebuddy", "scb.conf") #file

ui_main = os.path.join(DATA_DIR, "main.ui")
ui_welcome = os.path.join(DATA_DIR, "welcome.ui")
ui_env_vars = os.path.join(DATA_DIR, "environment_variables.ui")
ui_gamescope = os.path.join(DATA_DIR, "gamescope.ui")
ui_apply_changes = os.path.join(DATA_DIR, "apply.ui")

ui_env_vars_entry = os.path.join(DATA_DIR, "env_var.ui")