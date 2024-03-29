# Generated by Django 3.2.7 on 2021-10-29 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_remove_owner_registration_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='business_type',
            field=models.CharField(blank=True, choices=[('Sole Proprietorship', 'Sole Proprietorship'), ('Partnership', 'Partnership'), ('Limited Liability Partnership', 'Limited Liability Partnership'), ('Limited Liability Company', 'Limited Liability Company'), ('Society', 'Society')], max_length=32),
        ),
        migrations.AlterField(
            model_name='business',
            name='status',
            field=models.CharField(blank=True, choices=[('Active', 'Active'), ('Suspended', 'Suspended')], default='Active', max_length=32),
        ),
        migrations.AlterField(
            model_name='loanportfolio',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Closed', 'Closed')], default='Active', max_length=16),
        ),
        migrations.AlterField(
            model_name='owner',
            name='gender',
            field=models.CharField(blank=True, choices=[('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other')], max_length=16),
        ),
        migrations.AlterField(
            model_name='owner',
            name='identification_method',
            field=models.CharField(choices=[('National ID', 'National Id'), ('Passoport', 'Passport'), ("Driver's License", 'Driver License')], default='National ID', max_length=32),
        ),
        migrations.AlterField(
            model_name='owner',
            name='identification_number',
            field=models.CharField(max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('Single', 'Single'), ('Married', 'Married'), ('Widowed', 'Widowed'), ('Divorced', 'Divorced')], max_length=16),
        ),
    ]
