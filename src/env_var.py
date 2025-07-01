from PySide6.QtWidgets import QPushButton, QListWidget

class EnvVarLogic:
    def __init__(self) -> None:
            self.userinputs = {
                'button_new_config': [QPushButton,self.new_config_pressed],
                'file_list': [QListWidget, self.list_clicked]
            }

    def new_config_pressed(self) -> None:
        """opens a modal that has the user create a new config with a Steam AppID."""
        pass
    
    def list_clicked(self) -> str:
        """opens the config file the user clicked."""
        pass