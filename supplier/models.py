from django.db import models

# Create your models here.
from django.urls import reverse


class Supplier(models.Model):
    class Meta:
        permissions = (("can_access_supplier","Can access Supplier"),)
        default_permissions = ()



class ProductforWeek(models.Model):
    name = models.CharField(default='',max_length=64)
    supplier = models.ForeignKey('core.Supplier',on_delete=models.SET_NULL,null=True)
    date = models.DateField(verbose_name="Date For")
    products = models.ManyToManyField('core.Product',related_name="supplier_products")
    active = models.BooleanField('Active',default=False)

    def get_absolute_url(self):
        return reverse('supplier')