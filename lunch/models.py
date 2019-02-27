from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Order(models.Model):
    """Blueprint for Order object"""

    name = models.CharField(max_length=255,default='')
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    total = models.DecimalField(max_digits=9,decimal_places=2,verbose_name='Total')
    status = models.CharField(max_length=10,verbose_name='Status')
    supplier_id = models.ForeignKey('core.Supplier',verbose_name='Supplier',on_delete=models.SET_NULL,null=True)
    date = models.DateField()

    def get_absolute_url(self):
        return reverse('order-detail', args=[str(self.id)])


class OrderLine(models.Model):
    order_id = models.ForeignKey('Order',on_delete=models.SET_NULL,null=True)
    product_id = models.ForeignKey('core.Product',on_delete=models.SET_NULL,null=True)
    date = models.DateField(verbose_name="Date",null=True)





