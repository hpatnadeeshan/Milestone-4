window.onload = function () {
    var modal = document.getElementById("myModal");
    var span = document.getElementsByClassName("close")[0];

    // Check if the toast message exists, if so, do not show the modal
    var toastMessage = document.querySelector('.toast');
    if (!toastMessage) {
        modal.style.display = "block";
        var showStyle = document.createElement('style');
        showStyle.innerHTML = '.fade:not(.show) { opacity: 1; }';
        document.head.appendChild(showStyle);
    }

    // When the user clicks on <span> (x), close the modal
    span.onclick = function () {
        modal.style.display = "none";
        var hideStyle = document.createElement('style');
        hideStyle.innerHTML = '.fade:not(.show) { opacity: 0; }';
        document.head.appendChild(hideStyle);
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
            hideStyle.innerHTML = '.fade:not(.show) { opacity: 0; }';
            document.head.appendChild(hideStyle);
        }
    }
}
