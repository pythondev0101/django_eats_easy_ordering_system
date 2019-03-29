from django.contrib import admin
from .models import Order,OrderLine
# Register your models here.


class OrderLineInline(admin.StackedInline):
    model = OrderLine


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderLineInline]
    list_display = ('user','weekorder','total','status','date')

