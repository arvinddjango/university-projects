# Generated by Django 2.2.3 on 2019-07-26 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('universityapp', '0054_auto_20190726_1422'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('popular_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pcomments', to='universityapp.PopularCourses')),
            ],
        ),
        migrations.DeleteModel(
            name='CourseComment',
        ),
    ]
