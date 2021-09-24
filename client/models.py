from enum import unique
from django.db import models
from django.utils import tree

from infrastructure import model_utils
from model_utils.models import TimeStampedModel, SoftDeletableModel
from address.models import Address
from djmoney.models.fields import MoneyField
from phonenumber_field.modelfields import PhoneNumberField


class Business(TimeStampedModel, SoftDeletableModel, model_utils.SchmsoftModel):
    class Types(models.TextChoices):
        SOLE_PROPRIETORSHIP = "SOLE_PROPRIETORSHIP"
        PARTNERSHIP = "PARTNERSHIP"
        LIMITED_LIABILITY_PARTNERSHIP = "LIMITED_LIABILITY_PARTNERSHIP"
        LIMITED_LIABILITY_COMPANY = "LIMITED_LIABILITY_COMPANY"
        SOCIETY = "SOCIETY"

    class Status(models.TextChoices):
        ACTIVE = "ACTIVE"
        SUSPENDED = "SUSPENDED"

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
        NATIONAL_ID = "NATIONAL_ID"
        PASSPORT = "PASSPORT"
        DRIVER_LICENSE = "DRIVER_LICENSE"

    class Gender(models.TextChoices):
        FEMALE = "FEMALE"
        MALE = "MALE"
        OTHER = "OTHER"

    class MaritalStatus(models.TextChoices):
        SINGLE = "SINGLE"
        MARRIED = "MARRIED"
        WIDOWED = "WIDOWED"
        DIVORCED = "DIVORCED"

    role_definition = models.CharField(max_length=64, blank=True)
    user = models.OneToOneField("auth.User", on_delete=models.PROTECT)
    business = models.ForeignKey(Business, on_delete=models.PROTECT)
    identification_method = models.CharField(
        max_length=32,
        choices=IdentificationMethods.choices,
        default=IdentificationMethods.NATIONAL_ID,
    )
    identification_number = models.CharField(max_length=32)
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
    registration_fee = models.OneToOneField("billing.Payment", on_delete=models.PROTECT)
