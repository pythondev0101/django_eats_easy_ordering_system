from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Order(models.Model):
    """Blueprint for Order object"""
    weekorder = models.ForeignKey('human_resource.OrderForWeek',on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=255,default='')
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    total = models.DecimalField(max_digits=9,decimal_places=2,verbose_name='Total')

    ORDER_STATUS = (('new', 'New'),('received', 'Received'),('ordered', 'Ordered'),('cancelled', 'Cancelled'))
    status = models.CharField(max_length=10,choices=ORDER_STATUS,blank=True, verbose_name='Status',default='new')
    date = models.DateField(null=True)

    def get_absolute_url(self):
        return reverse('order-detail', args=[str(self.id)])


class OrderLine(models.Model):
    order = models.ForeignKey('Order',on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey('core.Product',on_delete=models.SET_NULL,null=True)
    date = models.DateField(verbose_name="Date",null=True)





