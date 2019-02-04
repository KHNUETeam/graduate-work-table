$(document).ready(function () {
    $(window).on('load', function () {
        $('.loader').hide(900);
    });

    $(document).on("click", ".btn-group > .btn-secondary", function () {
        var test = $(this).text();
        $('.btn-secondary').removeClass('active')
        $(this).addClass('active')

    });
    $(window).on('load', function () {
            var url = location.search.substr(1);
        if (url == '') {
            $('[str="1"]').addClass("active");
        } else {
            $('.btn-group > .btn-secondary').removeClass('active')
            $('[formaction="/?' + url + '"]').addClass("active");
        }
    });
});
