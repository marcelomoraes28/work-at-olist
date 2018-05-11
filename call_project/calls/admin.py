from django.contrib import admin
from .models import Cost, Call, Bill


class CostAdmin(admin.ModelAdmin):
    list_display = ('connection_cost', 'cost_per_minute', 'initial_period',
                    'end_period', 'status')
    list_filter = ('status',)


class CallAdmin(admin.ModelAdmin):
    list_display = ('destination', 'source', 'call_id',
                    'call_type', 'timestamp')
    list_filter = ('destination', 'source', 'call_id', 'timestamp')


class BillAdmin(admin.ModelAdmin):
    list_display = ('destination', 'call_id', 'call_start_date',
                    'call_start_time', 'call_price')
    list_filter = ('destination', 'call_id')


admin.site.register(Call, CallAdmin)
admin.site.register(Cost, CostAdmin)
admin.site.register(Bill, BillAdmin)
