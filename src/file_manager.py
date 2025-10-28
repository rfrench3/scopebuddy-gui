import os, shutil
from re import search

# TODO: consider replacing os.path use with Path in the future, 
# for now it's just here to validate filenames
from pathlib import Path 

from PySide6.QtGui import QIcon
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QMessageBox

#################################################
# data directories for program and config files #
#################################################

# program files
DATA_DIR:str = os.path.abspath(os.path.dirname(__file__))
TEMPLATE:str = os.path.join(DATA_DIR, "default_scb.conf")

# config files
SCB_DIR:str = os.path.join(os.environ.get("XDG_CONFIG_HOME", os.path.expanduser("~/.config")), "scopebuddy") #folder
APPID_DIR:str = os.path.join(SCB_DIR, "AppID") #folder
GLOBAL_CONFIG:str = os.path.join(os.environ.get("XDG_CONFIG_HOME", os.path.expanduser("~/.config")), "scopebuddy", "scb.conf") #file

# program UI files
ui_main = os.path.join(DATA_DIR, "main.ui")
ui_env_vars = os.path.join(DATA_DIR, "environment_variables.ui")
ui_gamescope = os.path.join(DATA_DIR, "gamescope.ui")
ui_general_settings = os.path.join(DATA_DIR, "general_settings.ui")
ui_launch_options = os.path.join(DATA_DIR, "launch_options.ui")

ui_env_vars_entry = os.path.join(DATA_DIR, "env_var.ui")
ui_launch_options_entry = os.path.join(DATA_DIR, "launch_opt.ui")

# SVG file for display on the homepage
svg_path:str = os.path.join(DATA_DIR,"io.github.rfrench3.scopebuddy-gui.svg") 
if not os.path.exists(svg_path):
    # Not running in flatpak, default to source code path
    svg_path = os.path.join(DATA_DIR, "img", "io.github.rfrench3.scopebuddy-gui.svg")


########################
# Managing Qt UI files #
########################

icon = QIcon.fromTheme("io.github.rfrench3.scopebuddy-gui")

def load_widget(ui_file: str, window_title:str='Scopebuddy GUI', icon:QIcon|None=icon):
    """Load a widget from a UI file and return it."""
    loader = QUiLoader()
    ui = QFile(ui_file)
    ui.open(QFile.OpenModeFlag.ReadOnly)
    widget = loader.load(ui)
    ui.close()
    if widget.isWindow():
        # set window attributes
        widget.setWindowTitle(window_title)
        widget.setWindowIcon(icon) #type:ignore
    return widget

def load_message_box(parent_window,title:str,  text:str,  icon:QMessageBox.Icon=QMessageBox.Icon.Information,  standard_buttons:QMessageBox.StandardButton=QMessageBox.StandardButton.Ok) -> QMessageBox.StandardButton:
    """Loads a QMessageBox, returns the result of exec()."""
    msg = QMessageBox(parent_window)
    msg.setIcon(icon)
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.setStandardButtons(standard_buttons)
    return msg.exec() #type:ignore

####################################
# Managing scopebuddy config files #
####################################
    
def create_directory() -> None:
    """Create the directory for /scopebuddy/AppID."""
    APPID_DIR = os.path.join(os.environ.get("XDG_CONFIG_HOME", os.path.expanduser("~/.config")), "scopebuddy", "AppID")
    os.makedirs(APPID_DIR, exist_ok=True)

def is_filename_invalid(filename:str) -> bool:
    """True if not valid, false otherwise"""
    
    if not filename or filename in ('.', '..'):
        return True

    if '/' in filename or '\\' in filename:
        return True

    if '\0' in filename:
        return True

    try:
        # Validate using pathlib
        path = Path(filename)
        if path.is_absolute():
            return True
        return False
    except (ValueError, OSError):
        return True

