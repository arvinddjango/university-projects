# Generated by Django 2.2.3 on 2019-07-18 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universityapp', '0031_auto_20190718_1220'),
    ]

    operations = [
        migrations.RenameField(
            model_name='semesterlist',
            old_name='user_semester',
            new_name='exam_sem',
        ),
    ]
