# SPDX-License-Identifier: LGPL-2.1-or-later
# SPDX-FileCopyrightText: 2016-2022 Red Hat Inc
# SPDX-FileContributor: Jan Grulich <jgrulich@redhat.com>
# SPDX-FileCopyrightText: 2022 Harald Sitter <sitter@kde.org>
# SPDX-FileCopyrightText: 2026 Robert French <frenchrobertm@outlook.com>
#
# Ported to Python from the following code, then tweaked to open a file instead of a URL:
#   https://invent.kde.org/libraries/xdg-portal-test-kde/-/blob/master/src/xdgportaltest.cpp?ref_type=heads

from PySide6.QtDBus import QDBusMessage, QDBusConnection, QDBusPendingCallWatcher, QDBusUnixFileDescriptor
from PySide6.QtCore import Slot
import os

def chooseApplication(file_path:str, choose_application:bool=True):
    """
    Opens a dialog that tells the user to select an app to open the file or folder at the given path.
    Once selected, it then opens the file or folder.
    
    :param file_path: Path to the file or folder
    :type file_path: str
    :param choose_application: Should the user be asked which application to open the file/folder with, or should their default be used?
    :type choose_application: bool (default: True)
    :return: No return value
    :rtype: None
    """
    
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} does not exist!")
        raise FileNotFoundError
    
    message = QDBusMessage.createMethodCall(
        "org.freedesktop.portal.Desktop",
        "/org/freedesktop/portal/desktop",
        "org.freedesktop.portal.OpenURI",
        "OpenFile"
    )

    parent_window_id = ""
    
    fd = os.open(file_path, os.O_RDONLY)
    fd_wrapper = QDBusUnixFileDescriptor(fd)
    
    if not fd_wrapper.isValid():
        print("Error: File descriptor is not valid!")
        os.close(fd)
        raise ValueError(f"File descriptor for '{file_path}' is not valid for D-Bus operations")
    
    options = {"ask": choose_application}
    message.setArguments([parent_window_id, fd_wrapper, options])

    print("Sending D-Bus message...")
    pending_call = QDBusConnection.sessionBus().asyncCall(message)
    watcher = QDBusPendingCallWatcher(pending_call)

    def on_finished(w):
        print("D-Bus call finished")
        os.close(fd)
        w.deleteLater()
        reply = w.reply()
        if reply.isError():
            print("Couldn't get reply")
            print(f"Error: {reply.error().message()}")
        else:
            print("Got reply successfully")
            object_path = reply.arguments()[0]
            path_str = object_path.path() if hasattr(object_path, 'path') else str(object_path)
            print(f"Connecting to response signal on path: {path_str}")
            
            QDBusConnection.sessionBus().connect(
                "org.freedesktop.portal.Desktop",
                path_str,
                "org.freedesktop.portal.Request",
                "Response",
                None,
                gotApplicationChoice
            )

    watcher.finished.connect(on_finished)


@Slot(int, dict)
def gotApplicationChoice(response_code: int, results: dict) -> tuple[int,dict]:
    return (response_code, results)