# Generated by Django 3.2.13 on 2022-11-03 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='grade',
        ),
    ]
