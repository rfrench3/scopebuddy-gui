# This file contains functions for the scopebuddy-gui application.
# They are here because some of them are extremely long and would clutter the main file.

import sys
sys.path.insert(0, "/app/share/scopebuddygui") # flatpak path

import os
from re import search # for searching for gamescope args in the config file
import subprocess # for finding gamescope and scopebuddy

