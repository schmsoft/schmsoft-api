# Generated by Django 3.2.7 on 2021-10-30 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0008_business_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='business_type',
            new_name='type',
        ),
    ]