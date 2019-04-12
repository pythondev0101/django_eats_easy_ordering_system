if (!$){
    $ = django.jQuery;
}

$(function(){
    if ($('#form_name').length){
        var new_date = new Date();
        var name_val = "Order for " + new_date.getMonth() + '_' + new_date.getDate();
        $('#id_name').val(name_val);
//        $('#id_orderline_set-0-day').val('monday');
//        $('#id_orderline_set-1-day').val('tuesday');
//        $('#id_orderline_set-2-day').val('wednesday');
//        $('#id_orderline_set-3-day').val('thursday');
//        $('#id_orderline_set-4-day').val('friday');
    }
});


