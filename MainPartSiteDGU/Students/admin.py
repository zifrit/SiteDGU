from django.contrib.admin.forms import AdminPasswordChangeForm
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

# Register your models here.


admin.site.register(StatusStudent)
# admin.site.register(TypeDirection)
# admin.site.register(CustomUser, UserAdmin)
# admin.site.register(Events)
admin.site.register(OrganizationSector)


# admin.site.register(Test)

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


@admin.register(Events)
class AdminEvents(admin.ModelAdmin):
    list_display = ['name',
                    'id',
                    'date',
                    'user']
    list_filter = ['date']


@admin.register(TypeDirection)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']
#     list_display = ("name", "date", "view_students_link")
#
#     def view_students_link(self, obj):
#         return re
#         # count = obj.customuser_set.count()
#         # url = (
#         #         reverse("admin:core_person_changelist")
#         #         + "?"
#         #         + urlencode({"courses__id": f"{obj.id}"})
#         # )
#         # return format_html('<a href="{}">{} Students</a>', url, count)
