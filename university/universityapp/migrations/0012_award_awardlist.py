# Generated by Django 2.2.3 on 2019-07-15 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('universityapp', '0011_admissionpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award_title', models.CharField(max_length=30)),
                ('award_desc', models.TextField()),
                ('award_img', models.ImageField(upload_to='award_img/')),
                ('award_date', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AwardList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award_list_title', models.CharField(max_length=55)),
                ('award_time_from', models.TimeField(blank=True)),
                ('award_time_to', models.TimeField(blank=True)),
                ('award_list_img', models.ImageField(upload_to='award_img/')),
                ('award_list_desc', models.TextField()),
                ('award_list_desc1', models.TextField()),
                ('award_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universityapp.Award')),
            ],
        ),
    ]
