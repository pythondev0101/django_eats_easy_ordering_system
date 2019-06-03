import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer,ProductSerializer,HRSerializer,OrderSerializer
from .models import Product, FeedBack
from human_resource.models import OrderForWeek
from lunch.models import Order
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class HRViewSet(viewsets.ModelViewSet):
    queryset = OrderForWeek.objects.all()
    serializer_class = HRSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

def index(request):
    """View function returning the home page"""

    return render(request,'index.html')

class CommentView(LoginRequiredMixin, CreateView):
    model = FeedBack
    fields = ('comment',)
    template_name = 'comments.html'

    # def get_success_url(self):
    #     return reverse('myorder-detail', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        data = super(CommentView, self).get_context_data(**kwargs)
        user = self.request.user
        comments = FeedBack.objects.filter(product=self.kwargs['pk'])
        data["comments"] = comments
        print(comments)
        return data


    def form_valid(self, form):
        form.instance.date = datetime.datetime.now()  # this is for initial data only
        form.instance.user = self.request.user
        form.instance.product = Product.objects.get(pk=self.kwargs['pk'])
        form.instance.save()
        return super(CommentView, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('comment', args=(self.kwargs['pk'],))

