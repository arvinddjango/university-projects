# Generated by Django 2.2.3 on 2019-07-12 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universityapp', '0003_upcomingevent_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobVacant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_img', models.ImageField(upload_to='job_image/')),
                ('job_title', models.CharField(max_length=200)),
                ('slug', models.SlugField(default='', max_length=264)),
                ('job_desc', models.TextField(max_length=5000)),
                ('job_location', models.CharField(max_length=50)),
                ('job_from', models.DateField(blank=True)),
                ('job_time_from', models.TimeField(blank=True)),
                ('job_time_to', models.TimeField(blank=True)),
                ('job_create', models.DateTimeField(auto_now_add=True)),
                ('job_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
