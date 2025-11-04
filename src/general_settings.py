from PySide6.QtWidgets import QLineEdit, QCheckBox, QDialogButtonBox, QMessageBox
import file_manager as fman
from file_manager import ConfigFile
import shared_data
import os

class GeneralSettingsLogic:
    def __init__(self, file:ConfigFile, parent_widget=None) -> None:
            self.initialized = False # ensure certain functions don't run until __init__ is finished

            self.parent_logic = None  # Will be set by main.py
            self.entries = []  # Store references to all entry widgets
            self.file = file
            self.parent_widget = parent_widget

            # Initialize and connect inputs
            self.display_name = parent_widget.findChild(QLineEdit, 'display_name')  # type: ignore
            self.scb_noscope = parent_widget.findChild(QCheckBox, 'scb_noscope')  # type: ignore
            self.scb_auto_res :QCheckBox = parent_widget.findChild(QCheckBox, 'auto_res') # type: ignore
            self.scb_auto_ref :QCheckBox = parent_widget.findChild(QCheckBox, 'auto_ref') # type: ignore
            self.scb_auto_frame :QCheckBox = parent_widget.findChild(QCheckBox, 'auto_frame') # type: ignore
            self.scb_auto_hdr :QCheckBox = parent_widget.findChild(QCheckBox, 'auto_hdr') # type: ignore
            self.scb_auto_vrr :QCheckBox = parent_widget.findChild(QCheckBox, 'auto_vrr') # type: ignore
            self.button_box = parent_widget.findChild(QDialogButtonBox, 'buttonBox')  # type: ignore
            self.apply_button = self.button_box.button(QDialogButtonBox.StandardButton.Apply) # type: ignore
            self.help_button = self.button_box.button(QDialogButtonBox.StandardButton.Help) # type: ignore

            self.apply_button.clicked.connect(self.save_data)
            self.help_button.clicked.connect(lambda: os.system("xdg-open https://rfrench3.github.io/scopebuddy-gui/"))
    
            # Load lines from the file
            self.load_data()

            self.data = {
                'name': self.display_name.text(),
                'noscope': self.scb_noscope.isChecked(),
                'auto_res': self.scb_auto_res.isChecked(),
                'auto_ref': self.scb_auto_ref.isChecked(),
                'auto_frame': self.scb_auto_frame.isChecked(),
                'auto_hdr': self.scb_auto_hdr.isChecked(),
                'auto_vrr': self.scb_auto_vrr.isChecked()
            }

            self.display_name.textChanged.connect(self.data_changed)
            self.scb_noscope.stateChanged.connect(self.data_changed)
            self.scb_auto_res.stateChanged.connect(self.data_changed)
            self.scb_auto_ref.stateChanged.connect(self.data_changed)
            self.scb_auto_frame.stateChanged.connect(self.data_changed)
            self.scb_auto_hdr.stateChanged.connect(self.data_changed)
            self.scb_auto_vrr.stateChanged.connect(self.data_changed)

            self.apply_button.setDisabled(True)
            self.initialized = True

    def data_changed(self) -> None:
        """When the user has inputted data, compare it to the saved data
          and enable/disable the apply button based on that."""

        if not self.initialized:
            return

        if (
            self.data['name'] == self.display_name.text() and
            self.data['noscope'] == self.scb_noscope.isChecked() and
            self.data['auto_res'] == self.scb_auto_res.isChecked() and
            self.data['auto_ref'] == self.scb_auto_ref.isChecked() and
            self.data['auto_frame'] == self.scb_auto_frame.isChecked() and
            self.data['auto_hdr'] == self.scb_auto_hdr.isChecked() and
            self.data['auto_vrr'] == self.scb_auto_vrr.isChecked()
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

        if self.file.check_for_exact_line("SCB_AUTO_RES=1"):
            self.scb_auto_res.setChecked(True)

        if self.file.check_for_exact_line("SCB_AUTO_REFRESH=1"):
            self.scb_auto_ref.setChecked(True)

        if self.file.check_for_exact_line("SCB_AUTO_FRAME_LIMIT=1"):
            self.scb_auto_frame.setChecked(True)

        if self.file.check_for_exact_line("SCB_AUTO_HDR=1"):
            self.scb_auto_hdr.setChecked(True)

        if self.file.check_for_exact_line("SCB_AUTO_VRR=1"):
            self.scb_auto_vrr.setChecked(True)

        

    def save_data(self) -> bool:
        """Saves data from each of the elements into the file."""

        parent_window = self.parent_widget.window() if self.parent_widget else None


        if self.file.print_displayname() != self.display_name.text():
            self.data['name'] = self.display_name.text()
            self.file.edit_displayname(self.data['name'])
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



        #TODO: This isn't necessarily BAD, but it could easily be better

        

        # if noscope needs to be added:
        if self.scb_noscope.isChecked() and (not self.file.check_for_exact_line("SCB_NOSCOPE=1")):
            lines_to_change["#SCB_NOSCOPE=1"] = "SCB_NOSCOPE=1"
            self.data['noscope'] = True


        # if scb_auto_res needs to be removed:
        if (not self.scb_auto_res.isChecked()) and self.file.check_for_exact_line("SCB_AUTO_RES=1"):
            lines_to_change["SCB_AUTO_RES=1"] = "#SCB_AUTO_RES=1"
            self.data['auto_res'] = False

        # if scb_auto_res needs to be added:
        if self.scb_auto_res.isChecked() and (not self.file.check_for_exact_line("SCB_AUTO_RES=1")):
            lines_to_change["#SCB_AUTO_RES=1"] = "SCB_AUTO_RES=1"
            self.data['auto_res'] = True

        # if scb_auto_ref needs to be removed:
        if (not self.scb_auto_ref.isChecked()) and self.file.check_for_exact_line("SCB_AUTO_REFRESH=1"):
            lines_to_change["SCB_AUTO_REFRESH=1"] = "#SCB_AUTO_REFRESH=1"
            self.data['auto_ref'] = False

        # if scb_auto_ref needs to be added:
        if self.scb_auto_ref.isChecked() and (not self.file.check_for_exact_line("SCB_AUTO_REFRESH=1")):
            lines_to_change["#SCB_AUTO_REFRESH=1"] = "SCB_AUTO_REFRESH=1"
            self.data['auto_ref'] = True

        # if scb_auto_frame needs to be removed:
        if (not self.scb_auto_frame.isChecked()) and self.file.check_for_exact_line("SCB_AUTO_FRAME_LIMIT=1"):
            lines_to_change["SCB_AUTO_FRAME_LIMIT=1"] = "#SCB_AUTO_FRAME_LIMIT=1"
            self.data['auto_frame'] = False

        # if scb_auto_frame needs to be added:
        if self.scb_auto_frame.isChecked() and (not self.file.check_for_exact_line("SCB_AUTO_FRAME_LIMIT=1")):
            lines_to_change["#SCB_AUTO_FRAME_LIMIT=1"] = "SCB_AUTO_FRAME_LIMIT=1"
            self.data['auto_frame'] = True

        # if scb_auto_hdr needs to be removed:
        if (not self.scb_auto_hdr.isChecked()) and self.file.check_for_exact_line("SCB_AUTO_HDR=1"):
            lines_to_change["SCB_AUTO_HDR=1"] = "#SCB_AUTO_HDR=1"
            self.data['auto_hdr'] = False

        # if scb_auto_hdr needs to be added:
        if self.scb_auto_hdr.isChecked() and (not self.file.check_for_exact_line("SCB_AUTO_HDR=1")):
            lines_to_change["#SCB_AUTO_HDR=1"] = "SCB_AUTO_HDR=1"
            self.data['auto_hdr'] = True

        # if scb_auto_vrr needs to be removed:
        if (not self.scb_auto_vrr.isChecked()) and self.file.check_for_exact_line("SCB_AUTO_VRR=1"):
            lines_to_change["SCB_AUTO_VRR=1"] = "#SCB_AUTO_VRR=1"
            self.data['auto_vrr'] = False

        # if scb_auto_vrr needs to be added:
        if self.scb_auto_vrr.isChecked() and (not self.file.check_for_exact_line("SCB_AUTO_VRR=1")):
            lines_to_change["#SCB_AUTO_VRR=1"] = "SCB_AUTO_VRR=1"
            self.data['auto_vrr'] = True
            
        list_current = []
        list_new = []

        for key, value in lines_to_change.items():
            list_current.append(key)
            list_new.append(value)

        self.file.edit_exact_lines(list_current,list_new)
        
        self.apply_button.setDisabled(True)
        shared_data.unsaved_changes = False
        return False
            

        
        

    