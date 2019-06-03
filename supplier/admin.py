from django.contrib import admin
from .models import ProductforWeek

# Register your models here.
# Register your models here.



@admin.register(ProductforWeek)
class ProductForWeekAdmin(admin.ModelAdmin):
    filter_horizontal = ('products',)
