# Generated by Django 3.2.7 on 2021-10-17 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_auto_20211016_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='registration_fee',
        ),
    ]