# Generated by Django 4.0 on 2022-09-30 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0002_alter_infostudent_direction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='infostudent',
            old_name='first_name',
            new_name='name',
        ),
    ]