angular.module('blstApp', []);

function rotateCard(btn){
    var $card = $(btn).closest('.card-container');
    if($card.hasClass('hover')){
        $card.removeClass('hover');
    } else {
        $card.addClass('hover');
    }
}

$(document).ready(function() {
    $.fn.editable.defaults.mode = 'inline';
    
    $('#title').editable({
        toggle:'manual'
    });

    $('.edit-title').click(function(e){
        e.stopPropagation();
        $('#title').editable('toggle');
    });
});
