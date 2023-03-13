from django.contrib import admin

from .models import Events


@admin.register(Events)
class AdminEvents(admin.ModelAdmin):
    list_display = ['name',
                    'id',
                    'date',
                    'user']
    list_filter = ['date']
