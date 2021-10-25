from enum import unique
from django.db import models
from django.db.models.enums import TextChoices

from infrastructure import model_utils
from model_utils.models import TimeStampedModel, SoftDeletableModel
from address.models import Address
from djmoney.models.fields import MoneyField
from phonenumber_field.modelfields import PhoneNumberField


class Business(TimeStampedModel, SoftDeletableModel, model_utils.SchmsoftModel):
    class Types(models.TextChoices):
        SOLE_PROPRIETORSHIP = "Sole Proprietorship"
        PARTNERSHIP = "Partnership"
        LIMITED_LIABILITY_PARTNERSHIP = "Limited Liability Partnership"
        LIMITED_LIABILITY_COMPANY = "Limited Liability Company"
        SOCIETY = "Society"

    class Status(models.TextChoices):
        ACTIVE = "Active"
        SUSPENDED = "Suspended"

    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    business_type = models.CharField(max_length=32, blank=True, choices=Types.choices)
    registration_number = models.CharField(max_length=64, blank=True, null=True)
    status = models.CharField(
        max_length=32, blank=True, choices=Status.choices, default=Status.ACTIVE
    )
    current_location = Address()
    years_in_current_location = models.IntegerField(blank=True)
    operating_capital = MoneyField(
        max_digits=19, decimal_places=4, null=True, default_currency="KES"
    )
    daily_sales = MoneyField(
        max_digits=19, decimal_places=4, null=True, default_currency="KES"
    )
    suspension_reason = models.TextField(blank=True, null=True)


class Owner(TimeStampedModel, SoftDeletableModel, model_utils.SchmsoftModel):
    class IdentificationMethods(models.TextChoices):
        NATIONAL_ID = "National ID"
        PASSPORT = "Passoport"
        DRIVER_LICENSE = "Driver's License"

    class Gender(models.TextChoices):
        FEMALE = "Female"
        MALE = "Male"
        OTHER = "Other"

    class MaritalStatus(models.TextChoices):
        SINGLE = "Single"
        MARRIED = "Married"
        WIDOWED = "Widowed"
        DIVORCED = "Divorced"

    role_definition = models.CharField(max_length=64, blank=True)
    user = models.OneToOneField("auth.User", on_delete=models.PROTECT)
    business = models.ForeignKey(Business, on_delete=models.PROTECT)
    identification_method = models.CharField(
        max_length=32,
        choices=IdentificationMethods.choices,
        default=IdentificationMethods.NATIONAL_ID,
    )
    identification_number = models.CharField(max_length=32, unique=True, blank=False)
    phone_number = PhoneNumberField(blank=False, unique=True)
    total_monthly_income = MoneyField(
        max_digits=19, decimal_places=4, null=True, default_currency="KES", default=0
    )
    number_of_dependants = models.IntegerField(default=0)
    gender = models.CharField(max_length=16, blank=True, choices=Gender.choices)
    marital_status = models.CharField(
        max_length=16, blank=True, choices=MaritalStatus.choices
    )
    passport_photo = models.FileField(blank=True)


class LoanPortfolio(TimeStampedModel, SoftDeletableModel, model_utils.SchmsoftModel):
    class Status(TextChoices):
        ACTIVE = "Active"
        CLOSED = "Closed"

    name = models.CharField(max_length=32, unique=True, blank=False, null=False)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=16, choices=Status.choices, default=Status.ACTIVE
    )
    owners = models.ManyToManyField("auth.User", blank=True)
