default:
    just --list

# build, install, and run flatpak
brun-flatpak:
    flatpak-builder --force-clean --user --install app io.github.rfrench3.scopebuddy-gui.yml
    flatpak run --user io.github.rfrench3.scopebuddy-gui

run:
    python src/main.py

validate-appstream:
    appstreamcli validate io.github.rfrench3.scopebuddy-gui.metainfo.xml
