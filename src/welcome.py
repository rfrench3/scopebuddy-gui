from PySide6.QtWidgets import QApplication, QPushButton, QListWidget, QWidget

class WelcomeLogic:
    def __init__(self, widget=None) -> None:
            self.userinputs = {
            #   'objectName': [Class,function],
                'button_new_config': [QPushButton,self.new_config_pressed],
                'file_list': [QListWidget, self.list_clicked]
                }

            if widget:
                self.initialize(widget)

    def initialize(self, parent_widget):
        """using the self.userinputs dictionary, establishes the Qt objects and connects it to python code."""
        for object_name, (widget_class, method) in self.userinputs.items():
            widget = parent_widget.findChild(widget_class, object_name)
            if widget:
                if isinstance(widget, QPushButton):
                    widget.clicked.connect(method)
                elif isinstance(widget, QListWidget):
                    widget.itemClicked.connect(method)

    def new_config_pressed(self) -> None:
        """opens a modal that has the user create a new config with a Steam AppID."""
        print('press')
        pass
    
    def list_clicked(self) -> None:
        """opens the config file the user clicked."""
        pass
