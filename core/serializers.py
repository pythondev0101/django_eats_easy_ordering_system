from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product
from lunch.models import Order,OrderLine
from human_resource.models import OrderForWeek
import pprint
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','url', 'username', 'email', 'is_staff')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name','image')


class HRSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = OrderForWeek
        fields = '__all__'



class HRActiveSerializer(serializers.ModelSerializer):
    class Meta:
        model= OrderForWeek
        fields = "__all__"


class OrderlineSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderLine
        fields = ('order','product','day')

class OrderSerializer(serializers.ModelSerializer):
    orderlines = OrderlineSerializer(source="orderline_set",many=True)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self,validated_data):
        lines = validated_data.pop('orderline_set')
        instance = Order.objects.create(**validated_data)
        for data in lines:
            data['order'] = instance
            profile = OrderLine.objects.create(**data)
        return instance
