# General Github Tutorial - how to install a new app release!
- insert image pointing to the Releases section

- [Link to the releases page!](https://github.com/rfrench3/scopebuddy-gui/releases)

# ScopeBuddy GUI
Graphical Frontend for the scopebuddy tool.

This GUI is only useful if you also have scopebuddy and gamescope installed, and it currently does not install those dependencies for you.

- [Link to the documentation! (in progress)](https://rfrench3.github.io/scopebuddy-gui)

# Build Instructions

Within the source folder, run:

- flatpak-builder --force-clean --repo=repo builddir io.github.rfrench3.scopebuddyGUI.yml

- flatpak build-bundle repo scopebuddyGUI.flatpak io.github.rfrench3.scopebuddyGUI --verbose