from PySide6.QtWidgets import QLineEdit, QCheckBox, QPushButton, QDialogButtonBox
import file_manager as fman
from file_manager import ConfigFile

class GeneralSettingsLogic:
    def __init__(self, file:ConfigFile, parent_widget=None) -> None:
            self.parent_logic = None  # Will be set by main.py
            self.entries = []  # Store references to all entry widgets
            self.file = file

            # Initialize and connect inputs
            self.display_name = parent_widget.findChild(QLineEdit, 'display_name')  # type: ignore
            self.scb_noscope = parent_widget.findChild(QCheckBox, 'scb_noscope')  # type: ignore
            self.scb_auto_flags = parent_widget.findChild(QCheckBox, 'scb_auto_flags')  # type: ignore
            self.deactivate_file = parent_widget.findChild(QCheckBox, 'deactivate_file')  # type: ignore
            self.delete_file = parent_widget.findChild(QPushButton, 'delete_file')  # type: ignore
            self.button_box = parent_widget.findChild(QDialogButtonBox, 'buttonBox')  # type: ignore
            self.apply_button = self.button_box.button(QDialogButtonBox.StandardButton.Apply) # type: ignore
            
            
            self.apply_button.clicked.connect(self.save_data)
            self.delete_file.clicked.connect(self.erase_data)
            

            # Load lines from the file
            self.load_data(self.file)
    
    def load_data(self,file:ConfigFile) -> None:
        pass

        #TODO: deactivate_file needs to set NOSCOPE to 1 and comment out everything
            
    def erase_data(self):
        pass

    def save_data(self):
        pass    
        

    