var otherAlbums = document.querySelectorAll('.otherAlbums');

if (otherAlbums.length === 0) {
    // If there are no other albums, hide the entire container
    var otherAlbumContainer = document.querySelector('.otherAlbumContainer');
    if (otherAlbumContainer) {
        otherAlbumContainer.style.display = 'none';
    }
}