# This portion of the codebase is dedicated to backend
# code that is not dependent on any GUI toolkit.

import sys
sys.path.insert(0, "/app/share/scopebuddygui") # flatpak path

import os
from re import search # for searching for gamescope args in the config file

config_dir = os.path.join(os.environ.get("XDG_CONFIG_HOME", os.path.expanduser("~/.config")), "scopebuddy")
print(f'config_dir: {config_dir}')

os.makedirs(config_dir, exist_ok=True)
scbpath = os.path.join(config_dir, "scb.conf")
print(f'scbpath: {scbpath}') 

class Mixins: 
    def apply_global_config(self):
        # set the config
        the_config = self.generate_new_config()

        # make sure the necessary line and file exist
        self.create_config_path()
        self.make_gamescope_line()

        # Open the config file
        with open(scbpath, 'r') as file:
            lines = file.readlines()

            # Find the line that starts with SCB_GAMESCOPE_ARGS
            for i, line in enumerate(lines):
                if line.startswith('SCB_GAMESCOPE_ARGS'):
                    commented_line = f"# commented out by scopebuddy-gui: {line}"# Comment out the original line
                    new_line = f'SCB_GAMESCOPE_ARGS="{the_config}"\n'# Create the new line
                    lines[i:i+1] = [commented_line, new_line]# Replace with the commented + new line
                    break

            # Write the modified lines back to the file
            with open(scbpath, 'w') as file:
                file.writelines(lines)

        if self.read_gamescope_args().strip() != '':
            self.displayGamescope.setText(f'Current Gamescope Config: {self.read_gamescope_args()}') #display the current gamescope args
        else:
            self.displayGamescope.setText(f'No Gamescope arguments active!') #display the current lack of gamescope args

    def generate_new_config(self) -> str: #output a new config string based on the user input
        self.config_list = []

        def apply_lineEdit_input(lineEdit:int, arg): #won't append an empty arg
            if lineEdit.text().isdigit(): 
                self.config_list.append(f'{arg} {lineEdit.text()} ')                
            
        def apply_combobox_input(comboBox, arg): #appends combobox input to the config list (unless default)
            if comboBox.currentIndex() != 0:
                self.config_list.append(f'{arg} {comboBox.currentText()} ')

        def apply_checkbox_input(checkBox, arg): #appends checkbox input to the config list 
            if checkBox.isChecked():
                self.config_list.append(f'{arg} ')

        def apply_doubleSpinBox_input(doubleSpinBox, arg): #preferred for float values
            if doubleSpinBox.value() != 1.0:
                self.config_list.append(f'{arg} {doubleSpinBox.value()} ')

        def compile_arguments(settings):
            for widget_type, input_widget, arg in settings:
                if widget_type == 'checkbox':
                    apply_checkbox_input(input_widget, arg)
                elif widget_type == 'lineEdit':
                    apply_lineEdit_input(input_widget, arg)
                elif widget_type == 'comboBox':
                    apply_combobox_input(input_widget, arg)
                elif widget_type == 'doubleSpinBox':
                    apply_doubleSpinBox_input(input_widget, arg)
                elif widget_type == 'additionalArgs':
                    self.config_list.append(f'{input_widget.text()} ')
                else:
                    raise NotImplementedError(f"Widget type '{widget_type}' is not implemented.")
                
        # IMPLEMENTED ARGUMENTS
        self.settings = [
            ('checkbox', self.mangoHUD, '--mangoapp'),
            ('lineEdit', self.rHeight, '-h'),
            ('lineEdit', self.rWidth, '-w'),
            ('lineEdit', self.fps, '-r'),
            ('checkbox', self.fullscreen, '-f'),
            ('checkbox', self.bWindow, '-b'),
            ('lineEdit', self.oHeight, '-H'),
            ('lineEdit', self.oWidth, '-W'),
            ('checkbox', self.steam, '-e'),
            ('checkbox', self.hdr, '--hdr-enabled'),
            ('lineEdit', self.maxScale, '-m'),
            ('comboBox', self.upscalerType, '-S'),
            ('comboBox', self.upscalerFilter, '-F'),
            ('lineEdit', self.upscalerSharpness, '--sharpness'),
            ('doubleSpinBox', self.mouseSensitivity, '-s'),
            ('checkbox', self.vrr, '--adaptive-sync'),
            ('checkbox', self.fullscreenInGamescope, '--force-windows-fullscreen'),
            ('checkbox', self.fgCursor, '--force-grab-cursor'),
            ('additionalArgs', self.unimplemented, '--placeholder-value')
            ]
        
        compile_arguments(self.settings)

        generated_config = ''
        for argument in self.config_list:
            generated_config += argument
        
        print(f'The generated config file is {generated_config}')
        return generated_config
    
    def apply_current_to_ui(self): #checks current config, applies it to the UI

        def remove_arg(unimplemented,arg,match):
            # Remove the first instance of the value after the argument (e.g., '-s 1.5')
            try:
                arg_index = unimplemented.index(arg)
                # Ensure the next item exists and matches the value
                if arg_index + 1 < len(unimplemented) and unimplemented[arg_index + 1] == match.group(1):
                    unimplemented.pop(arg_index + 1)
            except ValueError:
                pass
            unimplemented.remove(arg) if arg in unimplemented else None

        def set_lineEdit_input(lineEdit:int, arg,unimplemented):
            args = self.read_gamescope_args()
            match = search(rf'{arg} (\d+)', args)
            if match:
                lineEdit.setText(match.group(1))
                remove_arg(unimplemented,arg,match)
                
            
        def set_combobox_input(comboBox, arg,unimplemented):
            args = self.read_gamescope_args()
            match = search(rf'{arg} ([^\s]+)', args)
            if match:
                value = match.group(1)
                for index in range(comboBox.count()):
                    if comboBox.itemText(index) == value:
                        comboBox.setCurrentIndex(index)
                        remove_arg(unimplemented,arg,match)
                

        def set_checkbox_input(checkBox, arg,unimplemented):
            checkBox.setChecked(arg in self.read_gamescope_args()) # set checkbox state based on config
            unimplemented.remove(arg) if arg in unimplemented else None
            

        def set_doubleSpinBox_input(doubleSpinBox, arg,unimplemented): #preferred for float values
            args = self.read_gamescope_args()
            match = search(rf'{arg} ([\d.]+)', args)
            if match:
                doubleSpinBox.setValue(float(match.group(1)))
                remove_arg(unimplemented,arg,match)

  

        def set_arguments(settings):
            unimplemented = self.read_gamescope_args().split()
            for widget_type, input_widget, arg in settings:
                if widget_type == 'checkbox':
                    set_checkbox_input(input_widget, arg,unimplemented)
                    unimplemented.remove(arg) if arg in unimplemented else None # remove the argument from the unimplemented list
                elif widget_type == 'lineEdit':
                    set_lineEdit_input(input_widget, arg,unimplemented)
                elif widget_type == 'comboBox':
                    set_combobox_input(input_widget, arg,unimplemented)
                elif widget_type == 'doubleSpinBox':
                    set_doubleSpinBox_input(input_widget, arg,unimplemented)
                else:
                    raise NotImplementedError(f"Widget type '{widget_type}' is not implemented.")
                self.unimplemented.setText(' '.join(unimplemented)) # set the unimplemented arguments to the line edit
            
        
        # IMPLEMENTED ARGUMENTS
        self.settings = [
            ('checkbox', self.mangoHUD, '--mangoapp'),
            ('lineEdit', self.rHeight, '-h'),
            ('lineEdit', self.rWidth, '-w'),
            ('lineEdit', self.fps, '-r'),
            ('checkbox', self.fullscreen, '-f'),
            ('checkbox', self.bWindow, '-b'),
            ('lineEdit', self.oHeight, '-H'),
            ('lineEdit', self.oWidth, '-W'),
            ('checkbox', self.steam, '-e'),
            ('checkbox', self.hdr, '--hdr-enabled'),
            ('lineEdit', self.maxScale, '-m'),
            ('comboBox', self.upscalerType, '-S'),
            ('comboBox', self.upscalerFilter, '-F'),
            ('lineEdit', self.upscalerSharpness, '--sharpness'),
            ('doubleSpinBox', self.mouseSensitivity, '-s'),
            ('checkbox', self.vrr, '--adaptive-sync'),
            ('checkbox', self.fullscreenInGamescope, '--force-windows-fullscreen'),
            ('checkbox', self.fgCursor, '--force-grab-cursor'),
            ]
        

        set_arguments(self.settings) # apply the current config to the UI elements

    def read_gamescope_args(self) -> str: #output gamescope args as string
        with open(scbpath, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith('SCB_GAMESCOPE_ARGS='):
                    match = search(r'SCB_GAMESCOPE_ARGS="([^"]*)"', line)
                    if match:
                        return match.group(1)
                    else:
                        print('WARNING: CHECK UNCOMMENTED LINES!') # config file has incorrect format
            return ''

    def make_gamescope_line(self) -> bool: #if config file doesn't have the gamescope args line, create one
        if not self.create_config_path(): # runs the function and detects if it fails
            raise FileNotFoundError("Config file or location creation failed.")
        with open(scbpath, 'r+') as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith('SCB_GAMESCOPE_ARGS='):
                    match = search(r'SCB_GAMESCOPE_ARGS="([^"]*)"', line)
                    if match:
                        return True
            file.seek(0, os.SEEK_END) # ensure we are at the end of the file
            if lines and not lines[-1].endswith('\n'):
                file.write('\n')
            file.write("SCB_GAMESCOPE_ARGS=\"\"\n")
            return True

