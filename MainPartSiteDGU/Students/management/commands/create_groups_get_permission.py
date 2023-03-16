from django.core.management import BaseCommand
from Students.models import *
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        perm_add_customuser = Permission.objects.get(codename='add_customuser')
        perm_change_customuser = Permission.objects.get(codename='change_customuser')
        perm_view_customuser = Permission.objects.get(codename='view_customuser')

        perm_view_events = Permission.objects.get(id=56)
        perm_add_events = Permission.objects.get(id=53)
        perm_change_events = Permission.objects.get(id=54)

        group1, created1 = Group.objects.get_or_create(name='Студент')
        group2, created2 = Group.objects.get_or_create(name='Ласточка')
        group3, created3 = Group.objects.get_or_create(name='Преподаватель')

        group1.permissions.add(perm_view_events, perm_add_events)
        group2.permissions.add(perm_view_events, perm_add_events, perm_view_customuser)
        group3.permissions.add(perm_view_events, perm_add_events, perm_view_customuser, perm_add_customuser,
                               perm_change_events, perm_change_customuser)

        self.stdout.write(self.style.SUCCESS('Success create group'))
