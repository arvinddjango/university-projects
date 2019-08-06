# Generated by Django 2.2.3 on 2019-07-26 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('universityapp', '0051_auto_20190726_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('pcomment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pcomments', to='universityapp.PopularCourses')),
            ],
        ),
    ]