from django.contrib import admin
from .models import Call


class CallAdmin(admin.ModelAdmin):
    list_display = ('destination', 'source', 'call_id',
                    'type', 'timestamp')
    list_filter = ('destination', 'source', 'call_id', 'timestamp')

admin.site.register(Call, CallAdmin)
