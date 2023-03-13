from django.db import models
from django.urls import reverse
from Students.models import *


class Events(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название мероприятия')
    photo = models.FileField(upload_to='Events/%Y/%m.%d/', verbose_name='Фото мероприятия')
    text = models.TextField(verbose_name='текст')
    date = models.DateField(verbose_name='Дата мероприятия')
    time = models.TimeField(verbose_name='Время мероприятия')
    user = models.ForeignKey(to=CustomUser, verbose_name='Кто добавил', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'Events'

    def __str__(self):
        return self.name
