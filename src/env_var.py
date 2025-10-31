import sys
import os
sys.path.insert(0, "/app/share/scopebuddygui") # flatpak path

from PySide6.QtWidgets import QToolButton, QLineEdit, QWidget, QDialogButtonBox, QMessageBox
import file_manager as fman
from file_manager import ConfigFile
import shared_data

entry:str = fman.ui_env_vars_entry

class EnvVarLogic:
    def __init__(self, file:ConfigFile, parent_widget=None) -> None:
            self.initialized = False

            self.parent_logic = None  # Will be set by main.py
            self.entries = []  # Store references to all entry widgets
            self.file = file
            self.env_vars_list = parent_widget.findChild(QWidget, 'additional_entries')  # type: ignore
            self.parent_widget = parent_widget

            # Initialize and connect inputs
            self.add_entry = parent_widget.findChild(QToolButton, 'add_entry')  # type: ignore
            self.button_box = parent_widget.findChild(QDialogButtonBox, 'buttonBox')  # type: ignore

            self.apply_button = self.button_box.button(QDialogButtonBox.StandardButton.Apply) # type: ignore
            self.help_button = self.button_box.button(QDialogButtonBox.StandardButton.Help) # type: ignore
            self.reset_button = self.button_box.button(QDialogButtonBox.StandardButton.Reset) # type: ignore
            self.defaults_button = self.button_box.button(QDialogButtonBox.StandardButton.RestoreDefaults) # type: ignore
            
            self.add_entry.clicked.connect(self.new_entry)
            self.apply_button.clicked.connect(self.save_data)
            self.help_button.clicked.connect(lambda: os.system("xdg-open https://rfrench3.github.io/scopebuddy-gui/#environment_variables"))

            # Load lines from the file
            
            self.load_data()
            

            # Start the field with one blank entry
            self.new_entry()

            # checks against saved_data should only begin once everything is initialized
            self.saved_data:list[str] = self.file.print_export_lines()

            self.apply_button.setEnabled(False)
            self.initialized = True

    def data_changed(self) -> None:
        """When the user has inputted data, compare it to the saved data
          and enable/disable the apply button based on that."""
        if not self.initialized:
            return

        if (
            self.saved_data == self.return_env_vars_list()
            ):
            self.apply_button.setEnabled(False)
            shared_data.unsaved_changes = False
            return

        shared_data.unsaved_changes = True
        self.apply_button.setEnabled(True)

    def load_data(self) -> None:
        """Loads the data from the file into the UI elements."""
        variables_list:list[str] = self.file.print_export_lines()

        for entry in variables_list:
            self.new_entry(entry)

    def save_data(self) -> bool:
        """Load data into a list and apply it to the file."""
        data:list[str] = self.return_env_vars_list()

        parent_window = self.parent_widget.window() if self.parent_widget else None

        # Ensure user is warned if they are combining regular mangohud with gamescope
        adding_noscope:bool = False
        adding_mangohud:bool = False
        for variable in data:
            if variable.startswith("mangohud") or variable.startswith("MANGOHUD=1"):
                adding_mangohud = True
            if variable.startswith("SCB_NOSCOPE=1"):
                adding_noscope = True

            if adding_noscope and adding_mangohud:
                break # both have already been located

        gamescope_active:bool = False if (
            self.file.check_for_exact_line("SCB_NOSCOPE=1") or 
            self.file.check_for_exact_line("export SCB_NOSCOPE=1") or
            adding_noscope
            ) else True

        if gamescope_active and adding_mangohud:
            result = fman.load_message_box(
                parent_window,
                "Warning!",
                ("You have gamescope enabled and are attempting to use regular MangoHUD! This is not supported.\n"
                "You should either disable Gamescope or use the \"MangoHUD Overlay\" checkbox inside of Gamescope!"),
                QMessageBox.Icon.Warning,
                QMessageBox.StandardButton.Ignore | QMessageBox.StandardButton.Cancel
            )
            if result != QMessageBox.StandardButton.Ignore:
                return True
            
        self.apply_button.setEnabled(False)

        self.file.edit_export_lines(data)

        self.saved_data:list[str] = self.file.print_export_lines()
        shared_data.unsaved_changes = False
        return False


    def new_entry(self, data:str|None = None) -> None:
        """Creates a new entry in the environment variables list."""
        new_entry = fman.load_widget(entry)
        layout = self.env_vars_list.layout()
        layout.addWidget(new_entry)
        
        # Find and store references to the widgets
        variable_line = new_entry.findChild(QLineEdit, 'variable_line')
        delete_entry = new_entry.findChild(QToolButton, 'delete_entry')

        variable_line.textChanged.connect(self.data_changed) #type:ignore
        #delete_entry.clicked.connect(self.data_changed) #type:ignore
        
        # Put file's variables into entry
        if data:
            variable_line.setText(data) # type: ignore

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
    
    def remove_entry(self, entry_data) -> None:
        """Remove an entry from the list."""

        layout = self.env_vars_list.layout()
        layout.removeWidget(entry_data['widget'])
        
        # Delete the widget
        entry_data['widget'].deleteLater() # prevent memory leak
        
        # Remove from our list
        self.entries.remove(entry_data)
        self.data_changed()

    def return_env_vars_list(self) -> list[str]:
        """Outputs a list of environment variables input by the user.
        Ignores entries that are blank, and strips beginning/ending spaces."""
        vars_list = []

        for entry_data in self.entries:
            variable_line = entry_data['variable_line']
            if variable_line and variable_line.text().strip():  # Only include non-empty entries
                vars_list.append(variable_line.text().strip())

        return vars_list
    
    
