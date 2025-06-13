<table width="100%">
    <tr>
        <td align="center" width="50%">
        <p style="font-size:2.5em; font-weight:bold; margin:0;">ScopeBuddy GUI</p>
        </td>
        <td align="center" width="50%">
            <img src="src/img/io.github.rfrench3.scopebuddy-gui.svg" alt="ScopeBuddy GUI Logo" height="120">
        </td>
    </tr>
</table>



<h2 align="center"> A Graphical Frontend for the scopebuddy tool.</h2>

![Main Window](src/img/mainWindow.png)

This GUI is only useful if you also have scopebuddy and gamescope installed, and it currently does not install those dependencies for you. The github pages for the required programs are:
- [Gamescope](https://github.com/ValveSoftware/gamescope)
- [Scopebuddy](https://github.com/HikariKnight/scopebuddy)

Gamescope is likely available for easy installation through your Linux Distro's package manager. Helpful information regarding the usage of gamescope can be found in my [documentation.](https://rfrench3.github.io/scopebuddy-gui)

<br>

# Where to install the latest release:
[![GitHub Releases Section](github.png)](https://github.com/rfrench3/scopebuddy-gui/releases)
<sub>Clicking the image also brings you to the releases.</sub>

<br>

# License

GPL-3.0-only. See LICENSE for details.
# Build Instructions

Once you have all of the required dependencies, within the root folder (the one that contains the .yml) run the following commands in order:

- flatpak-builder --force-clean --repo=repo builddir io.github.rfrench3.scopebuddy-gui.yml

- flatpak build-bundle repo scopebuddy-gui.flatpak io.github.rfrench3.scopebuddy-gui --verbose


(Running the first command and reviewing the errors is a simple way to locate other build dependencies)


