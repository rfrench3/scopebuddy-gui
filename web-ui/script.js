function copyConfigToClipboard() {
    const output = document.getElementById('output_config');
    if (output) {
        const text = output.textContent || output.innerText;
        navigator.clipboard.writeText(text);
    }
}

function generateGamescopeConfig() {
    const output = document.getElementById('output_config'); // send generated line to this element
    if (output) {
        output.textContent = 'test';
    }
}