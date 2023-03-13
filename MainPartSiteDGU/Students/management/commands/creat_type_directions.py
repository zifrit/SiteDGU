from django.core.management import BaseCommand
from Students.models import *


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        direction = ['ПИЭ',
                     'ПИМ',
                     'ИСиТ',
                     'ИСиП',
                     'ИБ',
                     'ПИВЭУ',
                     ]
        for d in direction:
            TypeDirection.objects.get_or_create(name=d)
        self.stdout.write(self.style.SUCCESS('Success create type direction'))
