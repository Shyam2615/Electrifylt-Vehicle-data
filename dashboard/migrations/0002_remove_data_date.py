# Generated by Django 5.0.1 on 2024-04-09 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='Date',
        ),
    ]
