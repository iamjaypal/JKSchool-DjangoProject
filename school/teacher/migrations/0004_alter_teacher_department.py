# Generated by Django 5.2 on 2025-05-01 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_rename_department_teacher_department_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='department',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
