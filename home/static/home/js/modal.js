console.log("JavaScript code is executing.");
// Get the modal element
var modal = document.getElementById("myModal");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];
    
// When the page loads, show the modal
window.onload = function () {
    modal.style.display = "block";
    console.log("window onload working.");

    // Apply the CSS rule for showing the modal
    var showStyle = document.createElement('style');
    showStyle.innerHTML = '.fade:not(.show) { opacity: 1; }';
    document.head.appendChild(showStyle);

    // Event listener for close button
    span.onclick = function () {
        modal.style.display = "none";

        // Apply the CSS rule for hiding the modal
        var hideStyle = document.createElement('style');
        hideStyle.innerHTML = '.fade:not(.show) { opacity: 0; }';
        document.head.appendChild(hideStyle);
    }
}
