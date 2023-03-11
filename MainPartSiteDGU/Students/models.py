from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

# def directory_path(instance, filename):
#     return f'photo/%Y/%m.%d/{filename}'
from django.urls import reverse


class CustomUser(AbstractUser):
    ROLES = (
        ('T', 'Преподаватель'),
        ('S', 'Студент'),
        ('B', 'Ласточка'),
    )
    roles = models.CharField(choices=ROLES, max_length=2, blank=True,
                             default='S')
    middle_name = models.CharField(max_length=255, verbose_name='Отчество', blank=True)

    class Meta:
        db_table = 'Dj_CUser'

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        full_name = '%s %s %s' % (self.first_name, self.last_name, self.middle_name)
        return full_name.strip()


class ProfileStudent(models.Model):
    student = models.OneToOneField(to='CustomUser', on_delete=models.CASCADE, verbose_name='Студент')
    direction = models.ForeignKey(to='TypeDirection', verbose_name='Направление', on_delete=models.CASCADE,
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
    student_status = models.ForeignKey(to='StatusStudent', verbose_name='статус студента',
                                       on_delete=models.SET_NULL, default=1, null=True)
    photo_student = models.FileField(upload_to='photo_student/%Y/%m.%d/', verbose_name='фото студента',
                                     default='default_img/default.png', )
    photo_social_reference = models.FileField(upload_to='social_reference/', verbose_name='Социальная справка',
                                              default='default_img/default.png', )
    start_social_reference = models.DateField(verbose_name='дата назначения справки', blank=True, null=True)
    end_social_reference = models.DateField(verbose_name='дата завершения действия справки', blank=True, null=True)

    ORGANIZATION = (
        ('К', 'КДМ'),
        ('П', 'ПРОФКОМ'),
        ('С', 'СНО'),
        ('О', 'Отсутствует'),
    )
    organization = models.CharField(choices=ORGANIZATION, verbose_name='организация', max_length=1, default='О')
    organization_sector = models.ForeignKey(to='OrganizationSector', verbose_name='Сектор организации',
                                            on_delete=models.SET_NULL, null=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания', )
    time_update = models.DateTimeField(auto_now=True, verbose_name='дата изменения', )

    class Meta:
        db_table = 'ProfileStudent'

    def get_absolute_url(self):
        return reverse('detail_student', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.student.get_full_name()}'


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


class Events(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название мероприятия')
    photo = models.FileField(upload_to='Events/%Y/%m.%d/', verbose_name='Фото мероприятия')
    text = models.TextField(verbose_name='текст')
    date = models.DateField(verbose_name='Дата мероприятия')
    time = models.TimeField(verbose_name='Время мероприятия')
    user = models.ForeignKey(to='CustomUser', verbose_name='Кто добавил', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'Events'

    def __str__(self):
        return self.name
