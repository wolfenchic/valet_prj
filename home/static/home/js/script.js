$(document).ready(function(){

function typeWriter(text, i) {
 if (i < (text.length)) {
    $('.scroll').html(text.substring(0, i+1));
    i++;
    setTimeout(function(){
        typeWriter(text, i);
    }, 200);
}
}

typeWriter("Car, Bus, Lorry, Van, Tractor", 0);

  
$('#myForm').on('submit', function(e){
  $('#myModal').modal('show');
  e.preventDefault();

 });
  
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

$("..fa-linkedin, .fa-github, .fa-file").mouseleave(function(){
    $(this).css("color", "#C3AEAF");
});

$(".contactButton").mouseenter(function(){
    $(this).css("background-color", "#EA615B");
});

$(".contactButton").mouseleave(function(){
    $(this).css("background-color", "#EA615B");
});



});




