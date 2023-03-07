// 1) Dark Mode
const toggleSwitch = document.querySelector('#flexSwitchCheckChecked');
toggleSwitch.addEventListener('change', switchTheme);

function switchTheme(event) {
if (event.target.checked) {
    document.documentElement.setAttribute('data-theme', 'dark');
    localStorage.setItem('theme', 'dark');
} else {
    document.documentElement.setAttribute('data-theme', 'light');
    localStorage.setItem('theme', 'light');
    }
}

// retrieve saved user preference from local storage and set the theme
const currentTheme = localStorage.getItem('theme');
if (currentTheme) {
document.documentElement.setAttribute('data-theme', currentTheme);
if (currentTheme === 'dark') {
    toggleSwitch.checked = true;
    }
}

// 2) Copy to Clipboard
function copyToClipboard() {
    var textarea = document.getElementById("exampleFormControlTextarea1");
    textarea.select();
    document.execCommand("copy");
}
