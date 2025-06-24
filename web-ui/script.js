function copyConfigToClipboard() {
    const output = document.getElementById('output_config');
    if (output) {
        const text = output.textContent || output.innerText;
        navigator.clipboard.writeText(text);
    }
}

function generateGamescopeConfig() {
    // Assign all input fields to constants
    const rendered_width = document.getElementById('rendered_width');
    const rendered_height = document.getElementById('rendered_height');
    const output_width = document.getElementById('output_width');
    const output_height = document.getElementById('output_height');
    const fps = document.getElementById('fps');
    const fullscreen = document.getElementById('fullscreen');
    const borderless_window = document.getElementById('borderless_window');
    const hdr = document.getElementById('hdr');
    const steam = document.getElementById('steam');
    const mangohud = document.getElementById('mangohud');
    const force_grab_cursor = document.getElementById('force_grab_cursor');
    const force_internal_fullscreen = document.getElementById('force_internal_fullscreen');
    const mouse_sensitivity = document.getElementById('mouse_sensitivity');
    const vrr = document.getElementById('vrr');
    const max_scale_factor = document.getElementById('max_scale_factor');
    const upscaler_type = document.getElementById('upscaler_type');
    const upscaler_filter = document.getElementById('upscaler_filter');
    const upscaler_sharpness = document.getElementById('upscaler_sharpness');
    const additional_args = document.getElementById('additional_args');

    let editableList = []; //append each argument to this list
    editableList.push("gamescope");
    // beginning of entries


    // end of entries
    editableList.push("-- %command%");
    let gamescope_line = editableList.join(' ')
    const output = document.getElementById('output_config'); // send generated line to this element
    if (output) {
        output.textContent = gamescope_line;
    }
}