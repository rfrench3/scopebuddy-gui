import sys
import os
sys.path.insert(0, "/app/share/scopebuddygui") # flatpak path

import file_manager as fman

from PySide6.QtWidgets import QWidget, QPushButton, QListWidget, QPushButton
from PySide6.QtWidgets import QDialog, QVBoxLayout
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

DATA_DIR = fman.DATA_DIR
dialog_new_file = os.path.join(DATA_DIR, "dialog_new_file.ui")

class WelcomeLogic:
    def __init__(self, parent_widget=None) -> None:
            self.parent_logic = None  # Will be set by main.py

            # Manually initialize and connect inputs  (type: ignore comments prevent pyLance false positives)
            self.button_new_config = parent_widget.findChild(QPushButton, 'button_new_config')  # type: ignore
            self.file_list = parent_widget.findChild(QListWidget, 'file_list')  # type: ignore

            self.button_new_config.clicked.connect(self.new_config_pressed)
            self.file_list.itemClicked.connect(self.list_clicked)

    # Contained to this window

    def new_config_pressed(self) -> None:
        """opens a modal that has the user create a new config with a Steam AppID."""

        dialog:QDialog = fman.load_widget(dialog_new_file)
        dialog.show()
        dialog.exec()
        # end of QDialog
        
        print('press')
        pass

    # Calls the main window
    
    def list_clicked(self) -> None:
        """opens the config file the user clicked."""
        item = self.file_list.currentItem()
        if item:
            print("List item clicked:", item.text())
        if self.parent_logic:
            self.parent_logic.load_selected_file(item.text())
