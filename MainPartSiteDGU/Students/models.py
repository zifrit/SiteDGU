from django.db import models
# Create your models here.


class InfoStudent(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=255, verbose_name='Отчество')
     
    student_status = models.ForeignKey(to=SS, verbose_name='статус студента', on_delete=models.CASCADE(), default=1)
    social_status = models.BooleanField(verbose_name='социальная справка')

