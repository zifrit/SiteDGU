# Generated by Django 4.0 on 2022-10-07 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0013_remove_customuser_roles_customuser_roles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='roles',
            field=models.CharField(blank=True, choices=[('T', 'Преподаватель'), ('S', 'Студент'), ('B', 'Ласточка')], default='S', max_length=2),
        ),
    ]
