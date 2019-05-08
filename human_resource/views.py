from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from lunch.models import Order, OrderLine
from .models import OrderForWeek
from django.shortcuts import render
from functools import partial
import datetime
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from .forms import WeekOrderLineFormSet

# Create your views here.

DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class DateRangeForm(forms.Form):
    start_date = forms.DateField(widget=DateInput())
    end_date = forms.CharField()

class HRView(ListView):
    template_name = 'human_resource/order_list.html'
    paginate_by = 50

    def get_queryset(self):
        today = datetime.date.today()
        last_monday = today - datetime.timedelta(days=today.weekday())
        last_friday = last_monday + datetime.timedelta(days=4)
        if self.request.GET:
            filter_val = self.request.GET.get('start_date')
            print("!!!!!!!!!!!!!!!!!!")
            filter_val = datetime.datetime.strptime(filter_val, '%m/%d/%Y')
            print(filter_val)
            last_friday = filter_val + datetime.timedelta(days=4)
            return Order.objects.filter(date__range=[filter_val, last_friday])
        print("????????????")
        return Order.objects.filter(date__range=[last_monday, last_friday])

    def get_context_data(self, **kwargs):
        today = datetime.date.today()
        last_monday = today - datetime.timedelta(days=today.weekday())
        context = super(HRView, self).get_context_data(**kwargs)
        context['form'] = DateRangeForm()
        context['form'].fields['start_date'].initial = last_monday
        context['form'].fields['end_date'].initial = last_monday
        return context


class CreateWeekOrderView(CreateView):
    model = OrderForWeek
    fields = '__all__'
    template_name = 'human_resource/week_order_form.html'

    # def get_context_data(self, **kwargs):
    #     data = super(CreateWeekOrderView, self).get_context_data(**kwargs)
    #     if self.request.POST:
    #         data['weekorderlines'] = WeekOrderLineFormSet(self.request.POST)
    #     else:
    #         data['weekorderlines'] = WeekOrderLineFormSet()
    #     return data

    # def form_valid(self, form):
    #     total_price = 0
    #     form.instance.total = 0  # this is for initial data only
    #     form.instance.date = datetime.datetime.now() # this is for initial data only
    #     context = self.get_context_data()
    #     orderlines = context['orderlines']
    #     # pprint(orderlines.data)
    #     # for key, val in orderlines.data.items():
    #     #     print(key, "==",val)
    #     #     if key:
    #     if orderlines.is_valid():
    #         for f in orderlines:
    #             cd = f.cleaned_data
    #             if cd:
    #                 (vars(cd['product']))
    #                 total_price = total_price + cd['product'].price
    #
    #         self.object = form.save()
    #         orderlines.instance = self.object
    #         orderlines.save()
    #         #ORDER FORM
    #         form.instance.user = self.request.user
    #         form.instance.total = total_price
    #         form.instance.save()
    #     return super(CreateOrderView, self).form_valid(form)

# class MyView(ListView):
#     model = Update
#     template_name = "updates/update.html"
#     paginate_by = 10
#
#     def get_queryset(self):
#         filter_val = self.request.GET.get('filter', 'give-default-value')
#         order = self.request.GET.get('orderby', 'give-default-value')
#         new_context = Update.objects.filter(
#             state=filter_val,
#         ).order_by(order)
#         return new_context
#
#     def get_context_data(self, **kwargs):
#         context = super(MyView, self).get_context_data(**kwargs)
#         context['filter'] = self.request.GET.get('filter', 'give-default-value')
#         context['orderby'] = self.request.GET.get('orderby', 'give-default-value')
#         return context
#
# class InventoryListView(ListView):
#     template_name ='system/inventory_list.html'
#     context_object_name = 'inventorys'
#     model = models.Inventory
#
#     def get_context_data(self, **kwargs)
#         context = super(InventoryListView, self).get_context_data(**kwargs)
#         context['form'] = InventoryForm()
#         return context

# class CreateOrderView(CreateView):
#     model = Order
#     fields = ('name',)
#     template_name = 'lunch/order_form.html'
#
#     def get_context_data(self, **kwargs):
#         data = super(CreateOrderView, self).get_context_data(**kwargs)
#         if self.request.POST:
#             data['orderlines'] = OrderLineFormSet(self.request.POST)
#         else:
#             data['orderlines'] = OrderLineFormSet()
#         return data
#
#     def form_valid(self, form):
#         total_price = 0
#         form.instance.total = 0  # this is for initial data only
#         form.instance.date = datetime.datetime.now() # this is for initial data only
#         context = self.get_context_data()
#         orderlines = context['orderlines']
#         # pprint(orderlines.data)
#         # for key, val in orderlines.data.items():
#         #     print(key, "==",val)
#         #     if key:
#         if orderlines.is_valid():
#             for f in orderlines:
#                 cd = f.cleaned_data
#                 if cd:
#                     pprint(vars(cd['product']))
#                     total_price = total_price + cd['product'].price
#
#             self.object = form.save()
#             orderlines.instance = self.object
#             orderlines.save()
#             #ORDER FORM
#             form.instance.user = self.request.user
#             form.instance.total = total_price
#             form.instance.save()
#         return super(CreateOrderView, self).form_valid(form)
