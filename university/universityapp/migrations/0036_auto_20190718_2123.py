# Generated by Django 2.2.3 on 2019-07-18 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universityapp', '0035_delete_semesterlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobvacant',
            name='job_opening',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='popularcourses',
            name='course_duration',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='popularcourses',
            name='course_seat_total',
            field=models.CharField(default='', max_length=10),
        ),
    ]
