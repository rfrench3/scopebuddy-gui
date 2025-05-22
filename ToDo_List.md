# To-Do List

## reduced features build:

To ensure I get out a useful version of the app in a useful packaging format (Flatpak), I have made this build. Any major planned features (such as game-specific configs) will not be present to any extent until I am fully confident they are ready. My main goal is to get out a presentable "version 1" to avoid being overtaken by scope creep.




## Features (add new stuff)

- DEFAULT SETTINGS:
    - if there's a config already, open GUI with its options selected
    - if there isn't, have a sane set of defaults (1080p, 60fps, etc)
    - clear-all button 
    - large field for gamescope options not recognized by/implemented into the gui

- disable the "apply" button if scopebuddy is not installed

- implement game-specific configs

- make a pretty icon

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

- if the app is running inside gamescope-session, inform user that the tool should only be used in desktop mode 

- make the window look prettier

- text indicating an empty config file, instead of just showing nothing

## Features to add when all else is complete (non-critical, potentially difficult, etc)

- support for automatically adding scopebuddy configs to normal steam and flatpak steam

- in-GUI support for non-gamescope functionality of scopebuddy

- pretty window for setting up --display-index




