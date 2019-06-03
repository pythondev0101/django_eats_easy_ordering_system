from django.contrib import admin
from .models import OrderForWeek
# Register your models here.



@admin.register(OrderForWeek)
class OrderForWeekAdmin(admin.ModelAdmin):
    filter_horizontal = ('monday','tuesday','wednesday','thursday','friday')
    raw_id_fields = ('supply',)
    fieldsets = (
        (None, {
            'fields': (('name', 'status'), 'date','supply')
        }),
        ('Dates', {
            'fields': ('monday', 'tuesday','wednesday','thursday','friday')
        })
    )