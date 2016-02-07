angular.module('blstApp', []);

function rotateCard(btn){
    var $card = $(btn).closest('.card-container');
    if($card.hasClass('hover')){
        $card.removeClass('hover');
    } else {
        $card.addClass('hover');
    }
}

/* Initialize Digits for Web using your application's consumer key that Fabric generated */
document.getElementById('digits-sdk').onload = function() {
  Digits.init({ consumerKey: 'yourConsumerKey' });
};
