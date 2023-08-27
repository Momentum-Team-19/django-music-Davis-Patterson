<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

$(document).ready(function() {
    $(".favorite-toggle").click(function() {
        var albumId = $(this).data("album-id");

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
