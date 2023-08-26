$(document).ready(function () {
    $(document).on('click', '.favorite-toggle', function (event) {
        event.preventDefault();
        console.log('stopDefault')

    });
});

$(document).ready(function () {
    $(document).on('click', '.other-favorite-toggle', function (event) {
        event.preventDefault();
        console.log('stopDefault')

    });
});
