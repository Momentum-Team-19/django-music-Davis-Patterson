$(document).ready(function () {
    $(document).on('click', '.favorite-toggle', function (event) {
        event.preventDefault();
        event.stopPropagation();
        console.log('favorite click')

        var $toggleButton = $(this);

        var albumId = $toggleButton.data("album-id");

        var urlWithAlbumId = toggleFavoriteUrl.replace('0', albumId);

        $.ajax({
            type: "POST",
            url: urlWithAlbumId,
            data: {
                album_id: albumId,
            },
        });
    });
});

$(document).ready(function () {
    $(document).on('click', '.other-favorite-toggle', function (event) {
        event.preventDefault();
        event.stopPropagation();
        console.log('other-favorite click')

        var $toggleButton = $(this);

        var albumId = $toggleButton.data("album-id");

        var urlWithAlbumId = toggleFavoriteUrl.replace('0', albumId);

        $.ajax({
            type: "POST",
            url: urlWithAlbumId,
            data: {
                album_id: albumId,
            },
        });
    });
});

$(document).ready(function () {
    $(document).on('click', '.detail-favorite-toggle', function (event) {
        console.log('detail-favorite click')
        var $toggleButton = $(this);

        var albumId = $toggleButton.data("album-id");

        var urlWithAlbumId = toggleFavoriteUrl.replace('0', albumId);

        $.ajax({
            type: "POST",
            url: urlWithAlbumId,
            data: {
                album_id: albumId,
            },
        });
    });
});
