# To-Do List

## Features (add new stuff)

- get the app running outside of the dev environment

- DEFAULT SETTINGS:
    - if there's a config already, open GUI with its options selected
    - if there isn't, have a sane set of defaults (1080p, 60fps, etc)
    - clear-all button 
    - large field for gamescope options not recognized by/implemented into the gui

- add tooltips to further explain every option

- clearly indicate that a blank field uses gamescope's default

- disable the "apply" button if scopebuddy is not installed

- implement game-specific configs

- make a pretty icon

- add more gamescope args

- add a button to reset the config to default (if scopebuddy doesn't have one, just make sensible defaults)

- add a button to open the config file in a text editor

- instructions to put scopebuddy launch args in:
    - Lutris
    - Heroic

    - implement picture guides for: (and make the pictures scale based on the window)
        - Steam   *pictures are added but far too large in most cases*
        - Lutris   *no pictures*
        - Heroic   *no pictures*

## Bugfixes (make old stuff work)

- make the window look prettier

- text indicating an empty config file, instead of just showing nothing

- ensure a new scb.conf will be made if one does not exist

- ensure available settings are handled properly in gamescope-session as well as nested gamescope
    - check if the app is running within gamescope, and if its in nested or session, to properly limit settings?

## Features to add when all else is complete (non-critical, potentially difficult, etc)

- support for automatically adding scopebuddy configs to normal steam and flatpak steam

- in-GUI support for non-gamescope functionality of scopebuddy

- pretty window for setting up --display-index




