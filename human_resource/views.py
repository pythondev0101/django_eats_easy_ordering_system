from pprint import pprint

from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ModelForm
from django.urls import reverse
from django.views.generic import ListView, DetailView, TemplateView
from lunch.models import Order, OrderLine
from .models import OrderForWeek
from django.shortcuts import render
from functools import partial
import datetime
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from core.models import Product
from supplier.models import ProductforWeek
# from .forms import WeekOrderLineFormSet

# Create your views here.

class HRView(ListView):
    model = OrderForWeek
    template_name = 'human_resource/orderforweek_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HRView, self).get_context_data(**kwargs)
        context["supplies"] = ProductforWeek.objects.all()
        return context

class CreateWeekOrderForm(ModelForm):
    class Meta:
        model = OrderForWeek
        fields = ('name','date','status','monday','tuesday','wednesday','thursday','friday')

    def __init__(self, *args, **kwargs):
        supply = kwargs.pop('supply')
        super(CreateWeekOrderForm, self).__init__(*args, **kwargs)
        pkeys = ProductforWeek.objects.prefetch_related("products").filter(active=True).filter(pk=supply).values_list('products',flat=True)
        ckeys = Product.objects.filter(id__in=pkeys)
        self.fields['monday'].queryset=ckeys
        self.fields['tuesday'].queryset=ckeys
        self.fields['wednesday'].queryset=ckeys
        self.fields['thursday'].queryset=ckeys
        self.fields['friday'].queryset=ckeys

class CreateWeekOrderView(CreateView):
    model = OrderForWeek
    form_class = CreateWeekOrderForm
    template_name = 'human_resource/week_order_form.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CreateWeekOrderView, self).get_context_data(**kwargs)

        return context

    def get_form_kwargs(self):
        kwargs = super(CreateWeekOrderView, self).get_form_kwargs()
        kwargs['supply'] = self.request.GET.get('supply','')
        return kwargs

    def form_valid(self, form):
        form.instance.supply = ProductforWeek.objects.get(pk=self.request.GET.get('supply',''))
        form.instance.save()
        return super(CreateWeekOrderView, self).form_valid(form)


class UpdateWeekOrderView(UpdateView):
    model = OrderForWeek
    form_class = CreateWeekOrderForm
    template_name = 'human_resource/update_week_order_form.html'

    def get_absolute_url(self):
        return reverse('human_resource')

    def get_form_kwargs(self):
        kwargs = super(UpdateWeekOrderView, self).get_form_kwargs()
        kwargs['supply'] = self.get_object().supply.id
        return kwargs


def report_view(request):

    return render(request,'reports.html')


from easy_pdf.views import PDFTemplateView, PDFTemplateResponseMixin


class OrderPdfView(PDFTemplateView):

    def get_context_data(self, **kwargs):
        context = super(OrderPdfView, self).get_context_data(**kwargs)
        report = self.request.GET.get('report','')
        if report == "orderbyfood":
            print("orderbyfood")
            order =self.request.GET.get('order','')
            food = self.request.GET.get('food','')
            day = self.request.GET.get('day','')
            if day == "all":
                orders = OrderLine.objects.select_related("order").filter(order__weekorder=order).filter(product=food)
            else:
                orders = OrderLine.objects.select_related("order").filter(order__weekorder=order).filter(product=food).filter(day=day)

            context["orders"] = orders
            order = Order.objects.get(pk=order)
            food = Product.objects.get(pk=food)
            context["ordername"]= order.name
            context["food"] =food.name
            context["count"] = orders.count()

        elif report == "foodsummary":
            print("foodsummary")
            nc = {}
            order =self.request.GET.get('order','')
            day = self.request.GET.get('day','')
            if day == "all":
                orders = OrderLine.objects.filter(order__weekorder=order)
            else:
                orders = OrderLine.objects.select_related("order").filter(order__weekorder=order).filter(day=day)

            for qry in orders.iterator():
                print("start")
                print(qry.product.name)
                count = OrderLine.objects.filter(order__weekorder=order).filter(product=qry.product.id).count()
                print("end")
                if qry.product.name not in nc:
                    nc[qry.product.name] = count
            ncs = [(k, nc[k]) for k in sorted(nc, key=nc.get, reverse=True)]
            print(ncs)
            context["orders"] = ncs
            order = Order.objects.get(pk=order)
            context["ordername"]= order.name
            context["count"] = orders.count()

        return context

    def get_template_names(self):
        report =self.request.GET.get('report', '')
        if report == "orderbyfood":
            return ["order_by_food_pdf.html"]
        elif report == "foodsummary":
            return ["food_summary_pdf.html"]



class FoodSummaryView(TemplateView):
    template_name = 'human_resource/food_summary.html'

    def get_context_data(self, **kwargs):
        context = super(FoodSummaryView, self).get_context_data(**kwargs)
        context['orders'] = OrderForWeek.objects.all()
        context['products'] = Product.objects.all()
        print(context['orders'])
        return context

class TodayOrderView(TemplateView):
    template_name = 'human_resource/today_order_report.html'

    def get_context_data(self, **kwargs):
        context = super(TodayOrderView, self).get_context_data(**kwargs)
        context['orders'] = OrderForWeek.objects.all()
        print(context['orders'])
        return context

class OrderByFoodView(TemplateView):
    template_name = 'human_resource/order_by_food.html'

    def get_context_data(self, **kwargs):
        context = super(OrderByFoodView, self).get_context_data(**kwargs)
        context['orders'] = OrderForWeek.objects.all()
        context['products'] = Product.objects.all()
        print(context['orders'])
        return context






#
# DateInput = partial(forms.DateInput, {'class': 'datepicker'})
#
# class DateRangeForm(forms.Form):
#     start_date = forms.DateField(widget=DateInput())
#     end_date = forms.CharField()
#
# class HRView(ListView):
#     template_name = 'human_resource/order_list.html'
#     paginate_by = 50
#
#     def get_queryset(self):
#         today = datetime.date.today()
#         last_monday = today - datetime.timedelta(days=today.weekday())
#         last_friday = last_monday + datetime.timedelta(days=4)
#         if self.request.GET:
#             filter_val = self.request.GET.get('start_date')
#             print("!!!!!!!!!!!!!!!!!!")
#             filter_val = datetime.datetime.strptime(filter_val, '%m/%d/%Y')
#             print(filter_val)
#             last_friday = filter_val + datetime.timedelta(days=4)
#             return Order.objects.filter(date__range=[filter_val, last_friday])
#         print("????????????")
#         return Order.objects.filter(date__range=[last_monday, last_friday])
#
#     def get_context_data(self, **kwargs):
#         today = datetime.date.today()
#         last_monday = today - datetime.timedelta(days=today.weekday())
#         context = super(HRView, self).get_context_data(**kwargs)
#         context['form'] = DateRangeForm()
#         context['form'].fields['start_date'].initial = last_monday
#         context['form'].fields['end_date'].initial = last_monday
#         return context
