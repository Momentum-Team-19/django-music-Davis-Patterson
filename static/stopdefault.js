$(document).ready(function () {
    $(document).on('click', '.favorite-toggle', function (event) {
        event.preventDefault();
        event.stopPropagation();
        console.log('stopDefault')

        var $toggleButton = $(this); // Store the button that was clicked

        var albumId = $toggleButton.data("album-id");

        $.ajax({
            type: "POST",
            url: "{% url 'toggle_favorite' %}",  // Replace with your actual URL
            data: {
                album_id: albumId,
                csrfmiddlewaretoken: "{{ csrf_token }}"
            },
        });
    });
});

$(document).ready(function () {
    $(document).on('click', '.other-favorite-toggle', function (event) {
        event.preventDefault();
        event.stopPropagation();
        console.log('stopDefault')
    });
});
