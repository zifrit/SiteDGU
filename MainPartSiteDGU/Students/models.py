from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

# def directory_path(instance, filename):
#     return f'photo/%Y/%m.%d/{filename}'

class CustomUser(AbstractUser):
    ROLES = (
        ('T', 'Преподаватель'),
        ('S', 'Студент'),
        ('E', 'Староста'),
    )
    roles = models.CharField(choices=ROLES,
                             max_length=2,
                             blank=True,
                             null=True,
                             )

    class Meta:
        db_table = 'Dj_CUser'

    def __str__(self):
        return f'{self.username}'


class InfoStudent(models.Model):
    name = models.CharField(max_length=255,
                                  verbose_name='Имя'
                                  )
    last_name = models.CharField(max_length=255,
                                 verbose_name='Фамилия'
                                 )
    middle_name = models.CharField(max_length=255,
                                   verbose_name='Отчество'
                                   )

    direction = models.ForeignKey(to='Students.TypeDirection',
                                  verbose_name='Направление',
                                  on_delete=models.CASCADE,
                                  default=1
                                  )
    TYPE_STATUS = (
        (1, '1-курс'),
        (2, '2-курс'),
        (3, '3-курс'),
        (4, '4-курс'),
    )
    course = models.IntegerField(choices=TYPE_STATUS,
                                 default=0
                                 )
    student_status = models.ForeignKey(to='Students.StatusStudent',
                                       verbose_name='статус студента',
                                       on_delete=models.CASCADE,
                                       default=1
                                       )
    photo_student = models.FileField(upload_to='photo/%Y/%m.%d/',
                                     verbose_name='фото студента'
                                     )
    social_status = models.BooleanField(verbose_name='социальная справка',
                                        )
    time_create = models.DateTimeField(auto_now_add=True,
                                       verbose_name='дата создания'
                                       )
    time_update = models.DateTimeField(auto_now=True,
                                       verbose_name='дата изменения'
                                       )

    class Meta:
        db_table = 'InfoStudent'

    def get_full_name(self):
        return f'{self.last_name} {self.name} {self.middle_name}'

    def __str__(self):
        return f'{self.name} {self.last_name}'


class StatusStudent(models.Model):
    name = models.CharField(verbose_name='статус',
                            max_length=255,
                            )

    class Meta:
        db_table = 'StatusStudent'

    def __str__(self):
        return self.name


class TypeDirection(models.Model):
    name = models.CharField(verbose_name='Направление',
                            max_length=255,
                            )

    class Meta:
        db_table = 'TypeDirection'

    def __str__(self):
        return self.name
