# Generated by Django 3.2.7 on 2021-10-30 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0006_alter_owner_identification_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='identification_method',
            field=models.CharField(choices=[('NATIONAL_ID', 'National ID'), ('PASSPORT', 'Passport'), ('DRIVER_LICENSE', "Driver's License")], default='NATIONAL_ID', max_length=32),
        ),
    ]
