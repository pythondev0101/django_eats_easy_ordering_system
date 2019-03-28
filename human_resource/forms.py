from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import OrderForWeek
from core.models import Product
from django.forms import inlineformset_factory


class WeekOrderLineForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


# WeekOrderLineFormSet = inlineformset_factory(OrderForWeek,OrderProductWeek,form=WeekOrderLineForm)
# WeekOrderLineFormSet = ""


