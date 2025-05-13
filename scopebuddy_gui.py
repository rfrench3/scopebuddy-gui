#PySide6, Qt Designer UI files
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtGui import QIntValidator
from ui_mainwindow import Ui_MainWindow  # Import generated UI file
from ui_about import Ui_Dialog_About  # Import generated UI file
from ui_apply_confirmation import Ui_Dialog_Apply

# non-GUI imports
import sys  
import os
from re import search # for searching for gamescope args in the config file



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("ScopeBuddy GUI")  # Set the window title
        self.ui.variable_displayGamescope.setText('Current Gamescope Config: ' + self.get_gamescope_args()) #display the current gamescope args

        # Button actions
        self.ui.pushButton_apply.clicked.connect(self.apply_clicked)
        self.ui.pushButton_exit.clicked.connect(self.exit_app)
        self.ui.pushButton_about.clicked.connect(self.open_about_dialog)

        self.ui.lineEdit_oHeight.setValidator(QIntValidator()) # ensures valid inputs
        self.ui.lineEdit_rHeight.setValidator(QIntValidator()) # input fields are also limited to 
        self.ui.lineEdit_oWidth.setValidator(QIntValidator())  # 4 digits in Qt Designer to ensure sane configs
        self.ui.lineEdit_rWidth.setValidator(QIntValidator())
        self.ui.lineEdit_fps.setValidator(QIntValidator())

    def get_gamescope_args(self) -> str: #search for the config file, return args if it exists
        # Check if the config file exists
        if not os.path.exists(os.path.expanduser('~/.config/scopebuddy/scb.conf')):
            print("Config file does not exist.")
            return None #TODO: make it create the file if it doesn't exist, particularly important for game-specific configs

        # The file does exist, so read it and return the gamescope arguments
        with open(os.path.expanduser('~/.config/scopebuddy/scb.conf'), 'r') as file: #read-only mode, this part does not write to the file
            lines = file.readlines()
            for line in lines:
                if line.startswith('SCB_GAMESCOPE_ARGS='):
                    match = search(r'SCB_GAMESCOPE_ARGS="([^"]*)"', line)
                    if match:
                        return match.group(1)
                    else:
                        print("No SCB_GAMESCOPE_ARGS found in the config file.")
                        return None #TODO: make it add a line for the args
        

    def generate_new_config(self) -> str: #output a new config string based on the user input
        self.config_list = []

        def apply_lineEdit_input(lineEdit, arg):
            if lineEdit.text().isdigit():
                self.config_list.append(str(arg + ' ' + lineEdit.text() + ' '))
            
        def apply_checkbox_input(checkBox, arg): #appends checkbox input to the config list
            if checkBox.isChecked():
                self.config_list.append(str(arg + ' '))

        # IMPLEMENTED ARGUMENTS
        # TODO: implement more
        apply_checkbox_input(self.ui.checkBox_mango,'--mangoapp') 
        apply_lineEdit_input(self.ui.lineEdit_rHeight,'-h')
        apply_lineEdit_input(self.ui.lineEdit_rWidth,'-w')
        apply_lineEdit_input(self.ui.lineEdit_fps,'-r')
        apply_checkbox_input(self.ui.checkBox_fullscreen,'-f')
        apply_lineEdit_input(self.ui.lineEdit_oHeight,'-H')
        apply_lineEdit_input(self.ui.lineEdit_oWidth,'-W')
        apply_checkbox_input(self.ui.checkBox_steam,'-s')
        
        generated_config = ''
        for argument in self.config_list:
            generated_config += argument
        
        print(f'The generated config file is {generated_config}')
        return generated_config

    def apply_global_config(self):
        # set the config
        the_config = self.generate_new_config()

        # Open the config file
        with open(os.path.expanduser('~/.config/scopebuddy/scb.conf'), 'r') as file:
            lines = file.readlines()

            # Find the line that starts with SCB_GAMESCOPE_ARGS
            for i, line in enumerate(lines):
                if line.startswith('SCB_GAMESCOPE_ARGS'):
                    # Comment out the original line
                    commented_line = f"# commented out by scopebuddy-gui: {line}"
                    # Create the new line
                    new_line = f'SCB_GAMESCOPE_ARGS="{the_config}"\n'
                    # Replace with the commented + new line
                    lines[i:i+1] = [commented_line, new_line]
                    break

            # Write the modified lines back to the file
            with open(os.path.expanduser('~/.config/scopebuddy/scb.conf'), 'w') as file:
                file.writelines(lines)

        self.ui.variable_displayGamescope.setText('Current Gamescope Config: ' + self.get_gamescope_args()) #display updated config

    # ON-CLICK METHODS

    def apply_clicked(self):
        print("Apply button clicked...")
        #TODO: ensure the set of inputs is valid (-h cant be empty unless -w is empty, etc.)
        dialog = DialogApply()
        dialog.exec()
        if dialog.answer:
            print('Applying changes...')
            self.apply_global_config()

    def exit_app(self):
        print("Exiting application...")
        sys.exit()

    def open_about_dialog(self):
        print("Opening about dialog...")
        dialog = DialogAbout()
        result = dialog.exec() #TODO: popup can go behind the main window, while blocking inputs on the main window...


class DialogAbout(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog_About()
        self.ui.setupUi(self)
        self.setWindowTitle("About ScopeBuddy GUI")  # Set the window title
        self.ui.pushButton_okay.clicked.connect(self.exit_app)
    
    def exit_app(self):
        self.close()

class DialogApply(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog_Apply()
        self.ui.setupUi(self)
        self.setWindowTitle("Apply Changes?")  # Set the window title
        self.ui.var_currentConfig.setText(MainWindow.get_gamescope_args(window))
        self.ui.var_newConfig.setText(MainWindow.generate_new_config(window))

        #button actions
        self.ui.pushButton_Cancel.clicked.connect(self.exit_window)
        self.ui.pushButton_Apply.clicked.connect(self.apply_changes)
        self.answer = False #changes will not be applied unless explictly confirmed
    
    def exit_window(self):
        self.close()
    
    def apply_changes(self):
        self.answer = True #changes have been explicitly confirmed
        self.close()




app = QApplication([])
window = MainWindow()
window.show()
app.exec()

