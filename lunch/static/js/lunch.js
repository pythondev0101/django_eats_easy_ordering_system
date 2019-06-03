if (!$){
    $ = django.jQuery;
}

$(function(){
    if ($('#form_name').length){
        var new_date = new Date();
        var up_date = new_date.getMonth() + 1;

        var name_val = "Order for " + up_date + '_' + new_date.getDate();
        $('#id_name').val(name_val);
        $('#id_orderline_set-0-day').val('monday');
        $('#id_orderline_set-1-day').val('tuesday');
        $('#id_orderline_set-2-day').val('wednesday');
        $('#id_orderline_set-3-day').val('thursday');
        $('#id_orderline_set-4-day').val('friday');
    }

    $("img").dblclick(function(event) {
      var id = event.target.id;
      var updatedid = parseInt(id.substring(4));
      $.ajax({
        url: "/ajax/getproduct/",
        type : 'get',
        data: {
          'id': updatedid
        },
        dataType: 'json',
        success: function (data) {
          if (data.product) {
            var obj = $.parseJSON(data.product)
            alert(obj[0].fields.description);
          }
        }
      });
    });
});

[{"model": "core.product", "pk": 9,
"fields": {"name": "Nilagang Baka", "description": "Beef\r\n\r\nCalories from Fat 41. Calories 179.\r\n7% Total Fat 4.5g.\r\n9% Saturated Fat 1.8g.\r\n9% Cholesterol 27mg.\r\n10% Sodium 250mg.\r\n19% Potassium 648mg.", "price": "50.00", "active": true, "supplier": 3, "category": 1, "image": "products/baka.jpg"}}]