'''
The ConfigFile class:
PURPOSE: store data about the scopebuddy config file given to it and have simple methods for reading/editing that data.
OUTPUT: name of file, first line of file (display name), all export lines in file (env vars), gamescope line.
ALTER: first line of file, all export lines, gamescope line
'''
class ConfigFile:
    def __init__(self,path_to_file:str) -> None:
        self.path_to_file:str = path_to_file
        self.filename: str = self.print_filename()
        self.displayname: str = self.print_displayname()
        self.export_lines: list[str] = self.print_export_lines()
        self.gamescope_data: dict = self.return_gamescope_data()
        self.launch_options: str = self.print_launch_options()

    # DATA OUTPUT

    def __str__(self) -> str:
        """Returns all relevant information in the active file."""
        output: str = (
            f"Path to File: {self.path_to_file}\n"
            f"Filename: {self.print_filename()}\n"
            f"Display Name: {self.print_displayname()}\n"
            f"Export Lines: {self.print_export_lines()}\n"
            f"Gamescope Line: {self.return_gamescope_data()['args']}"
            f"Launch Options: {self.print_launch_options()}"
        )
        return output
    
    def print_path(self) -> str:
        """Returns the path of the file"""
        return self.path_to_file
    
    def print_filename(self) -> str:
        """Returns the name of the file"""
        return os.path.basename(self.path_to_file)
    
    def print_displayname(self) -> str:
        """Read the display name (the commented out line 1) from the active file.
        If the first line does not start with "# ", return the file name instead."""
        if self.path_to_file == GLOBAL_CONFIG:
            return "Global Config"
        with open(self.path_to_file, 'r') as file:
            first_line = file.readline().strip()
            if first_line.startswith("# "):
                return first_line[2:]
            else:
                return self.print_filename()
    
    def print_export_lines(self) -> list[str]:
        """Returns a list of active export lines (Environment Variables)."""
        export_lines: list[str] = []
        with open(self.path_to_file, 'r') as file:
            lines = file.readlines()

        for line in lines:
            if line.startswith('export '):
                export_lines.append(line[7:-1])
        return export_lines

    def return_gamescope_data(self) -> dict:
        """return dictionary about the gamescope line's status.\n
        args: gamescope args\n
        active:  is a gamescope line active?"""
        data = {
            'args': '',
            'active': False
        }

        with open(self.path_to_file, 'r') as file:
            lines = file.readlines()

        for line in lines:
            # an active line would never automatically be placed above an automatically commented out line
            if line.startswith('SCB_GAMESCOPE_ARGS='):
                data['active'] = True

            if (line.startswith('SCB_GAMESCOPE_ARGS=') or
                line.startswith('#SCBGUI#SCB_GAMESCOPE_ARGS=') or
                line.startswith('#SCB_GAMESCOPE_ARGS=')
                ):
                
                # return args
                match = search(r'SCB_GAMESCOPE_ARGS="([^"]*)"', line)                
                data['args'] = match.group(1) if match else ''

        return data

    def print_launch_options(self) -> str:
        """Returns the stored launch options as a string."""
        with open(self.path_to_file, 'r') as file:
            lines = file.readlines()

        for line in lines:
            if line.startswith(r'command+='):
                match = search(r"command\+='([^']*)'", line)
                if match:
                    return match.group(1)
                
        return ''
    
    def check_for_exact_line(self,startswith:str) -> bool:
        """Checks for a line that starts with a certain value. 
        Returns True if exactly that line it is found."""

        with open(self.path_to_file, 'r') as file:
            lines = file.readlines()

        for line in lines:
            if line.startswith(startswith):
                return True
        else:
            return False

    
    # DATA EDITING
    #TODO: implementing regex/string normals for editing lines would simplify certain things
    
    def edit_displayname(self, new_name:str) -> None:
        """Changes the display name (the commented out line 1) inside the file.
        Does not save the old display name when doing this."""
        
        try:
            with open(self.path_to_file, 'r') as file:
                lines = file.readlines()

            if lines and lines[0].startswith("# "):
                lines[0] = f"# {new_name}\n"
            else:
                lines.insert(0,f"# {new_name}\n")

            with open(self.path_to_file, 'w') as file:
                file.writelines(lines)
        except Exception as e:
            print(f"Failed to edit display name: {e}")
        
    def edit_export_lines(self, new_lines:list[str]) -> None:
        """Changes the export lines in the file to the newly listed ones by commenting out
        or uncommenting in lines, only adding new lines when necessary."""

        with open(self.path_to_file, 'r') as file:
            lines = file.readlines()

        if lines and not lines[-1].endswith('\n'):
            lines[-1] += '\n'

        # disable all oldlines
        for i, oldline in enumerate(lines):
            if oldline.startswith("export "):
                lines[i] = f"#{oldline}" 
        
        # re-enable any oldlines that match a newline
        for i, oldline in enumerate(lines):
            if oldline.startswith("#export "):
                for newline in new_lines[:]:
                    if oldline.startswith(f"#export {newline}"): # accounts for comments
                        new_lines.remove(newline)
                        lines[i] = oldline[1:]
                        break


        # append any newlines not in oldlines to the file
        if new_lines:

            
            for i, line in enumerate(lines[:]):
                if i == 0:
                    continue
                
                
                prev_line_is_export:bool = (lines[i-1].startswith("export ") or lines[i-1].startswith("#export "))
                curr_line_is_not_export:bool = not (line.startswith("export ") or line.startswith("#export "))

                if prev_line_is_export and curr_line_is_not_export:
                    
                    for export in new_lines[::-1]:
                        lines.insert(i, f"export {export}\n")
                        new_lines.remove(export)
                    
                    break
        

        # append new exports to the end of the file, because none were found within the file
        if new_lines:
            
            append_lines = [
                f"export {line}\n"
                for line in new_lines
            ]

            lines.extend(append_lines)

        with open(self.path_to_file,'w') as file:
            file.writelines(lines)

    def edit_gamescope_line(self, arguments:str, active:bool) -> None:
        """Changes the gamescope line in the file to the newly listed ones by commenting out
        or uncommenting in lines, only adding new lines when necessary.
        (made for export lines, but works better for the gamescope line than my other efforts)"""

        new_args = [arguments]

        with open(self.path_to_file, 'r') as file:
            lines = file.readlines()

        if lines and not lines[-1].endswith('\n'):
            lines[-1] += '\n'

        # disable all oldlines
        for i, oldline in enumerate(lines):
            if oldline.startswith("SCB_GAMESCOPE_ARGS="):
                lines[i] = f"#{oldline}" 
        
        # re-enable any oldlines that match a newline
        for i, oldline in enumerate(lines):
            if oldline.startswith("#SCB_GAMESCOPE_ARGS=") or oldline.startswith("#SCBGUI#SCB_GAMESCOPE_ARGS="):
                for args in new_args[:]:
                    if oldline.startswith(f'SCB_GAMESCOPE_ARGS="{args}"'): # accounts for comments
                        new_args.remove(args)
                        lines[i] = oldline[1:]
                        break


        # append any newlines not in oldlines to the file
        if new_args:
            
            for i, line in enumerate(lines[:]):
                if i == 0:
                    continue
                            
                prev_line_is_export:bool = (lines[i-1].startswith("SCB_GAMESCOPE_ARGS=") or 
                                            lines[i-1].startswith("#SCB_GAMESCOPE_ARGS=") or 
                                            lines[i-1].startswith("#SCBGUI#SCB_GAMESCOPE_ARGS=")
                                            )
                curr_line_is_not_export:bool = not (line.startswith("SCB_GAMESCOPE_ARGS=") or 
                                                    line.startswith("#SCB_GAMESCOPE_ARGS=") or 
                                                    line.startswith("#SCBGUI#SCB_GAMESCOPE_ARGS=")
                                                    )

                if prev_line_is_export and curr_line_is_not_export:
                    
                    for export in new_args[::-1]:
                        lines.insert(i, f'SCB_GAMESCOPE_ARGS="{export}"\n')
                        new_args.remove(export)
                    
                    break
        

        # append new exports to the end of the file, because none were found within the file
        if new_args:
            
            append_lines = [
                f'SCB_GAMESCOPE_ARGS="{line}\n"'
                for line in new_args
            ]

            lines.extend(append_lines)

        if not active:
            for i, line in enumerate(lines):
                if line.startswith("SCB_GAMESCOPE_ARGS="):
                    lines[i] = f'#{line}'
                    break

        # remove duplicate lines
        for i, line in enumerate(lines):
            if i == 0:
                continue
            if lines[i] == lines[i-1]:
                lines.pop(i)



        with open(self.path_to_file,'w') as file:
            file.writelines(lines)

        self.gamescope_data = self.return_gamescope_data()

    def update_gamescope_data(self, data:dict, DEPRACATED=True) -> None:
        """Update information about the gamescope line's status.\n
        args: str, gamescope args\n
        inactive: bool, should gamescope line be commented out"""

        # args to go in gamescope line
        args:str = data['args']

        # if true, no gamescope line in the file
        disable_gamescope:bool = data['inactive']

        with open(self.path_to_file, 'r') as file:
            lines = file.readlines()
        if lines and not lines[-1].endswith('\n'):
            lines[-1] += '\n'

        new_line = f'SCB_GAMESCOPE_ARGS="{args}"\n'

        backwards = lines[::-1] #type:ignore

        scb_found = False
        for i, line in enumerate(backwards):
            if line.startswith('SCB_GAMESCOPE_ARGS='):
                if disable_gamescope:
                    backwards[i] = f"#SCBGUI#{line}#SCBGUI#{new_line}"
                else:
                    backwards[i] = f"#SCBGUI#{line}{new_line}"
                scb_found = True
                break

            if line.startswith('#SCBGUI#SCB_GAMESCOPE_ARGS='):
                if disable_gamescope:
                    backwards[i] = f"{line}#SCBGUI#{new_line}"
                else:
                    backwards[i] = f"{line}{new_line}"
                scb_found = True
                break

            if line.startswith('#SCB_GAMESCOPE_ARGS='): #default example line
                if disable_gamescope:
                    backwards[i] = f"{line}#SCBGUI#{new_line}"
                else:
                    backwards[i] = f"{line}{new_line}"
                scb_found = True
                break

        new_lines = backwards[::-1]

        if not scb_found:
            # no scb_gamescope_args in file, put it at the end
            new_lines.append(new_line)

        with open(self.path_to_file, 'w') as file: 
            file.writelines(new_lines)

        # update gamescope data stored by program
        self.gamescope_data = self.return_gamescope_data()
        return
   
    def edit_exact_lines(self,start_with:list[str],new_lines:list[str],  opened_lines: list[str]|None=None) -> None | list[str]:
        """Checks for any lines that start with the start_with string, 
        replaces that portion with the string in the 2nd list's same index.\n
        Edit only one line by using two lists with one entry.
        If a start_with string is empty or not found, append the new line to the end of the file.\n
        If opened_lines is given, uses those and returns them in place of directly reading/editing the file."""
        if len(start_with) != len(new_lines):
            raise ValueError
        
        if opened_lines:
            lines = opened_lines
        else:
            with open(self.path_to_file, 'r') as file:
                lines = file.readlines()
            if lines and not lines[-1].endswith('\n'):
                lines[-1] += '\n'

        lines_to_append = []
        
        for j, start_str in enumerate(start_with):
            found = False
            for i, line in enumerate(lines):
                if start_str == '':
                    break # empty start_str means new line

                if line.startswith(start_str):
                    # Preserve any data after the start_str portion, such as comments left by the user
                    remaining_data = line[len(start_str):]
                    lines[i] = new_lines[j] + remaining_data
                    found = True
                    break
            
            if not found:
                # Add newline if the new line doesn't already end with one
                line_to_add = new_lines[j] + '\n' if not new_lines[j].endswith('\n') else new_lines[j]
                lines_to_append.append(line_to_add)
        
        # Append any lines that weren't found
        if lines_to_append:
            lines.extend(lines_to_append)

        if opened_lines:
            return lines
        else:    
            with open(self.path_to_file, 'w') as file:
                file.writelines(lines)
        
    def edit_launch_options(self, new_flags:str) -> None:
        """Changes the launch options in the file to the newly listed ones."""

        new_line = f"command+=' {new_flags.strip()}'\n"

        with open(self.path_to_file, 'r') as file:
            lines = file.readlines()

        if lines and not lines[-1].endswith('\n'):
            lines[-1] += '\n'

        for i, line in enumerate(lines):
            if line.startswith('command+='):

                lines[i] = new_line
                with open(self.path_to_file, 'w') as file: 
                    file.writelines(lines)
                # update launch options line stored by program
                self.launch_options: str = self.print_launch_options()
                return
            
        # place launch options line at the end, because no line was found in the file
        with open(self.path_to_file, 'a') as file: 
            file.writelines(new_line)
        self.launch_options: str = self.print_launch_options()
        return



