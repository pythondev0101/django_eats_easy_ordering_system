from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer,ProductSerializer
from .models import Product
# Create your views here.


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def index(request):
    """View function returning the home page"""

    return render(request,'index.html')



