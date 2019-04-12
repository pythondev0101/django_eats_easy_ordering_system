from django.contrib import admin
from .models import Order,OrderLine
# Register your models here.


class OrderLineInline(admin.TabularInline):
    model = OrderLine
    fields = ('product','date',)
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderLineInline]
    list_display = ('user','weekorder','total','status','date')
    list_filter = ['weekorder','date']

