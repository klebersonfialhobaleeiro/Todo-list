// dark/light
var elemento = document.getElementById('dark');
var theme = document.getElementById('theme');
document.getElementById("dark").onclick = function() {darklight()};

if (localStorage.theme == 'dark'){
    elemento.setAttribute("checked","");
    theme.setAttribute("data-bs-theme","dark");

} else if (localStorage.theme == 'light') {
    theme.setAttribute("data-bs-theme","light");
} else {
    console.log('F');
}

function darklight() {
    if (document.getElementById("dark").checked == true){
        localStorage.setItem('theme','dark')
        theme.setAttribute("data-bs-theme","dark");
    }
    else{
        localStorage.setItem('theme','light')
        theme.setAttribute("data-bs-theme","light");
    }
}