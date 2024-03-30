var alertBox = document.querySelector('#alert-container .alert');

// Timeout function to hide the alert after 5 seconds (5000 milliseconds)
setTimeout(function() {
    // Check if the alert box exists before trying to hide it
    if (alertBox) {
        alertBox.style.display = 'none';
    }
}, 4000);