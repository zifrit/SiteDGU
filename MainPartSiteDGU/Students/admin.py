from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(StatusStudent)
admin.site.register(TypeDirection)
admin.site.register(CustomUser)
# admin.site.register(Test)

@admin.register(InfoStudent)
class AdminInfoStudent(admin.ModelAdmin):
    list_display = [
        'last_name',
        'name',
        'direction',
        'course',

    ]
    list_filter = ['time_create',]
