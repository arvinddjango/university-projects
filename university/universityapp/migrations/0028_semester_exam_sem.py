# Generated by Django 2.2.3 on 2019-07-18 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universityapp', '0027_semesterlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester',
            name='exam_sem',
            field=models.CharField(default='', max_length=30),
        ),
    ]
