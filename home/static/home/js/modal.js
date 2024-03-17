window.onload = function () {
    var modal = document.getElementById("myModal");
    var span = document.getElementsByClassName("close")[0];
    var modalDisplayed = false;

    // Check if the toast message exists, if so, do not show the modal
    var toastMessage = document.querySelector('.toast');
    if (!toastMessage) {
        modal.style.display = "block";
        modalDisplayed = true;
    }

    // When the user clicks on <span> (x), close the modal
    span.onclick = function () {
        modal.style.display = "none";
        modalDisplayed = false;
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
            modalDisplayed = false;
        }
    }

    // Function to close the modal
    function closeModal() {
        modal.style.display = "none";
        modalDisplayed = false;
    }

    // Expose the closeModal function so it can be called from outside
    window.closeModal = closeModal;
}
