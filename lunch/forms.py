from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Order,OrderLine
from django.forms import inlineformset_factory,RadioSelect


class OrderLineForm(ModelForm):
    class Meta:
        model = OrderLine
        fields = ('product','day')
        widgets = {
            'product': RadioSelect(attrs={'cols': 80, 'rows': 20}),
        }

OrderLineFormSet = inlineformset_factory(Order,OrderLine,form=OrderLineForm, extra=5)





# class OrderForm(ModelForm):
#
#     class Meta:
#         model = Order
#         fields = ('total', 'status', 'date')
#
#     def __init__(self, *args, **kwargs):
#         super(OrderForm, self).__init__(*args,**kwargs)
#         self.fields['status'].widget.attrs['readonly'] = True
#

# class OrderForm(forms.Form):
#     """ TEST """
#     order_date = forms.DateField(help_text="Date of Order",required=True)
#
#     def clean_order_date(self):
#         data = self.cleaned_data['order_date']
#         if data < datetime.date.today():
#             raise ValidationError('Invalid date')
#
#         return data
#
#
# class OrderModelForm(ModelForm):
#     def clean_date(self):
#         data = self.cleaned_data['date']
#
#         return data
#
#     class Meta:
#         model = Order
#         fields = '__all__'


