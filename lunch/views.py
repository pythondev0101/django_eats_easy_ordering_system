from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Order, OrderLine
from django.views.generic import DetailView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from extra_views import CreateWithInlinesView,InlineFormSetFactory
from .forms import OrderLineFormSet
import datetime
from pprint import pprint
from human_resource.models import OrderForWeek

# Create your views here.


class OrdersOfUserListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'lunch/orders_list_of_user.html'
    paginate_by = 50

    def get_queryset(self):
        return Order.objects.filter(user_id=self.request.user)


class OrderListView(ListView):
    model = Order
    paginate_by = 10


class OrderDetailView(DetailView):
    model = Order

    def get_context_data(self, **kwargs):
        context = super(OrderDetailView, self).get_context_data(**kwargs)
        orderline = OrderLine.objects.filter
        return context


class OrderLineInline(InlineFormSetFactory):
    model = OrderLine
    fields = ['product', 'date']


class CreateOrderView(CreateView):
    model = Order
    fields = ('name',)
    template_name = 'lunch/order_form.html'

    def get_context_data(self, **kwargs):
        data = super(CreateOrderView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['orderlines'] = OrderLineFormSet(self.request.POST)
        else:
            try:
                order = OrderForWeek.objects.filter(status='active').latest('date')
                data['order'] = order
                data['mondays'] = order.monday.all()
                data['tuesdays'] = order.tuesday.all()
                data['wednesdays'] = order.wednesday.all()
                data['thursdays'] = order.thursday.all()
                data['fridays'] = order.friday.all()
            except Exception as e:
                pass
            data['orderlines'] = OrderLineFormSet()
        return data

    def form_valid(self, form):
        total_price = 0
        form.instance.total = 0  # this is for initial data only
        form.instance.date = datetime.datetime.now() # this is for initial data only
        context = self.get_context_data()
        orderlines = context['orderlines']
        # pprint(orderlines.data)
        # for key, val in orderlines.data.items():
        #     print(key, "==",val)
        #     if key:
        if orderlines.is_valid():
            for f in orderlines:
                cd = f.cleaned_data
                if cd:
                    pprint(vars(cd['product']))
                    total_price = total_price + cd['product'].price

            self.object = form.save()
            orderlines.instance = self.object
            orderlines.save()
            #ORDER FORM
            form.instance.user = self.request.user
            form.instance.total = total_price
            form.instance.save()
        return super(CreateOrderView, self).form_valid(form)

# class CreateOrderView(CreateWithInlinesView):
#     model = Order
#     fields = ('total','status','date')
#     inlines = [OrderLineInline]
#     template_name = 'lunch/order_form.html'
#
#     def forms_valid(self, form, inlines):
#         # TODO: order name
#         form.instance.user = self.request.user
#         form.instance.save()
#         return super(CreateOrderView, self).forms_valid(form,inlines)


class OrderUpdate(UpdateView):
    model = Order
    fields = '__all__'


class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('order')

