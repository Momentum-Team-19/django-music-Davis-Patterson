$(document).ready(function () {
    $(document).on('click', '.favorite-toggle', function (event) {
        event.preventDefault();
        console.log('stopDefault')

    });
});
