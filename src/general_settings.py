from PySide6.QtWidgets import QToolButton, QLineEdit, QCheckBox, QWidget
import file_manager as fman
from file_manager import ConfigFile

class GeneralSettingsLogic:
    def __init__(self, file:ConfigFile, parent_widget=None) -> None:
            self.parent_logic = None  # Will be set by main.py
            self.entries = []  # Store references to all entry widgets
            self.file = file

            # Initialize and connect inputs
            
            
            
            

            # Load lines from the file
            self.load_data(self.file)
    
    def load_data(self,file:ConfigFile) -> None:
        pass

        #TODO: deactivate_file needs to set NOSCOPE to 1 and comment out everything
            
            

    