# Generated by Django 4.0 on 2022-10-07 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0011_infostudent_end_social_reference_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalRoles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Роли')),
            ],
            options={
                'db_table': 'PersonalRoles',
            },
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='roles',
        ),
        migrations.AddField(
            model_name='customuser',
            name='roles',
            field=models.ManyToManyField(to='Students.PersonalRoles', verbose_name='тип пользователя'),
        ),
    ]
