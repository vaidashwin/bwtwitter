
function showhide(elementName, buttonName) {
    var div = document.getElementById(elementName);
    var button = document.getElementById(buttonName);
    if ( div.style.display !== "none" ) {
        div.style.display = "none";
        button.innerHTML = 'View Timeline';
    } else {
        div.style.display = "block";
        button.innerHTML = 'Hide Timeline';
    }
}
