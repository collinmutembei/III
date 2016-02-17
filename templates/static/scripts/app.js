angular.module('blstApp', ['ngResource', 'angularMoment']);

angular.module('blstApp').config(function($httpProvider) {

    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

});

function rotateCard(btn){
    var $card = $(btn).closest('.card-container');
    if($card.hasClass('hover')){
        $card.removeClass('hover');
    } else {
        $card.addClass('hover');
    }
}

$(document).ready(function(){
    $("#addBucketlistModal").on('shown.bs.modal', function(){
        $(this).find('input[type="text"]').focus();
    });

    $("#editBucketlistModal").on('shown.bs.modal', function(){
        $(this).find('input[type="text"]').focus();
    });

    $("#addItemModal").on('shown.bs.modal', function(){
        $(this).find('input[type="text"]').focus();
    });
});
