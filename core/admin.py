from django.contrib import admin
from core.models import *

# Register your models here.

admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Category)
admin.site.site_header = "Eats Easy Ordering Administration"

