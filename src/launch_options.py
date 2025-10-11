import sys
import os
sys.path.insert(0, "/app/share/scopebuddygui") # flatpak path

from PySide6.QtWidgets import QLineEdit, QDialogButtonBox, QMessageBox
import file_manager as fman
from file_manager import ConfigFile
import shared_data

entry:str = fman.ui_launch_options_entry

class LaunchOptionsLogic:
    def __init__(self, file:ConfigFile, parent_widget=None) -> None:
            self.initialized = False
            self.parent_logic = None  # Will be set by main.py
            self.file = file
            self.parent_widget = parent_widget

            # Initialize and connect inputs
            self.line_edit = parent_widget.findChild(QLineEdit, 'lineEdit') # type: ignore
            self.button_box = parent_widget.findChild(QDialogButtonBox, 'buttonBox')  # type: ignore

            self.apply_button = self.button_box.button(QDialogButtonBox.StandardButton.Apply) # type: ignore
            self.help_button = self.button_box.button(QDialogButtonBox.StandardButton.Help) # type: ignore

            self.apply_button.clicked.connect(self.save_data)
            self.help_button.clicked.connect(lambda: os.system("xdg-open https://help.steampowered.com/en/faqs/view/7D01-D2DD-D75E-2955"))
            self.line_edit.textChanged.connect(self.data_changed)

            # Load line from the file
            self.load_data()
            self.saved_data = self.file.print_launch_options().strip()

            self.apply_button.setEnabled(False)
            self.initialized = True

    def data_changed(self) -> None:
        """When the user has inputted data, compare it to the saved data
          and enable/disable the apply button based on that."""
        if not self.initialized:
            return

        if (
            self.saved_data == self.line_edit.text().strip()
            ):
            self.apply_button.setEnabled(False)
            shared_data.unsaved_changes = False
            return

        shared_data.unsaved_changes = True
        self.apply_button.setEnabled(True)

    def load_data(self) -> None:
        """Loads the data from the file into the UI elements."""

        argument = self.file.print_launch_options().strip()
        self.line_edit.setText(argument)
        
    def save_data(self) -> bool:
        """Save the user input to the file's command+=' ' line."""
        new_line = f' {self.line_edit.text().strip()}'
        self.file.edit_launch_options(new_line)

        self.saved_data = self.line_edit.text().strip()
        self.apply_button.setEnabled(False)
        shared_data.unsaved_changes = False
        return False



