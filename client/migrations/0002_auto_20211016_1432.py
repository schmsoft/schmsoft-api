# Generated by Django 3.2.7 on 2021-10-16 11:32

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default=0, max_length=128, region=None, unique=True),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='LoanPortfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=32, unique=True)),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('CLOSED', 'Closed')], default='ACTIVE', max_length=16)),
                ('owners', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
