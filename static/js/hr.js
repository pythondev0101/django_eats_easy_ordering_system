if (!$){
    $ = django.jQuery;
}
$(function(){

$(".datepicker").datepicker({
    beforeShowDay: function(date){
        return [(date.getDay() == 1), ""]; },
    onSelect: function(){
    $("#order_form").submit();
    alert("awef");}
    });
});
