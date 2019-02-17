from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from django.contrib.auth.models import User
import logging

# Create your models here.

logger = logging.getLogger(__name__)


@receiver(signals.pre_save,sender=User)
def pre_create_of_user(sender,instance,**kwargs):
    if instance._state.adding:
        instance.is_active = False


class Base(models.Model):
    """Base Fields"""

    class Meta:
        abstract = True


class Product(models.Model):
    """Blueprint for Product Model"""

    name = models.CharField(max_length=50, verbose_name="Product name", help_text="Enter the product name")
    description = models.TextField(max_length=1000, verbose_name="Description",
                                   help_text="Enter the product description", null=True, )
    price = models.DecimalField(max_digits=9, verbose_name="Price", decimal_places=2, null=True, )
    active = models.BooleanField(verbose_name="Active", default=True, help_text="Is active?", )
    supplier = models.ForeignKey('Supplier', verbose_name='Supplier', on_delete=models.SET_NULL, null=True,
                                 help_text="Select the product's supplier")
    category = models.ForeignKey('Category', verbose_name='Category', on_delete=models.SET_NULL, null=True,
                                 help_text="Select the product's category")

    def __str__(self):
        """Function returning a string representation of the product object"""
        return self.name

    def get_absolute_url(self):
        pass


class Supplier(models.Model):
    """Blueprint for Supplier model"""

    name = models.CharField(max_length=50, verbose_name="Supplier", help_text="Enter the supplier's name")
    address = models.CharField(max_length=50, verbose_name='Address', help_text="Enter the supplier's address",blank=True)
    phone = models.CharField(max_length=50,verbose_name='Phone',help_text="Enter the supplier's phone",blank=True)
    fax = models.CharField(max_length=50,verbose_name='Fax',help_text="Enter the supplier's fax",blank=True)
    email = models.CharField(max_length=50,verbose_name='Email',help_text="Enter the supplier's email",blank=True)

    def __str__(self):
        """Function returning a string representation of the supplier object"""
        return self.name


class Category(Base):
    """Blueprint for Category model"""

    name = models.CharField(max_length=50, verbose_name="Category", help_text="Enter the category name", )
    description = models.TextField(max_length=1000, verbose_name="Description",
                                   help_text="Enter the product description", null=True, )

    class Meta:
        abstract = False
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Function returning a string representation of the category object"""
        return self.name
