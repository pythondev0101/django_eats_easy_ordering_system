from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer,ProductSerializer,HRSerializer,OrderSerializer
from .models import Product
from human_resource.models import OrderForWeek
from lunch.models import Order

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



