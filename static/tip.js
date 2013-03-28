var tip = (function(my, $) {

    my.getPercentage = function(rating) {
        return 1.0 + (rating * 4 * 0.01);
    };

    return my;


})(tip || {}, jQuery);
