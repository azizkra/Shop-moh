
$('.alert').click(function() {
    $(this).fadeOut();
});
$(document).ready(function() {
    // messages timeout for 10 sec
    setTimeout(function() {
        $('.message').fadeOut('slow');
    }, 10000000000); // <-- time in milliseconds, 1000 =  1 sec

    // delete message
    $('.alert').live('click', function(){
        $('.alert').parent().attr('style', 'display:none;');
    })
});