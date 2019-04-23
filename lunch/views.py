from django.core.exceptions import ValidationError
from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Order, OrderLine
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from extra_views import CreateWithInlinesView, InlineFormSetFactory
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
        # d = Order.orderline_set.objects.all()
        # d = OrderLine.objects.select_related('order').get(id=self.kwargs['pk'])
        order = Order.objects.get(id=self.kwargs['pk'])
        orderlines = order.orderline_set.all()
        print(orderlines[0].product)
        # y = x.p_perm
        context['orderlines'] = orderlines
        # print("!!!!!!!!!!!")
        # print(context['order'].weekorder_id.monday.name)
        # for x in context['order'].weekorder.values():
        #      print(x)
        return context


class OrderLineInline(InlineFormSetFactory):
    model = OrderLine
    fields = ['product', 'date', 'day']


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
                check = Order.objects.filter(user=self.request.user, weekorder=order).count()
                data['check'] = check
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
        order = OrderForWeek.objects.filter(status='active').latest('date')
        print("awefzxcvzxc")

        num = order.id
        form.instance.total = 0  # this is for initial data only
        form.instance.date = datetime.datetime.now()  # this is for initial data only
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
                    # print(cd['day'])
                    total_price = total_price + cd['product'].price
            print("??????")
            self.object = form.save()
            orderlines.instance = self.object
            orderlines.save()
            # ORDER FORM
            print("!!!!!!!")
            form.instance.weekorder = order
            form.instance.user = self.request.user
            form.instance.total = total_price
            form.instance.save()
            return super(CreateOrderView, self).form_valid(form)
        else:
            print(orderlines.errors)
        return None


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


class OrderUpdateView(UpdateView):
    model = Order
    fields = '__all__'
    template_name = 'lunch/order_update_form.html'
    queryset = Order.objects.all()

    def get_context_data(self, **kwargs):
        data = super(OrderUpdateView, self).get_context_data(**kwargs)
        # BooksFormSet = inlineformset_factory(Author, Book, fields='__all__', extra=1)
        if self.request.POST:
            # Create a formset instance to edit an existing model object,
            # but use POST data to populate the formset.
            data['orderlines'] = OrderLineFormSet(self.request.POST, instance=self.get_object())
        else:
            # Create a formset with the data from model object and add it to context
            data['orderlines'] = OrderLineFormSet(instance=self.get_object())
            try:
                order = OrderForWeek.objects.filter(status='active').latest('date')
                check = Order.objects.filter(user=self.request.user, weekorder=order).count()
                data['check'] = check
                data['order'] = order
                data['mondays'] = order.monday.all()
                data['tuesdays'] = order.tuesday.all()
                data['wednesdays'] = order.wednesday.all()
                data['thursdays'] = order.thursday.all()
                data['fridays'] = order.friday.all()
            except Exception as e:
                pass
        return data

    def form_valid(self, form):
        print("!!!!!!!!!!")
        context = self.get_context_data()
        orderlines = context['orderlines']
        self.object = form.save()

        if orderlines.is_valid():
            orderlines.instance = self.object
            orderlines.save()
        else:
            print(orderlines.errors)
            context.update({'orderlines': orderlines})
            return self.render_to_response(context)

        return super(OrderUpdateView, self).form_valid(form)


    def get_object(self, queryset=None):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Order,id=id_)

class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('order')
