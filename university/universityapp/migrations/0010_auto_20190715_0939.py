# Generated by Django 2.2.3 on 2019-07-15 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universityapp', '0009_admission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='email_id',
            field=models.EmailField(max_length=254),
        ),
    ]
