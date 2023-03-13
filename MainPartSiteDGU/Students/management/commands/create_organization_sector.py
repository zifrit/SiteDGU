from django.core.management import BaseCommand
from Students.models import *


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        direction = ['Кураторы',
                     'Пресса',
                     'Интеллектуальный сектор',
                     ]
        for d in direction:
            OrganizationSector.objects.get_or_create(name=d)
        self.stdout.write(self.style.SUCCESS('Success create organization sector'))
