# This file contains functions for the scopebuddy-gui application.
# They are here because some of them are extremely long and would clutter the main file.

import sys
sys.path.insert(0, "/app/share/scopebuddygui") # flatpak path

import os
from re import search # for searching for gamescope args in the config file
import subprocess # for finding gamescope and scopebuddy

scbpath = os.path.expanduser('~/.config/scopebuddy/scb.conf')

def verify_dependencies_present(programs:list) -> bool:
    # Check if the required dependencies are installed
    for program in programs:
        if not locate_dependency(program):
            return False
    return True #false if any program is not found, true otherwise

def locate_dependency(program: str) -> str | None:
    # return path to program if it exists, None if it doesn't. for determining if gamescope/scopebuddy are installed
    try:
        result = subprocess.run(
            ["flatpak-spawn", "--host", "which", program],
            capture_output=True,
            text=True,
            check=True
        )
        path = result.stdout.strip()
        if path:
            print(f"{program} found at: {path}")
            return path
        else:
            print(f"{program} not found.")
            return None
    except subprocess.CalledProcessError:
        print(f"{program} not found or 'which' failed.")
        return None

class Mixins: 
    def ensure_valid_args(self) -> tuple:
        #TODO: Before adding more checks, make a general function for checking
        if self.ui.lineEdit_rHeight.text() == '' and self.ui.lineEdit_rWidth.text() != '':
            print("Invalid arguments: -h is empty, but -w is not.")
            return (False,'-w','-h')
        
        if self.ui.lineEdit_oHeight.text() == '' and self.ui.lineEdit_oWidth.text() != '':
            print("Invalid arguments: -H is empty, but -W is not.")
            return (False,'-W','-H')
        
        return (True,) #nothing went wrong

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

        self.ui.variable_displayGamescope.setText(f'Current Gamescope Config: {self.read_gamescope_args()}') #display updated config

    def generate_new_config(self) -> str: #output a new config string based on the user input
        self.config_list = []

        def apply_lineEdit_input(lineEdit:int, arg):
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
                else:
                    raise NotImplementedError(f"Widget type '{widget_type}' is not implemented.")
                
        # IMPLEMENTED ARGUMENTS
        self.settings = [
            ('checkbox', self.ui.checkBox_mango, '--mangoapp'),
            ('lineEdit', self.ui.lineEdit_rHeight, '-h'),
            ('lineEdit', self.ui.lineEdit_rWidth, '-w'),
            ('lineEdit', self.ui.lineEdit_fps, '-r'),
            ('checkbox', self.ui.checkBox_fullscreen, '-f'),
            ('checkbox', self.ui.checkBox_borderless, '-b'),
            ('lineEdit', self.ui.lineEdit_oHeight, '-H'),
            ('lineEdit', self.ui.lineEdit_oWidth, '-W'),
            ('checkbox', self.ui.checkBox_steam, '-e'),
            ('checkbox', self.ui.checkBox_hdr, '--hdr-enabled'),
            ('lineEdit', self.ui.lineEdit_maxScaleFactor, '-m'),
            ('comboBox', self.ui.comboBox_upscalerType, '-S'),
            ('comboBox', self.ui.comboBox_upscalerFilter, '-F'),
            ('lineEdit', self.ui.lineEdit_upscalerSharpness, '--sharpness'),
            ('doubleSpinBox', self.ui.doubleSpinBox_mouseSensitivity, '-s'),
            ('checkbox', self.ui.checkBox_adaptiveSync, '--adaptive-sync'),
            ('checkbox', self.ui.checkBox_forceInternalFullscreen, '--force-windows-fullscreen'),
            ]
        
        compile_arguments(self.settings)


        generated_config = ''
        for argument in self.config_list:
            generated_config += argument
        
        print(f'The generated config file is {generated_config}')
        return generated_config
    
    def apply_current_to_ui(self): #checks current config, applies it to the UI

        def set_lineEdit_input(lineEdit:int, arg):
            args = self.read_gamescope_args()
            match = search(rf'{arg} (\d+)', args)
            if match:
                lineEdit.setText(match.group(1))
            
        def set_combobox_input(comboBox, arg): #appends combobox input to the config list (unless default)
            args = self.read_gamescope_args()
            match = search(rf'{arg} (\d+)', args)
            if match:
                return match.group(1)

        def set_checkbox_input(checkBox, arg): #appends checkbox input to the config list 
            checkBox.setChecked(arg in self.read_gamescope_args()) # set checkbox state based on config

        def set_doubleSpinBox_input(doubleSpinBox, arg): #preferred for float values
            args = self.read_gamescope_args()
            match = search(rf'{arg} ([\d.]+)', args)
            if match:
                doubleSpinBox.setValue(match.group(1))
  

        def set_arguments(settings):
            for widget_type, input_widget, arg in settings:
                if widget_type == 'checkbox':
                    set_checkbox_input(input_widget, arg)
                elif widget_type == 'lineEdit':
                    set_lineEdit_input(input_widget, arg)
                elif widget_type == 'comboBox':
                    set_combobox_input(input_widget, arg)
                elif widget_type == 'doubleSpinBox':
                    set_doubleSpinBox_input(input_widget, arg)
                else:
                    raise NotImplementedError(f"Widget type '{widget_type}' is not implemented.")
        
        # IMPLEMENTED ARGUMENTS
        self.settings = [
            ('checkbox', self.ui.checkBox_mango, '--mangoapp'),
            ('lineEdit', self.ui.lineEdit_rHeight, '-h'),
            ('lineEdit', self.ui.lineEdit_rWidth, '-w'),
            ('lineEdit', self.ui.lineEdit_fps, '-r'),
            ('checkbox', self.ui.checkBox_fullscreen, '-f'),
            ('checkbox', self.ui.checkBox_borderless, '-b'),
            ('lineEdit', self.ui.lineEdit_oHeight, '-H'),
            ('lineEdit', self.ui.lineEdit_oWidth, '-W'),
            ('checkbox', self.ui.checkBox_steam, '-e'),
            ('checkbox', self.ui.checkBox_hdr, '--hdr-enabled'),
            ('lineEdit', self.ui.lineEdit_maxScaleFactor, '-m'),
            ('comboBox', self.ui.comboBox_upscalerType, '-S'),
            ('comboBox', self.ui.comboBox_upscalerFilter, '-F'),
            ('lineEdit', self.ui.lineEdit_upscalerSharpness, '--sharpness'),
            ('doubleSpinBox', self.ui.doubleSpinBox_mouseSensitivity, '-s'),
            ('checkbox', self.ui.checkBox_adaptiveSync, '--adaptive-sync'),
            ('checkbox', self.ui.checkBox_forceInternalFullscreen, '--force-windows-fullscreen'),
            ]
        

        set_arguments(self.settings) # apply the current config to the UI elements

        #pass#TODO: apply current config to the UI elements
        self.ui.checkBox_mango.setChecked('--mangoapp' in self.read_gamescope_args()) # set checkbox state based on config
        self.ui.lineEdit_rHeight
        self.ui.lineEdit_rWidth
        self.ui.lineEdit_fps
        self.ui.checkBox_fullscreen.setChecked('-f' in self.read_gamescope_args())
        self.ui.checkBox_borderless.setChecked('-b' in self.read_gamescope_args())
        self.ui.lineEdit_oHeight
        self.ui.lineEdit_oWidth
        self.ui.checkBox_steam.setChecked('-e' in self.read_gamescope_args())
        self.ui.checkBox_hdr.setChecked('--hdr-enabled' in self.read_gamescope_args())
        self.ui.lineEdit_maxScaleFactor
        self.ui.comboBox_upscalerType
        self.ui.comboBox_upscalerFilter
        self.ui.lineEdit_upscalerSharpness
        self.ui.doubleSpinBox_mouseSensitivity
        self.ui.checkBox_adaptiveSync.setChecked('--adaptive-sync' in self.read_gamescope_args())
        self.ui.checkBox_forceInternalFullscreen.setChecked('--force-windows-fullscreen' in self.read_gamescope_args())


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
        
    def create_config_path(self) -> bool: #create .config/scopebuddy, return True if successful
        if os.path.exists(scbpath):
            return True
        print('config file does not exist, checking for Gamescope and Scopebuddy...')
        if not verify_dependencies_present(['gamescope', 'scopebuddy']):
            print('Gamescope or ScopeBuddy not found, unable to create config file.')
            return False
        print("dependencies present, generating default file...")
        
        try: #generates new config file with default values
            os.makedirs(os.path.dirname(scbpath), exist_ok=True)
            with open(scbpath,'w') as file:
                # Create scopebuddy's default file (TODO: must be manually updated if ScopeBuddy changes)
                file.write("# This is the config file that let's you assign defaults for gamescope when using the scopebuddy script\n")
                file.write("# lines starting with # are ignored\n")
                file.write("# Conf files matching the games Steam AppID stored in ~/.conf/scopebuddy/AppID/ will be sourced after\n")
                file.write("# ~/.config/scopebuddy/scb.conf or whichever file you specify with SCB_CONF=someotherfile.conf env var in the launch options.\n")
                file.write("# \n")
                file.write("# Example for always exporting specific environment variables for gamescope\n")
                file.write("#export XKB_DEFAULT_LAYOUT=no\n")
                file.write("#export MANGOHUD_CONFIG=preset=2\n")
                file.write("#\n")
                file.write("# Example for providing default gamescope arguments through scopebuddy if no arguments are given to the scopebuddy script, this does not need to be exported.\n")
                file.write("# To not use this default set of arguments, just launch scb with SCB_NOSCOPE=1 or just add any gamescope argument before the '-- %command%' then this variable will be ignored\n")
                file.write("#SCB_GAMESCOPE_ARGS=\"--mangoapp -f -w 2560 -h 1440 -W 2560 -H 1440 -r 180 --force-grab-cursor --hdr-enabled -e\"\n")
                file.write("#\n")
                file.write("# To auto-detect KDE display width, height, refresh, VRR and HDR states, you can use SCB_AUTO_* {RES|HDR|VRR}\n")
                file.write("# These vars will override any previously set values for -W and -H or append --hdr-enabled and --adaptive-sync\n")
                file.write("# automatically depending on the current settings for your active display, or the display chosen with -O /\n")
                file.write("# --prefer-output flags in gamescsope.\n")
                file.write("#SCB_AUTO_RES=1\n")
                file.write("#SCB_AUTO_HDR=1\n")
                file.write("#SCB_AUTO_VRR=1\n")
                file.write("# To debug scopebuddy output, uncomment the following line. After launching games, the executed cmd will be output to ~/.config/scopebuddy/scopebuddy.log\n")
                file.write("#SCB_DEBUG=1\n")
                file.write("###\n")
                file.write("## FOR ADVANCED USE INSIDE AN APPID CONFIG\n")
                file.write("###\n")
                file.write("# The config files are treated as a bash script by scopebuddy, this means you can use bash to do simple tasks before the game runs\n")
                file.write("# or you can check which mode scopebuddy is running in and apply settings accordingly, below are some handy variables for scripting.\n")
                file.write("# $SCB_NOSCOPE will be set to 1 if we are running in no gamescope mode\n")
                file.write("# $SCB_GAMEMODE will be set to 1 if we are running inside steam gamemode (which means SCB_NOSCOPE will also be set to 1 due to nested gamescope not working in gamemode)\n")
                file.write("# $command will contain everything steam expanded %command% into\n")
        except OSError as e:
            print(f"Error creating config file: {e}")
            return False
        return True

    def make_gamescope_line(self) -> bool: #if config file doesn't have the gamescope args line, create one
        if not self.create_config_path(): # runs the function and detects if it fails
            raise FileNotFoundError("Config file or location creation failed.")
        # The file does exist, so read it and return the gamescope arguments
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
        
