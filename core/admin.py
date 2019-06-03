from django.contrib import admin
from core.models import *

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(FeedBack)
admin.site.site_header = "Eats Easy Ordering Administration"


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    filter_horizontal = ('user',)


