from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(StatusStudent)
admin.site.register(TypeDirection)

@admin.register(InfoStudent)
class AdminInfoStudent(admin.ModelAdmin):
    list_display = [
        'last_name',
        'first_name',
        'direction',
        'course',

    ]
    list_filter = ['time_create',]
