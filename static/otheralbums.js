const showAlbumsIcon = document.getElementById("showAlbumsIcon");
const otherContainer = document.getElementById('otherContainer');
var otherAlbums = document.querySelectorAll('.otherAlbums');


showAlbumsIcon.addEventListener("click", function() {
    if (showAlbumsIcon.innerText === "⌄") {
        showAlbumsIcon.innerText = "^";
        otherContainer.style.display = 'none';
        showAlbumsIcon.style.top = "40.1%";
    } else {
        showAlbumsIcon.innerText = "⌄";
        otherContainer.style.display = 'flex';
        showAlbumsIcon.style.top = "38.85%";
    }
});


if (otherAlbums.length === 0) {
    // If there are no other albums, hide the entire container
    var otherAlbumContainer = document.querySelector('.otherAlbumContainer');
    if (otherAlbumContainer) {
        otherAlbumContainer.style.display = 'none';
    }
}