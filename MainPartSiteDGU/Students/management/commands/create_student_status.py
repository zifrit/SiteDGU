from django.core.management import BaseCommand
from Students.models import *


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        direction = ['Без статуса',
                     'Стипендиант',
                     ]
        for d in direction:
            StatusStudent.objects.get_or_create(name=d)
        self.stdout.write(self.style.SUCCESS('Success create status student'))
