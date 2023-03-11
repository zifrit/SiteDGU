# Generated by Django 4.0 on 2023-03-07 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0008_infostudent_full_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='date',
            field=models.DateField(verbose_name='Дата мероприятия'),
        ),
        migrations.AlterField(
            model_name='events',
            name='text',
            field=models.TextField(verbose_name='текст'),
        ),
        migrations.AlterField(
            model_name='events',
            name='time',
            field=models.TimeField(verbose_name='Время мероприятия'),
        ),
        migrations.AlterField(
            model_name='infostudent',
            name='start_social_reference',
            field=models.DateField(blank=True, null=True, verbose_name='дата на значения справки'),
        ),
    ]
