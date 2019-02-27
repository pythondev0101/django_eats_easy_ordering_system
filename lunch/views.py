from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Order
from django.views.generic import DetailView,ListView
# Create your views here.


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

