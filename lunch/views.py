from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Order
from django.views.generic import DetailView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class OrdersOfUserListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'lunch/orders_list_of_user.html'
    paginate_by = 10

    def get_queryset(self):
        return Order.objects.filter(user_id=self.request.user)


class OrderListView(ListView):
    model = Order
    paginate_by = 10


class OrderDetailView(DetailView):
    model = Order


class OrderCreate(CreateView):
    model = Order
    fields = '__all__'


class OrderUpdate(UpdateView):
    model = Order
    fields = '__all__'


class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('order')

