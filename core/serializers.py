from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','url', 'username', 'email', 'is_staff')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('name','description')




