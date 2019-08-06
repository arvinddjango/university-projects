# Generated by Django 2.2.3 on 2019-07-12 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universityapp', '0004_jobvacant'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_gallery', models.ImageField(upload_to='Image_Gallery/')),
                ('img_caption', models.CharField(max_length=50)),
                ('img_created', models.DateTimeField(auto_now_add=True)),
                ('img_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='jobvacant',
            name='job_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='upcomingevent',
            name='event_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]