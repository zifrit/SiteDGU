# Generated by Django 4.0 on 2022-10-13 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0002_rename_deta_events_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PersonalRoles',
        ),
    ]
