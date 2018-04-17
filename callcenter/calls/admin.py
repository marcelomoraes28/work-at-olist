from django.contrib import admin
from .models import Cost


class CostAdmin(admin.ModelAdmin):
    list_display = ('connection_cost', 'cost_per_minute', 'initial_period',
                    'end_period', 'status')
    list_filter = ('status',)

admin.site.register(Cost, CostAdmin)