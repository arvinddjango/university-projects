# Generated by Django 2.2.3 on 2019-07-20 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universityapp', '0040_auto_20190720_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcomingevent',
            name='event_img',
            field=models.ImageField(upload_to='event_image/'),
        ),
    ]
