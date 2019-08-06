# Generated by Django 2.2.3 on 2019-07-12 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universityapp', '0006_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_title_one', models.CharField(max_length=20)),
                ('about_title_two', models.CharField(max_length=20)),
                ('about_desc', models.TextField(max_length=5000)),
                ('about_created', models.DateTimeField(auto_now_add=True)),
                ('about_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]