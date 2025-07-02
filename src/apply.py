import sys
import os
sys.path.insert(0, "/app/share/scopebuddygui") # flatpak path

from PySide6.QtWidgets import QLineEdit
from file_manager import ConfigFile

class ApplyChangesLogic:
    def __init__(self, file:ConfigFile, parent_widget=None) -> None:
            self.parent_logic = None  # Will be set by main.py
            self.file = file  # Store the file path

            # Initialize and connect inputs  (type: ignore comments prevent pyLance false positives)
            #self. = parent_widget.findChild(Q, '')  # type: ignore


    def load_data(self, data:str) -> None:
        """Loads the data from the file into the UI elements."""
        pass