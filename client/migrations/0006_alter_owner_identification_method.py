# Generated by Django 3.2.7 on 2021-10-30 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0005_auto_20211030_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='identification_method',
            field=models.CharField(choices=[('NATIONAL_ID', 'National Id'), ('PASSPORT', 'Passport'), ('DRIVER_LICENSE', 'Driver License')], default='NATIONAL_ID', max_length=32),
        ),
    ]
