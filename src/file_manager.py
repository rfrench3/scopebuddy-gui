import os, shutil
from re import search


def get_data_path():
    if os.path.basename(os.path.dirname(__file__)) == "src":
        return os.path.abspath(os.path.dirname(__file__))
    else:
        return os.path.abspath(os.path.join(os.path.dirname(__file__), "../share/scopebuddygui"))
    
def create_directory():
    """Create the directory for /scopebuddy/scb.conf, returns full path to scb.conf"""
    CONFIG_DIR = os.path.join(os.environ.get("XDG_CONFIG_HOME", os.path.expanduser("~/.config")), "scopebuddy")
    os.makedirs(CONFIG_DIR, exist_ok=True)
    scb_config_path = os.path.join(CONFIG_DIR, "scb.conf")

def ensure_file(scb_config_path) -> None: 
    """creates scb.conf if it doesn't exist, and calls on ensure_gamescope_line afterwards."""
    def ensure_gamescope_line(): 
        """ if config file doesn't have the gamescope args line, create one in the best place.
        this will be where a commented out line is if one is found, or at the end."""

        # will be used if the correct line isn't already present
        new_line = f'SCB_GAMESCOPE_ARGS=""\n'

        with open(scb_config_path, 'r') as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            if line.startswith('SCB_GAMESCOPE_ARGS='):
                match = search(r'SCB_GAMESCOPE_ARGS="([^"]*)"', line)
                if match:
                    #the line is exists and is good
                    return 
                else:
                    #the line will be commented out because it will probably cause errors.
                    #a proper line will be placed after it
                    lines[i:i+1] = [f'#SCBGUI_ERROR_PREVENTATION!#{line}', new_line]
                    with open(scb_config_path, 'w') as file: 
                        file.writelines(lines)
                    return

        # Assume the gamescope_args line has no breaking issues at this point.

        # check for the default commented out line in the config file.
        # if found, place the new gamescope line right after it
        for i, line in enumerate(lines):
            if line.startswith('#SCB_GAMESCOPE_ARGS'):
                lines[i:i+1] = [line, new_line]
                # Write the modified lines back to the file
                with open(scb_config_path, 'w') as file:
                    file.writelines(lines)
                return
    
        # no match was found, so create the necessary line at the end of the file
        with open(scb_config_path, 'a') as file:
            if lines and not lines[-1].endswith('\n'):
                file.write('\n')
            file.write('SCB_GAMESCOPE_ARGS=""\n')
        return
            
    try:
        if os.path.exists(scb_config_path):
            #print(f"Config file already exists at {scb_config_path}, ensuring the proper format...")
            ensure_gamescope_line()
            return
        else:
            #print(f"Creating config file at {scb_config_path} from template...")
            shutil.copyfile(template, scb_config_path)
            ensure_gamescope_line()
            return
    except Exception as e:
        print(f"Error creating config file: {e}")





DATA_DIR = get_data_path()
template = os.path.join(DATA_DIR, "default_scb.conf")