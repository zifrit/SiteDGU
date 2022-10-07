from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

# def directory_path(instance, filename):
#     return f'photo/%Y/%m.%d/{filename}'

class CustomUser(AbstractUser):
    ROLES = (
        ('T', 'Преподаватель'),
        ('S', 'Студент'),
        ('B', 'Ласточка'),
    )
    roles = models.CharField(choices=ROLES, max_length=2, blank=True,
                             default='S')

    class Meta:
        db_table = 'Dj_CUser'

    def __str__(self):
        return f'{self.username}'


class PersonalRoles(models.Model):
    name = models.CharField(verbose_name='Роли', max_length=255, )

    class Meta:
        db_table = 'PersonalRoles'

    def __str__(self):
        return self.name


class InfoStudent(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=255, verbose_name='Отчество')

    direction = models.ForeignKey(to='Students.TypeDirection', verbose_name='Направление', on_delete=models.CASCADE,
                                  default=1)
    TYPE_STATUS = (
        ('1', '1-курс'),
        ('1-1', '1-курс-академ'),
        ('1-2', '1-курс-магистратура'),
        ('2', '2-курс'),
        ('2-1', '2-курс-академ'),
        ('2-2', '2-курс-магистратура'),
        ('3', '3-курс'),
        ('3-1', '3-курс-академ'),
        ('4', '4-курс'),
        ('4-1', '4-курс-академ'),
    )
    course = models.CharField(choices=TYPE_STATUS, verbose_name='курс', default='1', max_length=3)
    student_status = models.ForeignKey(to='Students.StatusStudent', verbose_name='статус студента',
                                       on_delete=models.CASCADE, default=1)
    photo_student = models.FileField(upload_to='photo/%Y/%m.%d/', verbose_name='фото студента',
                                     default='default_img/default.png', )
    photo_social_reference = models.FileField(upload_to='social_reference/', verbose_name='Социальная справка',
                                              default='default_img/default.png', )
    start_social_reference = models.CharField(verbose_name='дата назначения справки', max_length=255, blank=True)
    end_social_reference = models.CharField(verbose_name='дата завершения действия справки', max_length=255,
                                            blank=True)

    ORGANIZATION = (
        ('К', 'КДМ'),
        ('П', 'ПРОФКОМ'),
        ('С', 'СНО'),
        ('Н', 'Нету'),
    )
    organization = models.CharField(choices=ORGANIZATION, verbose_name='организация', max_length=1, default='Н')
    organization_sector = models.ForeignKey(to='OrganizationSector', verbose_name='Сектор организации',
                                            on_delete=models.SET_NULL, null=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='дата изменения')

    class Meta:
        db_table = 'InfoStudent'

    def get_full_name(self):
        return f'{self.last_name} {self.name} {self.middle_name}'

    def get_fields(self):
        return [(field.verbose_name, field.value_from_object(self)) for field in self.__class__._meta.fields]

    def __str__(self):
        return f'{self.name} {self.last_name}'


class StatusStudent(models.Model):
    name = models.CharField(verbose_name='статус', max_length=255, )

    class Meta:
        db_table = 'StatusStudent'

    def __str__(self):
        return self.name


class TypeDirection(models.Model):
    name = models.CharField(verbose_name='Направление', max_length=255, )

    class Meta:
        db_table = 'TypeDirection'

    def __str__(self):
        return self.name


class OrganizationSector(models.Model):
    name = models.CharField(verbose_name='Сектор организации', max_length=255, )

    class Meta:
        db_table = 'OrganizationSector'

    def __str__(self):
        return self.name
