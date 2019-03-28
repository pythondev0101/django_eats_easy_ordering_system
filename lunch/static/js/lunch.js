if (!$){
    $ = django.jQuery;
}

$(function(){
    if ($('#form_name').length){
        var new_date = new Date();
        var name_val = "Order for " + new_date.getMonth() + '_' + new_date.getDate();
        $('#id_name').val(name_val);
    }
});


