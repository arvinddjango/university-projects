# Generated by Django 2.2.3 on 2019-07-18 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universityapp', '0037_jobvacant_job_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobvacant',
            name='job_position',
            field=models.CharField(default='', max_length=100),
        ),
    ]
