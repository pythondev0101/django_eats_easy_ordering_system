from django.contrib import admin
from .models import OrderForWeek
# Register your models here.



@admin.register(OrderForWeek)
class OrderForWeekAdmin(admin.ModelAdmin):
    filter_horizontal = ('monday','tuesday','wednesday','thursday','friday')
    fieldsets = (
        (None, {
            'fields': (('name', 'status'), 'date')
        }),
        ('Dates', {
            'fields': ('monday', 'tuesday','wednesday','thursday','friday')
        })
    )