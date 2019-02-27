from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Order
import datetime


class OrderForm(forms.Form):
    """ TEST """
    order_date = forms.DateField(help_text="Date of Order",required=True)

    def clean_order_date(self):
        data = self.cleaned_data['order_date']
        if data < datetime.date.today():
            raise ValidationError('Invalid date')

        return data


class OrderModelForm(ModelForm):
    def clean_date(self):
        data = self.cleaned_data['date']

        return data

    class Meta:
        model = Order
        fields = '__all__'


