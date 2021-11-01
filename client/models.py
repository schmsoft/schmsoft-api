from enum import unique
from django.db import models
from django.db.models.enums import TextChoices

from infrastructure import model_utils
from model_utils.models import TimeStampedModel, SoftDeletableModel
from address.models import Address
from djmoney.models.fields import MoneyField
from phonenumber_field.modelfields import PhoneNumberField


class Business(TimeStampedModel, SoftDeletableModel, model_utils.SchmsoftModel):
    class BusinessType(models.TextChoices):
        SOLE_PROPRIETORSHIP = (
            "SOLE_PROPRIETORSHIP",
            "Sole Proprietorship",
        )
        PARTNERSHIP = (
            "PARTNERSHIP",
            "Partnership",
        )
        LIMITED_LIABILITY_PARTNERSHIP = (
            "LIMITED_LIABILITY_PARTNERSHIP",
            "Limited Liability Partnership",
        )
        LIMITED_LIABILITY_COMPANY = (
            "LIMITED_LIABILITY_COMPANY",
            "Limited Liability Company",
        )
        SOCIETY = (
            "SOCIETY",
            "Society",
        )

    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        SUSPENDED = "SUSPENDED", "Suspended"

    class Category(models.TextChoices):
        ACCOUNTING = (
            "ACCOUNTING",
            "Accounting",
        )
        AGENTS = ("AGENTS", "Agents")
        AGRICULTURE = (
            "AGRICULTURE",
            "Agriculture",
        )
        ANTIQUES_AND_COLLECTABLES = (
            "ANTIQUES_AND_COLLECTABLES",
            "Antiques and Collectables",
        )
        ARTS_AND_CRAFTS = (
            "ARTS_AND_CRAFTS",
            "Arts and Crafts",
        )
        ASSET_MANAGEMENT = (
            "ASSET_MANAGEMENT",
            "Assets Management",
        )
        AUTOMOTIVE = (
            "AUTOMOTIVE",
            "Automotive",
        )
        BEVERAGES = (
            "BEVERAGES",
            "Beverages",
        )
        BROKERS = (
            "BROKERS",
            "Brokers",
        )
        BUSINESS_SERVICES = (
            "BUSINESS_SERVICES",
            "Business Services",
        )
        CHILD_CARE = (
            "CHILD_CARE",
            "Child Care",
        )
        CLEANING_SERVICES = (
            "CLEANING_SERVICES",
            "Cleaning Services",
        )
        DESIGN = (
            "DESIGN",
            "Design",
        )
        DISTRIBUTOR = (
            "DISTRIBUTOR",
            "Distributor",
        )
        ECOMMERCE = (
            "ECOMMERCE",
            "Ecommerce",
        )
        EDUCATION_AND_TRAINING = (
            "EDUCATION_AND_TRAINING",
            "Education and Training",
        )
        ENTERTAINMENT = (
            "ENTERTAINMENT",
            "Entertainment",
        )
        FASHION = (
            "FASHION",
            "Fashion",
        )
        FOOD_SERVICES = (
            "FOOD_SERVICES",
            "Food Sevices",
        )
        GARDENING_AND_LANDSCAPING = (
            "GARDENING_AND_LANDSCAPING",
            "Gardening and Landscaping",
        )
        HEALTH_AND_BEAUTY = (
            "HEALTH_AND_BEAUTY",
            "Health and Beauty",
        )
        INFORMATION_TECHNOLOGY = (
            "INFORMATION_TECHNOLOGY",
            "Information Technology",
        )
        LEGAL_SERVICES = (
            "LEGAL_SERVICES",
            "Legal Services",
        )
        MAINTENANCE_AND_REPAIR = (
            "MAINTENANCE_AND_REPAIR",
            "Maintenance and Repair",
        )
        MANAGEMENT_SERVICES = (
            "MANAGEMENT_SERVICES",
            "Management Services",
        )
        MANUFACTURING = (
            "MANUFACTURING",
            "Manufacturing",
        )
        MARKETING_SERVICES = (
            "MARKETING_SERVICES",
            "Marketing Services",
        )
        MEDIA = (
            "MEDIA",
            "Media",
        )
        MEDICAL_PRACTITIONERS = (
            "MEDICAL_PRACTITIONERS",
            "Medical Practitioners",
        )
        MUSIC = (
            "MUSIC",
            "Music",
        )
        NIGHTLIFE = (
            "NIGHTLIFE",
            "Nightlife",
        )
        PERSONAL_SERVICES = (
            "PERSONAL_SERVICES",
            "Personal Services",
        )
        PET_SERVICES = (
            "PET_SERVICES",
            "Pet Services",
        )
        PHOTOGRAPHY = (
            "PHOTOGRAPHY",
            "Photography",
        )
        PROFESSIONAL_SERVICES = (
            "PROFESSIONAL_SERVICES",
            "Professional Services",
        )
        PUBLISHING = (
            "PUBLISHING",
            "Publishing",
        )
        RECRUITING_AND_STAFFING = (
            "RECRUITING_AND_STAFFING",
            "Recruiting and Staffing",
        )
        RENTAL_AND_LEASING = (
            "RENTAL_AND_LEASING",
            "Rental and Leasing",
        )
        RESEARCH_SERVICES = (
            "RESEARCH_SERVICES",
            "Research Services",
        )
        RETAIL = (
            "RETAIL",
            "Retail",
        )
        SHIPPING_AND_DELIVERY = (
            "SHIPPING_AND_DELIVERY",
            "Shipping and Delivery",
        )
        SPORTS_AND_RECREATION = (
            "SPORTS_AND_RECREATION",
            "Sports and Recreation",
        )
        TOYS_AND_HOBBIES = (
            "TOYS_AND_HOBBIES",
            "Toys and Hobbies",
        )
        TRANSPORTATION = (
            "TRANSPORTATION",
            "Transportation",
        )
        TRAVEL_AND_TOURISM = (
            "TRAVEL_AND_TOURISM",
            "Travel and Tourism",
        )
        VALUE_ADDED_RESELLER = (
            "VALUE_ADDED_RESELLER",
            "Value Added Reseller",
        )
        WAREHOUSING_AND_STORAGE = (
            "WAREHOUSING_AND_STORAGE",
            "Warehousing and Storage",
        )
        WHOLESALE = (
            "WHOLESALE",
            "Wholesale",
        )

    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    business_type = models.CharField(
        max_length=64, blank=True, choices=BusinessType.choices
    )
    category = models.CharField(max_length=255, blank=True, choices=Category.choices)
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
        NATIONAL_ID = "NATIONAL_ID", "National ID"
        PASSPORT = "PASSPORT", "Passport"
        DRIVER_LICENSE = "DRIVER_LICENSE", "Driver's License"

    class Gender(models.TextChoices):
        FEMALE = "FEMALE", "Female"
        MALE = "MALE", "Male"
        OTHER = "OTHER", "Other"

    class MaritalStatus(models.TextChoices):
        SINGLE = "SINGLE", "Single"
        MARRIED = "MARRIED", "Married"
        WIDOWED = "WIDOWED", "Widowed"
        DIVORCED = "DIVORCED", "Divorced"

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
        ACTIVE = "ACTIVE", "Active"
        CLOSED = "CLOSED", "Closed"

    name = models.CharField(max_length=32, unique=True, blank=False, null=False)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=16, choices=Status.choices, default=Status.ACTIVE
    )
    owners = models.ManyToManyField("auth.User", blank=True)
