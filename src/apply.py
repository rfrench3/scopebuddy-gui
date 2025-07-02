import sys
import os
sys.path.insert(0, "/app/share/scopebuddygui") # flatpak path

from PySide6.QtWidgets import QLineEdit
import file_manager as fman

class ApplyChangesLogic:
    def __init__(self, parent_widget=None) -> None:
            self.parent_logic = None  # Will be set by main.py

            # Initialize and connect inputs  (type: ignore comments prevent pyLance false positives)
            #self. = parent_widget.findChild(Q, '')  # type: ignore


            

    # Contained to this window

    def func(self) -> None:
        """."""
        print('pressed')
        pass

    # Calls the main window
    
    def func2(self) -> None:
        """."""
        pass