# Generated by Django 2.2.3 on 2019-07-18 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('universityapp', '0033_remove_semesterlist_exam_sem'),
    ]

    operations = [
        migrations.AddField(
            model_name='semesterlist',
            name='exam_sem',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='universityapp.ExamSem'),
        ),
    ]