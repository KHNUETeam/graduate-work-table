$(document).ready(function() {
$(window).on('load', function () {
    $('.loader').hide(900);
});
    
    $(document).on("click",".btn-group > .btn-secondary", function(){
        var test = $(this).text();
        $('.btn-secondary').removeClass('active')
        $(this).addClass('active')
        
    });
    $(window).on('load', function () {
        var hash = window.location.hash.substr(1);
            if(hash == ''){
                $('[str="1"]').addClass("active");
            }else{
                $('.btn-group > .btn-secondary').removeClass('active')
                $('[str="'+hash+'"]').addClass("active");
            }

    });
});