from PySide6.QtWidgets import QLineEdit, QCheckBox, QDialogButtonBox, QMessageBox
import file_manager as fman
from file_manager import ConfigFile
import shared_data

class GeneralSettingsLogic:
    def __init__(self, file:ConfigFile, parent_widget=None) -> None:
            self.parent_logic = None  # Will be set by main.py
            self.entries = []  # Store references to all entry widgets
            self.file = file
            self.parent_widget = parent_widget

            # Initialize and connect inputs
            self.display_name = parent_widget.findChild(QLineEdit, 'display_name')  # type: ignore
            self.scb_noscope = parent_widget.findChild(QCheckBox, 'scb_noscope')  # type: ignore
            self.scb_auto_flags = parent_widget.findChild(QCheckBox, 'scb_auto_flags')  # type: ignore
            self.button_box = parent_widget.findChild(QDialogButtonBox, 'buttonBox')  # type: ignore
            self.apply_button = self.button_box.button(QDialogButtonBox.StandardButton.Apply) # type: ignore

            self.apply_button.clicked.connect(self.save_data)
    
            # Load lines from the file
            self.load_data()

            self.data = {
                'name': self.display_name.text(),
                'noscope': self.scb_noscope.isChecked(),
                'autos': self.scb_auto_flags.isChecked()
            }

            self.display_name.textChanged.connect(self.data_changed)
            self.scb_noscope.stateChanged.connect(self.data_changed)
            self.scb_auto_flags.stateChanged.connect(self.data_changed)

            self.apply_button.setDisabled(True)

    def data_changed(self) -> None:
        """When the user has inputted data, compare it to the saved data
          and enable/disable the apply button based on that."""

        if (
            self.data['name'] == self.display_name.text() and
            self.data['noscope'] == self.scb_noscope.isChecked() and
            self.data['autos'] == self.scb_auto_flags.isChecked()
            ):
            self.apply_button.setEnabled(False)
            shared_data.unsaved_changes = False
            return

        shared_data.unsaved_changes = True
        self.apply_button.setEnabled(True)
        
    
    def load_data(self) -> None:
        """Loads data from the file into the interface."""
        self.display_name.setText(self.file.print_displayname())


        if self.file.print_path() == fman.GLOBAL_CONFIG:
            self.display_name.setDisabled(True)

        if self.file.check_for_exact_line("SCB_NOSCOPE=1"):
            self.scb_noscope.setChecked(True)


        if self.file.check_for_exact_line("SCB_AUTO_"):
            self.scb_auto_flags.setChecked(True)

        

    def save_data(self) -> bool:
        """Saves data from each of the elements into the file."""

        parent_window = self.parent_widget.window() if self.parent_widget else None


        if self.file.print_displayname() != self.display_name.text():
            self.file.edit_displayname(self.display_name.text())
            #TODO: update file selector screen with new displayname 

        # Update all elements that don't get their own function at the same time
        lines_to_change = {}
        

        # if noscope needs to be removed:
        if (not self.scb_noscope.isChecked()) and self.file.check_for_exact_line("SCB_NOSCOPE=1"):

            # make sure this wont lead to regular mangohud being paired with gamescope
            if (
                self.file.check_for_exact_line("export mangohud") or
                self.file.check_for_exact_line("export MANGOHUD=1")
            ):
                result = fman.load_message_box(
                    parent_window,
                    "Warning!",
                    ("You have MangoHUD as an environment variable and are attempting to enable Gamescope!\n"
                    "This is not supported.\n"
                    "You should either use the \"MangoHUD Overlay\" checkbox inside of Gamescope or disable Gamescope!"),
                    QMessageBox.Icon.Warning,
                    QMessageBox.StandardButton.Ignore | QMessageBox.StandardButton.Cancel
                )
                if result != QMessageBox.StandardButton.Ignore:
                    return True
                
            lines_to_change["SCB_NOSCOPE=1"] = "#SCB_NOSCOPE=1"
            self.data['noscope'] = False


        # if noscope needs to be added:
        if self.scb_noscope.isChecked() and (not self.file.check_for_exact_line("SCB_NOSCOPE=1")):
            lines_to_change["#SCB_NOSCOPE=1"] = "SCB_NOSCOPE=1"
            self.data['noscope'] = True


        # if scb_autos need to be removed:
        if (not self.scb_auto_flags.isChecked()) and self.file.check_for_exact_line("SCB_AUTO"):
            lines_to_change["SCB_AUTO_RES=1"] = "#SCB_AUTO_RES=1"
            lines_to_change["SCB_AUTO_HDR=1"] = "#SCB_AUTO_HDR=1"
            lines_to_change["SCB_AUTO_VRR=1"] = "#SCB_AUTO_VRR=1"
            self.data['autos'] = False

        # if scb_autos need to be added:
        if self.scb_auto_flags.isChecked() and (not self.file.check_for_exact_line("SCB_AUTO")):
            lines_to_change["#SCB_AUTO_RES=1"] = "SCB_AUTO_RES=1"
            lines_to_change["#SCB_AUTO_HDR=1"] = "SCB_AUTO_HDR=1"
            lines_to_change["#SCB_AUTO_VRR=1"] = "SCB_AUTO_VRR=1"
            self.data['autos'] = True
            
        list_current = []
        list_new = []

        for key, value in lines_to_change.items():
            list_current.append(key)
            list_new.append(value)

        self.file.edit_exact_lines(list_current,list_new)
        
        self.apply_button.setDisabled(True)
        return False
            

        
        

    