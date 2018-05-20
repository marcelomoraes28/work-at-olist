from django.contrib import admin
from .models import Bill


class BillAdmin(admin.ModelAdmin):
    list_display = (
        'destination', 'call_id', 'call_start_date', 'call_start_time',
        'call_price')
    list_filter = ('destination', 'call_id')


admin.site.register(Bill, BillAdmin)
