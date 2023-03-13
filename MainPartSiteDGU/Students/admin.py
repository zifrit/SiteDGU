from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

admin.site.register(StatusStudent)

# admin.site.register(CustomUser, UserAdmin)

admin.site.register(OrganizationSector)


@admin.register(ProfileStudent)
class AdminProfileStudent(admin.ModelAdmin):
    list_display = [
        'student',
        'id',
        'direction',
        'course',

    ]
    list_display_links = ['id', 'student']


@admin.register(CustomUser)
class AdminStudent(UserAdmin):
    list_display = ['username',
                    'id',
                    'roles',
                    'is_active',
                    'is_staff']
    list_filter = ['roles']
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        (_('Personal info'), {
            'fields': ('first_name', 'last_name', 'middle_name', 'email', 'roles')
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {
            'fields': ('last_login', 'date_joined')
        }),
    )


@admin.register(TypeDirection)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']
