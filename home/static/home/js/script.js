$(document).ready(function(){

$('li').mouseenter(function() {
 	$(this).css("background-color", "#0F2281");
 });

$('li').mouseleave(function(){
    $(this).css("background-color", "white").css("color", "#0F2281");
});

$('.readButton').mouseenter(function() {
 	$(this).css("background-color", "white").css("color", "#0F2281");
 });
 
 $('.readButton').mouseleave(function(){
    $(this).css("background-color", "#0F2281").css("color", "white");
});

$(".servicePageCard").mouseenter(function(){
    $(this).css("background-color", "#E48D3D").css("color", "white");
  
    
});

$(".servicePageCard").mouseleave(function(){
    $(this).css("background-color", "white").css("color", "#0F2281");
    $(".cardTitle").css("background-color", "white").css("color", "#5EC5C4")
   
});

$(".voucherCard").mouseenter(function(){
    $(this).animate({opacity: '1.0'}, "slow");
   
});

$(".voucherCard").mouseleave(function(){
    $(this).animate({opacity: '0.7'}, "fast");
});

});



