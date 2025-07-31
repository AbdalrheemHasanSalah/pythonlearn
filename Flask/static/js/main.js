$(function() {
    // Function to dynamically set the width of the skill progress bars
        $('.skill-progress span').each(function() {
            $(this).animate({
                width: $(this).data('width') 
            }, 90000);
        });
    }
)
