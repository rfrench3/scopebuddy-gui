
<h1>ScopeBuddy GUI</h1>

<img src="src/img/io.github.rfrench3.scopebuddy-gui.svg" alt="ScopeBuddy GUI Logo">

<h2 align="center">A Graphical Frontend for the scopebuddy tool.</h2>

![Welcome Screen](src/img/welcomeScreen.png)

<h1 align="center">Features</h1>

<p>This is a convenient, easy-to-use interface for configuring Gamescope through Scopebuddy. Gamescope, which plays a large role in the interface of the SteamDeck, has many features that allow for precise control of many aspects of rendering games and other programs. This is especially useful with screens such as ultrawide monitors and others that have an unusual aspect ratio. These features, which may have previously been too complicated for many to use, include:</p>

- Setting a normal screen resolution and aspect ratio for games to run through.
- Support for features like High Dynamic Range (HDR) and Adaptive Sync.
- Running games at a lower resolution to greatly improve FPS.


<p>While a lot of games will handle oddities like a strange aspect ratio gracefully, a lot of games do not.</p>

<br>

<h1 align="center">Requirements</h1>

This GUI is only useful if you also have scopebuddy and gamescope installed, and it currently does not install those dependencies for you. The github pages for the required programs are:
- [Gamescope](https://github.com/ValveSoftware/gamescope)
- [Scopebuddy](https://github.com/HikariKnight/scopebuddy)

Gamescope is likely available for easy installation through your Linux Distro's package manager. Helpful information regarding the usage of gamescope can be found in my [documentation.](https://rfrench3.github.io/scopebuddy-gui)

<br>

<h1 align="center">Where to Install the Latest Release</h1>

There are a few different ways to use this application:

You can get it on Flathub,

<a href='https://flathub.org/apps/io.github.rfrench3.scopebuddy-gui'>
  <img width='240' alt='Get it on Flathub' src='https://flathub.org/api/badge?locale=en'/>
</a>


you can use the [web-based version](https://rfrench3.github.io/scopebuddy-gui/web-ui/index.html) (that outputs for gamescope directly),


or, you can install it directly from this github.

[![GitHub Releases Section](github.png)](https://github.com/rfrench3/scopebuddy-gui/releases)
<sub>Clicking the image also brings you to the releases.</sub>

<br>

<h1 align="center">License</h1>

<p>GPL-3.0-only. See LICENSE for details.</p>

<br>

<h1 align="center">Build Instructions</h1>

Once you have all of the required dependencies, within the root folder (the one that contains the .yml) run the following commands in order:

- flatpak-builder --force-clean --repo=repo builddir io.github.rfrench3.scopebuddy-gui.yml

- flatpak build-bundle repo scopebuddy-gui.flatpak io.github.rfrench3.scopebuddy-gui --verbose


(Running the first command and reviewing the errors is a simple way to locate other build dependencies)


