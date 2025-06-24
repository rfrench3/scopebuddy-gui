function copyConfigToClipboard() {
    const output = document.getElementById('output_config');
    if (output) {
        const text = output.textContent || output.innerText;
        navigator.clipboard.writeText(text);
    }
}