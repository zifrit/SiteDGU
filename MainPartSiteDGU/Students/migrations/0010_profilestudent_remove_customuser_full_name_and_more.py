# Generated by Django 4.0 on 2023-03-07 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0009_alter_events_date_alter_events_text_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(choices=[('1', '1-курс'), ('1-1', '1-курс-академ'), ('1-2', '1-курс-магистратура'), ('2', '2-курс'), ('2-1', '2-курс-академ'), ('2-2', '2-курс-магистратура'), ('3', '3-курс'), ('3-1', '3-курс-академ'), ('4', '4-курс'), ('4-1', '4-курс-академ')], default='1', max_length=3, verbose_name='курс')),
                ('photo_student', models.FileField(default='default_img/default.png', upload_to='photo/%Y/%m.%d/', verbose_name='фото студента')),
                ('photo_social_reference', models.FileField(default='default_img/default.png', upload_to='social_reference/', verbose_name='Социальная справка')),
                ('start_social_reference', models.DateField(blank=True, null=True, verbose_name='дата назначения справки')),
                ('end_social_reference', models.DateField(blank=True, null=True, verbose_name='дата завершения действия справки')),
                ('organization', models.CharField(choices=[('К', 'КДМ'), ('П', 'ПРОФКОМ'), ('С', 'СНО'), ('О', 'Отсутствует')], default='О', max_length=1, verbose_name='организация')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='дата изменения')),
                ('direction', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Students.typedirection', verbose_name='Направление')),
                ('organization_sector', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Students.organizationsector', verbose_name='Сектор организации')),
            ],
            options={
                'db_table': 'ProfileStudent',
            },
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='full_name',
        ),
        migrations.AddField(
            model_name='customuser',
            name='middle_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Отчество'),
        ),
        migrations.DeleteModel(
            name='InfoStudent',
        ),
        migrations.AddField(
            model_name='profilestudent',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Students.customuser', verbose_name='Студент'),
        ),
        migrations.AddField(
            model_name='profilestudent',
            name='student_status',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Students.statusstudent', verbose_name='статус студента'),
        ),
    ]
