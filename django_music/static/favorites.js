document.addEventListener("DOMContentLoaded", function() {
    var favoriteButtons = document.querySelectorAll(".favorite-toggle");

    favoriteButtons.forEach(function(button) {
        button.addEventListener("click", function() {
            var albumId = button.getAttribute("data-album-id");
            var form = button.nextElementSibling; // Get the next form element

            // Toggle the icon
            var isFavorite = button.querySelector("img").src.endsWith("love-heart-svgrepo-com.svg");
            if (isFavorite) {
                button.querySelector("img").src = "{% static 'icons/heart-svgrepo-com.svg' %}";
            } else {
                button.querySelector("img").src = "{% static 'icons/love-heart-svgrepo-com.svg' %}";
            }

            // Submit the form to update the server
            form.submit();
        });
    });
});