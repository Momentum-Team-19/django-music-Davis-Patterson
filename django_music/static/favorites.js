$(document).ready(function () {
    $('.favorite-toggle').click(function (event) {
        event.preventDefault();
        event.stopPropagation();

        const albumId = $(this).data('album-id');
        const button = $(this); 

        $.post(`/toggle_favorite/${albumId}/`, function (data) {
            if (data.is_favorite) {
                button.addClass('favorited').text('Remove from Favorites');
            } else {
                button.removeClass('favorited').text('Add to Favorites');
            }
        });
    });
});
