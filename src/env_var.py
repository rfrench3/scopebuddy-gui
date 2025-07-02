import sys
import os
sys.path.insert(0, "/app/share/scopebuddygui") # flatpak path

from PySide6.QtWidgets import QToolButton, QLineEdit, QScrollArea, QVBoxLayout, QWidget
import file_manager as fman

entry:str = fman.ui_env_vars_entry

class EnvVarLogic:
    def __init__(self, parent_widget=None) -> None:
            self.parent_logic = None  # Will be set by main.py
            self.entries = []  # Store references to all entry widgets

            # Initialize and connect inputs  (type: ignore comments prevent pyLance false positives)
            self.add_entry = parent_widget.findChild(QToolButton, 'add_entry')  # type: ignore
            self.env_vars_list = parent_widget.findChild(QWidget, 'additional_entries')  # type: ignore
            
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
        entry_data['widget'].deleteLater()
        
        # Remove from our list
        self.entries.remove(entry_data)

    # Calls the main window
    
    def func2(self) -> None:
        """."""
        pass