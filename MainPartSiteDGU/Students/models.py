from django.db import models


# Create your models here.

def directory_path(instance, filename):
    return f'photo/%Y/%m.%d/'


class InfoStudent(models.Model):
    first_name = models.CharField(
        max_length=255, verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=255, verbose_name='Фамилия'
    )
    middle_name = models.CharField(
        max_length=255, verbose_name='Отчество'
    )

    direction = models.ForeignKey(
        to='TypeCourse',
        verbose_name='Направление',
        on_delete=models.CASCADE,
    )
    TYPE_STATUS = (
        (1, '1-курс'),
        (2, '2-курс'),
        (3, '3-курс'),
        (4, '4-курс'),
    )
    course = models.IntegerField(
        choices=TYPE_STATUS,
        default=0
    )
    photo_student = models.FileField(
        upload_to=directory_path,
        verbose_name='фото студента'
    )
    student_status = models.ForeignKey(
        to='StatusStudent',
        verbose_name='статус студента',
        on_delete=models.CASCADE,
        default=1
    )
    social_status = models.BooleanField(
        verbose_name='социальная справка'
    )

    class Meta:
        db_table = 'InfoStudent'


class StatusStudent(models.Model):
    name = models.CharField(
        verbose_name='статус',
        max_length=255,
    )

    class Meta:
        db_table = 'StatusStudent'


class TypeCourse(models.Model):
    name = models.CharField(
        verbose_name='Направление',
        max_length=255,
    )

    class Meta:
        db_table = 'TypeCourse'
