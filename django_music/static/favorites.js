$(document).ready(function () {
    $(document).on('click', '.favorite-toggle', function (event) {
        event.preventDefault();
        event.stopPropagation();
        console.log('stopPropagation')

    });
});
