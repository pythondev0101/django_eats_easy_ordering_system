from django.db import models
from django.urls import reverse

from core.models import Product

# Create your models here.


class HumanResource(models.Model):
    class Meta:
        permissions = (("can_access_hr","Can access HR"),)
        default_permissions = ()


class OrderForWeek(models.Model):
    name = models.CharField(max_length=255,default='')
    ORDER_STATUS = (('active', 'Active'),('ordered', 'Ordered'))
    status = models.CharField(max_length=10,choices=ORDER_STATUS,blank=True, verbose_name='Status',default='new')
    date = models.DateField()
    supply = models.ForeignKey('supplier.ProductforWeek', on_delete=models.SET_NULL, null=True,)
    monday = models.ManyToManyField('core.Product',related_name="monday_order")
    tuesday = models.ManyToManyField('core.Product',related_name="tuesday_order")
    wednesday = models.ManyToManyField('core.Product',related_name="wednesday_order")
    thursday = models.ManyToManyField('core.Product',related_name="thursday_order")
    friday = models.ManyToManyField('core.Product',related_name="friday_order")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
         return reverse('human_resource')

# #
# class Book(models.Model):
#     publication = models.ForeignKey(Publication)
#     writer = ChainedManyToManyField(
#         Writer,
#         horizontal=True,
#         verbose_name='writer',
#         chained_field="publication",
#         chained_model_field="publications")
#     name = models.CharField(max_length=255)
# class OrderProductWeek(models.Model):
#     product = models.ForeignKey('core.Product', on_delete=models.CASCADE)
#     orderforweek=models.ForeignKey(OrderForWeek,on_delete=models.CASCADE)


# class OrderProductForWeek(models.Model):
#     orderweek = models.ForeignKey('OrderForWeek',on_delete=models.SET_NULL,null=True)
#     monday = models.ForeignKey('core.Product',related_name="monday_order",on_delete=models.SET_NULL,null=True)
#     tuesday = models.ForeignKey('core.Product',related_name="tuesday_order",on_delete=models.SET_NULL,null=True)
#     wednesday = models.ForeignKey('core.Product',related_name="wednesday_order",on_delete=models.SET_NULL,null=True)
#     thursday = models.ForeignKey('core.Product',related_name="thursday_order",on_delete=models.SET_NULL,null=True)
#     friday = models.ForeignKey('core.Product',related_name="friday_order",on_delete=models.SET_NULL,null=True)
