# Generated by Django 5.2 on 2025-05-01 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_teacher'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
