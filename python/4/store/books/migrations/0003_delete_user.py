# Generated by Django 3.2 on 2021-05-11 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
