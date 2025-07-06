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
            #self.deactivate_file = parent_widget.findChild(QCheckBox, 'deactivate_file')  # Removed to reduce complexity   # type: ignore
            self.delete_file = parent_widget.findChild(QPushButton, 'delete_file')  # type: ignore
            self.button_box = parent_widget.findChild(QDialogButtonBox, 'buttonBox')  # type: ignore
            self.apply_button = self.button_box.button(QDialogButtonBox.StandardButton.Apply) # type: ignore
            
            
            self.apply_button.clicked.connect(self.save_data)
            self.delete_file.clicked.connect(self.erase_data)
            

            # Load lines from the file
            self.load_data()
    
    def load_data(self) -> None:
        """Loads data from the file into the interface."""
        self.display_name.setText(self.file.print_displayname())

        if self.file.print_path() == fman.GLOBAL_CONFIG:
            self.display_name.setDisabled(True)

        if self.file.check_for_exact_line("SCB_NOSCOPE=1"):
            self.scb_noscope.setChecked(True)

        if self.file.check_for_exact_line("SCB_AUTO_"):
            self.scb_auto_flags.setChecked(True)
        
        

            
    def erase_data(self):
        pass

    def save_data(self):
        """Saves data from each of the elements into the file."""

        if self.file.print_displayname() != self.display_name.text():
            self.file.edit_displayname(self.display_name.text())
            #TODO: update file selector screen with new displayname 

        # Update all elements that don't get their own function at the same time
        lines_to_change = {}
        

        # if noscope needs to be removed:
        if (not self.scb_noscope.isChecked()) and self.file.check_for_exact_line("SCB_NOSCOPE=1"):
            lines_to_change["SCB_NOSCOPE=1"] = "#SCB_NOSCOPE=1"

        # if noscope needs to be added:
        if self.scb_noscope.isChecked() and (not self.file.check_for_exact_line("SCB_NOSCOPE=1")):
            lines_to_change["#SCB_NOSCOPE=1"] = "SCB_NOSCOPE=1"


        # if scb_autos need to be removed:
        if (not self.scb_auto_flags.isChecked()) and self.file.check_for_exact_line("SCB_AUTO"):
            lines_to_change["SCB_AUTO_RES=1"] = "#SCB_AUTO_RES=1"
            lines_to_change["SCB_AUTO_HDR=1"] = "#SCB_AUTO_HDR=1"
            lines_to_change["SCB_AUTO_VRR=1"] = "#SCB_AUTO_VRR=1"

        # if scb_autos need to be added:
        if self.scb_auto_flags.isChecked() and (not self.file.check_for_exact_line("SCB_AUTO")):
            lines_to_change["#SCB_AUTO_RES=1"] = "SCB_AUTO_RES=1"
            lines_to_change["#SCB_AUTO_HDR=1"] = "SCB_AUTO_HDR=1"
            lines_to_change["#SCB_AUTO_VRR=1"] = "SCB_AUTO_VRR=1"
            
        list_current = []
        list_new = []

        for key, value in lines_to_change.items():
            list_current.append(key)
            list_new.append(value)

        self.file.edit_exact_lines(list_current,list_new)
            

        
        

    