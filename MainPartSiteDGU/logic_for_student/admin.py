from django.contrib import admin
from .models import Events


@admin.register(Events)
class AdminEvents(admin.ModelAdmin):
    list_display = ['id',
                    'name',
                    'date',
                    'user']
    list_filter = ['date']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    fieldsets = (
        (None, {
            'fields': ('name', 'user')
        }),
        (None, {
            'fields': ('text', 'photo', 'date', 'time')
        }),
    )

    def get_queryset(self, request):
        return Events.objects.select_related('user')
