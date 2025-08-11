import os, shutil
from re import search

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

def invalid_filename(filename: str) -> bool:
    """Determines that a given file name has only valid characters using re.search. 
    Returns False if there are no issues."""
    if not filename or '/' in filename or filename in ('.', '..'):
        return True
    # Use re.search to find any character NOT allowed
    if search(r'[^\w\-.]', filename):
        return True
    return False

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
        self.launch_options: str = self.print_launch_options()

    # DATA OUTPUT

    def __str__(self) -> str:
        """Returns all relevant information in the active file."""
        output: str = (
            f"Path to File: {self.path_to_file}\n"
            f"Filename: {self.print_filename()}\n"
            f"Display Name: {self.print_displayname()}\n"
            f"Export Lines: {self.print_export_lines()}\n"
            f"Gamescope Line: {self.print_gamescope_line()}"
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
    
    def print_launch_options(self) -> str:
        """Returns the stored launch options as a string."""
        with open(self.path_to_file, 'r') as file:
            lines = file.readlines()

        for line in lines:
            if line.startswith('command+='):
                match = search(r"command+='([^']*)'", line)
                if match:
                    return match.group(1)
        return 'No launch options line'

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

    def create_new_gamescope_line(self): 
        """ if config file doesn't have an active gamescope args line, create one in the best place.
        this will be after a commented out line if one is found, or at the end."""

        # will be used if the correct line isn't already present
        new_line = f'SCB_GAMESCOPE_ARGS=""\n'

        with open(self.path_to_file, 'r') as file:
            lines = file.readlines()

        if lines and not lines[-1].endswith('\n'):
            lines[-1] += '\n'

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
                    with open(self.path_to_file, 'w') as file: 
                        file.writelines(lines)
                    return

        # Assume the gamescope_args line has no breaking issues at this point.

        # check for the default commented out line in the config file.
        # if found, place the new gamescope line right after it
        for i, line in enumerate(lines):
            if line.startswith('#SCB_GAMESCOPE_ARGS'):
                lines[i:i+1] = [line, new_line]
                # Write the modified lines back to the file
                with open(self.path_to_file, 'w') as file:
                    file.writelines(lines)
                self.gamescope_line: str = self.print_gamescope_line()
                return
    
        # no match was found, so create the necessary line at the end of the file
        with open(self.path_to_file, 'a') as file:
            if lines and not lines[-1].endswith('\n'):
                file.write('\n')
            file.write('SCB_GAMESCOPE_ARGS=""\n')
        self.gamescope_line: str = self.print_gamescope_line()
        return

    def edit_gamescope_line(self, new_flags:str) -> None:
        """Changes the gamescope args in the file to the newly listed ones,
        commenting out the old line and appending the new one in its place."""

        new_line = f'SCB_GAMESCOPE_ARGS="{new_flags}"\n'

        with open(self.path_to_file, 'r') as file:
            lines = file.readlines()

        if lines and not lines[-1].endswith('\n'):
            lines[-1] += '\n'

        for i, line in enumerate(lines):
            if line.startswith('SCB_GAMESCOPE_ARGS='):

                lines[i:i+1] = [f'#SCBGUI#{line}', new_line]
                with open(self.path_to_file, 'w') as file: 
                    file.writelines(lines)
                # update gamescope line stored by program
                self.gamescope_line: str = self.print_gamescope_line()
                return
            
        # place gamescope line at the end, because no line was found in the file
        with open(self.path_to_file, 'a') as file: 
            file.writelines(new_line)
        self.gamescope_line: str = self.print_gamescope_line()
        return

    def edit_exact_lines(self,start_with:list[str],new_lines:list[str]) -> None:
        """Checks for any lines that start with the start_with string, 
        replaces that portion with the string in the 2nd list's same index.\n
        Edit only one line by using two lists with one entry."""
        if len(start_with) != len(new_lines):
            raise ValueError
        
        with open(self.path_to_file, 'r') as file:
            lines = file.readlines()

        if lines and not lines[-1].endswith('\n'):
            lines[-1] += '\n'

        lines_to_append = []
        
        for j, start_str in enumerate(start_with):
            found = False
            for i, line in enumerate(lines):
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

        # This will only be needed for the AppID folder.
        self.config_files = [
            ConfigFile(os.path.join(self.appid_path, file))
            for file in os.listdir(self.appid_path)
            if os.path.isfile(os.path.join(self.appid_path, file)) and file.endswith(".conf")
        ]
        
    def __str__(self) -> str:
        """Returns detected path to scopebuddy directory."""
        return self.directory_path
    
    def print_files_list(self) -> list[str]:
        """Returns a list of readable strings describing each config file."""
        return [f"{config.print_filename()}: {config.print_displayname()}" for config in self.config_files]
    
    def print_appid_dict(self) -> dict[str, str]:
        """Returns a dictionary of filepath: displayname"""
        return {config.print_path(): config.print_displayname() for config in self.config_files}
    


    # DATA EDITING

    def create_file(self,filename:str,displayname:str='',directory:str=APPID_DIR) -> bool:
        """Adds a new file to the chosen directory and gives it a displayname. 
        If no display name is provided, it will default to the filename.
        If the file cannot be made, it will return True."""
        if invalid_filename(filename):
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
                    new_file.create_new_gamescope_line()
                else:
                    new_file.edit_displayname(filename)
                    new_file.create_new_gamescope_line()

                return False

        except FileExistsError:
            # Expected response outside of first launch
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





