from django.contrib import admin
from .models import Cost, Call


class CostAdmin(admin.ModelAdmin):
    list_display = ('connection_cost', 'cost_per_minute', 'initial_period',
                    'end_period', 'status')
    list_filter = ('status',)


class CallAdmin(admin.ModelAdmin):
    list_display = ('destination', 'source', 'call_id',
                    'call_type')
    list_filter = ('destination', 'source', 'call_id')


admin.site.register(Cost, CostAdmin)
admin.site.register(Call, CallAdmin)
