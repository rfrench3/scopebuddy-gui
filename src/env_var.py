import sys
import os
sys.path.insert(0, "/app/share/scopebuddygui") # flatpak path

from PySide6.QtWidgets import QToolButton, QLineEdit, QCheckBox, QWidget
import file_manager as fman

entry:str = fman.ui_env_vars_entry

class EnvVarLogic:
    def __init__(self, parent_widget=None, file=None) -> None:
            self.parent_logic = None  # Will be set by main.py
            self.entries = []  # Store references to all entry widgets
            self.file = file
            self.env_vars_list = parent_widget.findChild(QWidget, 'additional_entries')  # type: ignore

            print(f"ENV VAR FILE RECIEVED: {file}")

            # Initialize and connect inputs
            self.add_entry = parent_widget.findChild(QToolButton, 'add_entry')  # type: ignore
            self.noscope_checkbox = parent_widget.findChild(QCheckBox, 'scb_noscope')  # type: ignore
            
            self.add_entry.clicked.connect(self.new_entry)
            # Start the field with one blank entry
            self.new_entry()

    # Contained to this window

    def new_entry(self) -> None:
        """Creates a new entry in the environment variables list."""
        new_entry = fman.load_widget(entry)
        layout = self.env_vars_list.layout()
        layout.addWidget(new_entry)
        
        # Find and store references to the widgets
        variable_line = new_entry.findChild(QLineEdit, 'variable_line')
        delete_entry = new_entry.findChild(QToolButton, 'delete_entry')
        
        # Store the entry data for later access
        entry_data = {
            'widget': new_entry,
            'variable_line': variable_line,
            'delete_entry': delete_entry
        }
        self.entries.append(entry_data)
        
        # Connect the delete button to remove this entry
        if delete_entry:
            delete_entry.clicked.connect(lambda: self.remove_entry(entry_data))
    
    def remove_entry(self, entry_data):
        """Remove an entry from the list."""

        layout = self.env_vars_list.layout()
        layout.removeWidget(entry_data['widget'])
        
        # Delete the widget
        entry_data['widget'].deleteLater() # prevent memory leak
        
        # Remove from our list
        self.entries.remove(entry_data)

    def return_env_vars_list(self) -> list:
        vars_list = []
        
        if self.noscope_checkbox.isChecked:
            vars_list.append("SCB_NOSCOPE=1")

        for entry_data in self.entries:
            variable_line = entry_data['variable_line']
            if variable_line and variable_line.text().strip():  # Only include non-empty entries
                vars_list.append(variable_line.text().strip())

        return vars_list
    
    def load_data(self, data:str) -> None:
        """Loads the data from the file into the UI elements."""
        pass
