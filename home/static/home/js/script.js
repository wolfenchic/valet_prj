$(document).ready(function(){

$('a').mouseenter(function() {
 	$(this).css("color", "#C3AEAF");
 });

$('a').mouseleave(function(){
    $(this).css("color", "#4a4a4f");
});

$(".card").mouseenter(function(){
    $(this).animate({opacity: '1.0'}, "slow");
});

$(".card").mouseleave(function(){
    $(this).animate({opacity: '0.6'}, "slow");
});

$(".fa-linkedin, .fa-github, .fa-file").mouseenter(function(){
    $(this).css("color", "#4a4a4f");
});

$(".fa-linkedin, .fa-github, .fa-file").mouseleave(function(){
    $(this).css("color", "#C3AEAF");
});

$(".contactButton").mouseenter(function(){
    $(this).css("background-color", "#EA615B");
});

$(".contactButton").mouseleave(function(){
    $(this).css("background-color", "#EA615B");
});



});






