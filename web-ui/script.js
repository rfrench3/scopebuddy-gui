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
    if (rendered_width.value != 0) {editableList.push(`-w ${rendered_width.value}`)}
    if (rendered_height.value != 0) {editableList.push(`-h ${rendered_height.value}`)}
    if (output_width.value != 0) {editableList.push(`-W ${output_width.value}`)}
    if (output_height.value != 0) {editableList.push(`-H ${output_height.value}`)}
    if (fps.value != 0) {editableList.push(`-r ${fps.value}`)}
    if (fullscreen.checked) {editableList.push(`-f`)}
    if (borderless_window.checked) {editableList.push(`-b`)}
    if (hdr.checked) {editableList.push(`--hdr-enabled`)}
    if (steam.checked) {editableList.push(`-e`)}
    if (mangohud.checked) {editableList.push(`--mangoapp`)}
    if (force_grab_cursor.checked) {editableList.push(`--force-grab-cursor`)}
    if (force_internal_fullscreen.checked) {editableList.push(`--force-windows-fullscreen`)}
    if (mouse_sensitivity.value != 1.00) {editableList.push(`-s ${mouse_sensitivity.value}`)}
    if (vrr.checked) {editableList.push(`--adaptive-sync`)}
    if (max_scale_factor.value != 0) {editableList.push(`-m ${max_scale_factor.value}`)}
    if (upscaler_type.value != 0) {editableList.push(`-S ${upscaler_type.value}`)}//       !!!
    if (upscaler_filter.value != 0) {editableList.push(`-F ${upscaler_filter.value}`)}//   !!!
    if (upscaler_sharpness.value != 0) {editableList.push(`--sharpness ${upscaler_sharpness.value}`)}
    if (additional_args.value != 0) {editableList.push(additional_args.value)}
    // end of entries
    editableList.push("-- %command%");
    let gamescope_line = editableList.join(' ');
    const output = document.getElementById('output_config'); // send generated line to this element
    if (output) {
        output.textContent = gamescope_line;
    }
}

document.getElementById('generate_gamescope_config').addEventListener('click', function() {
    if (document.querySelector('form').reportValidity()) {
        //TODO: make sure width is not set if height is not set
        generateGamescopeConfig();
    }
});