# SPDX-License-Identifier: LGPL-3.0-only
# SPDX-FileCopyrightText: 2016-2022 Red Hat Inc
# SPDX-FileContributor: Jan Grulich <jgrulich@redhat.com>
# SPDX-FileCopyrightText: 2022 Harald Sitter <sitter@kde.org>
# SPDX-FileCopyrightText: 2026 Robert French <frenchrobertm@outlook.com>
#
# Ported to Python from the following code, then tweaked to open a file instead of a URL:
#   https://invent.kde.org/libraries/xdg-portal-test-kde/-/blob/master/src/xdgportaltest.cpp?ref_type=heads

from PySide6.QtDBus import QDBusMessage, QDBusConnection, QDBusPendingCallWatcher, QDBusUnixFileDescriptor
# from PySide6.QtCore import Slot
import os

from PySide6.QtWidgets import QWidget

class ChooseApplicationMixin:
    """
    Mixin class that provides application selection functionality for Qt widgets.
    This mixin enables Qt-based GUI classes to use the freedesktop.org D-Bus portal
    to prompt users to select an application to open files or folders. It leverages
    the org.freedesktop.portal.OpenURI interface.
    
    Raises:
        TypeError: If the class using this mixin does not inherit from QWidget.

    Usage:
        self.chooseApplication(file_path:str, choose_application:bool=True)
    """
    
    def __init_subclass__(cls, **kwargs):
        # This init ensures the mixin is only added to a valid class
        super().__init_subclass__(**kwargs)
        
        # Check if the class defining this mixin is a subclass of QWidget
        if not issubclass(cls, QWidget):
            raise TypeError(
                f"Error: '{cls.__name__}' uses ChooseApplicationMixin "
                f"but does not inherit from QWidget."
            )

    def chooseApplication(self: QWidget, file_path:str, choose_application:bool=True): #type:ignore
        """
        Opens a dialog that tells the user to select an app to open the file or folder at the given path.
        Once selected, it then opens the file or folder.

        NOTE: This can fail silently! If file_path is not on the normal system (for example, it is a path specific to the flatpak sandbox), 
        it will not raise an error despite not *actually* being valid!

        :param file_path: Path to the file or folder
        :type file_path: str
        :param choose_application: Should the user be asked which application to open the file/folder with, or should their default be used?
        :type choose_application: bool (default: True)
        :return: No return value
        :rtype: None
        """

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File {file_path} does not exist!")

        message = QDBusMessage.createMethodCall(
            "org.freedesktop.portal.Desktop",
            "/org/freedesktop/portal/desktop",
            "org.freedesktop.portal.OpenURI",
            "OpenFile"
        )

        parent_window_id = str(self.winId()) if hasattr(self, 'winId') else ""

        fd = os.open(file_path, os.O_RDONLY)
        fd_wrapper = QDBusUnixFileDescriptor(fd)

        if not fd_wrapper.isValid():
            os.close(fd)
            raise ValueError(f"File descriptor for '{file_path}' is not valid for D-Bus operations")

        options = {"ask": choose_application}
        message.setArguments([parent_window_id, fd_wrapper, options])

        #print(f"Sending D-Bus message... ({message.arguments()})")
        pending_call = QDBusConnection.sessionBus().asyncCall(message)
        
        watcher = QDBusPendingCallWatcher(pending_call, self)
        
        def on_finished(watcher:QDBusPendingCallWatcher):
            #print("D-Bus call finished")
            os.close(fd)
            watcher.deleteLater()
            reply = watcher.reply()
            if reply.type() == QDBusMessage.errorMessage:
                print("Couldn't get reply")
                print(f"Error: {reply.errorMessage()}")
            else:
                #print(f"Got reply successfully ({reply})")
                object_path = reply.arguments()[0]
                path_str = object_path.path() if hasattr(object_path, 'path') else str(object_path)
                #print(f"Connecting to response signal on path: {path_str}")

                QDBusConnection.sessionBus().connect(
                    "org.freedesktop.portal.Desktop", # service
                    path_str,                         # path
                    "org.freedesktop.portal.Request", # interface
                    "Response",                       # name
                    self,                             # QObject
                    None                              # slot
                )

        watcher.finished.connect(on_finished)
'''
NOTE: replacing "None" in the QDBusConnection.sessionBus().connect with "callFinishedSlot" 
      results in the following message, making me think it is a PySide6 bug.
qt.dbus.integration: Could not connect "org.freedesktop.portal.Request" to allFinishedSlot :

This never runs, so it is commented out for now
    # @Slot(int, dict)
    # def callFinishedSlot(self, call):
    #     print("called")
    #     pass
'''