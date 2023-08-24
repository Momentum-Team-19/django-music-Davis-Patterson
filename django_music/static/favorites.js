$(document).ready(function () {
    $('#favoriteButton').click(function () {
        const albumId = $(this).data('album-id');

        $.post(`/toggle_favorite/${albumId}/`, function (data) {
            if (data.is_favorite) {
                $('#favoriteButton').addClass('favorited').text('Remove from Favorites');
            } else {
                $('#favoriteButton').removeClass('favorited').text('Add to Favorites');
            }
        });
    });
});
