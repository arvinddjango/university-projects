# Generated by Django 2.2.3 on 2019-07-18 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universityapp', '0029_semesterlist_exam_sem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semesterlist',
            name='user_semester',
        ),
    ]