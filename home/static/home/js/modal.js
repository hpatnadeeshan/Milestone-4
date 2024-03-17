console.log("JavaScript code is executing.");
// Get the modal element
var modal = document.getElementById("myModal");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];
    
// When the page loads, show the modal
window.onload = function () {
    modal.style.display = "block";
    console.log("window onload working.");
}

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}