'''
The ScopebuddyDirectory class:
PURPOSE: store data about the scopebuddy directory and its files and have simple methods for reading/editing that data.
OUTPUT: list of available files, name of files, first line of files (display name)
ALTER: add new files to directory
'''

class ScopebuddyDirectory:
    def __init__(self) -> None:
        self.directory_path = os.path.join(os.environ.get("XDG_CONFIG_HOME", os.path.expanduser("~/.config")), "scopebuddy")
        self.appid_path = os.path.join(self.directory_path,"AppID")

        # store all necessary info about files and their paths for the file selection part of the app
        self.full_directory = self.return_filesystem_information(self.directory_path)
        
    def __str__(self) -> str:
        """Returns detected path to scopebuddy directory."""
        return self.directory_path
    
    def print_files_list(self) -> list[str]:
        """Returns a list of readable strings describing each config file."""

        config_files = [
            ConfigFile(os.path.join(self.appid_path, file))
            for file in os.listdir(self.appid_path)
            if os.path.isfile(os.path.join(self.appid_path, file)) and file.endswith(".conf")
            ]


        return [f"{config.print_filename()}: {config.print_displayname()}" for config in config_files]
    
    def print_appid_dict(self) -> dict[str, str]:
        """Returns a dictionary of filepath: displayname"""

        config_files = [
            ConfigFile(os.path.join(self.appid_path, file))
            for file in os.listdir(self.appid_path)
            if os.path.isfile(os.path.join(self.appid_path, file)) and file.endswith(".conf")
            ]
        
        return {config.print_path(): config.print_displayname() for config in config_files}

    def return_filesystem_information(self, directory: str) -> dict:
        """Returns a nested dictionary about the scopebuddy directory.\n
        All entries have type=file/folder, path=path, name=filename.\n
        Files have displayname, 
        folders have a children that contains its own nested dictionary.
        
        """
        information = {}

        # Scan directory for all items
        try:
            items = os.listdir(directory)
        except Exception as e:
            print(f"return_filesystem_information ERROR! {e}")
            raise e

        for name in items:
            path = os.path.join(directory, name)
            
            if os.path.isfile(path):
                # Handle files - add displayname for .conf files
                item = {
                    'type': 'file',
                    'path': path,
                    'name': name
                }
                
                # Add displayname for config files
                if name.endswith('.conf'):
                    try:
                        config = ConfigFile(path)
                        item['displayname'] = config.print_displayname()
                    except Exception as e:
                        item['displayname'] = name
                        print(e)
                
                information[name] = item
                
            elif os.path.isdir(path):
                # Handle folders - recursively scan subdirectories
                item = {
                    'type': 'folder',
                    'path': path,
                    'name': name,
                    'children': self.return_filesystem_information(path)  # Recursive call
                }
                information[name] = item

        return information

    # DATA EDITING

    def create_file(self,filename:str,displayname:str='',directory:str=APPID_DIR) -> bool:
        """Adds a new file to the chosen directory and gives it a displayname. 
        If no display name is provided, it will default to the filename.
        If the file cannot be made, it will return True."""
        if is_filename_invalid(filename):
            print("The chosen filename is not valid.")
            return True

        new_file_path = os.path.join(directory, filename)
        os.makedirs(directory, exist_ok=True)
        try:
            if os.path.exists(new_file_path):
                raise FileExistsError
            else:
                shutil.copyfile(TEMPLATE, new_file_path)
                new_file = ConfigFile(new_file_path)

                if displayname:
                    new_file.edit_displayname(displayname)
                else:
                    new_file.edit_displayname(filename)

                return False

        except FileExistsError:
            # Not a problem
            return True
        except FileNotFoundError as e:
            print(f"Unable to create config file: {e}")
            return True
        except PermissionError as e:
            print(f"Unable to create config file: {e}")
            return True
        except Exception as e:
            print(f"Unanticipated error: {e}")
            return True





