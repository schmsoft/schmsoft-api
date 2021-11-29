from django.db import models
from model_utils.models import TimeStampedModel
from phonenumber_field.modelfields import PhoneNumberField


class ContactRecord(TimeStampedModel, models.Model):
    class Mechanisms(models.TextChoices):
        SMS = "SMS", "Text Message (SMS)"
        EMAIL = "EMAIL", "Email"
        SLACK = "SLACK", "Slack"

    sent_by = models.ForeignKey(
        "auth.User",
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name="contacts_sent",
    )
    sent_to = models.ForeignKey(
        "auth.User", on_delete=models.PROTECT, related_name="contacts_received"
    )
    mechanism = models.CharField(
        max_length=32, choices=Mechanisms.choices, db_index=True
    )
    sent_from_email_address = models.EmailField(max_length=200, blank=True)
    sent_to_email_address = models.EmailField(max_length=200, blank=True)
    sent_to_phone_number = PhoneNumberField(
        blank=True,
    )
    sent_from_sender_id = models.CharField(max_length=11, blank=True)
    sent_to_slack_username_or_channel = models.CharField(max_length=64, blank=True)
    definition_key = models.CharField(max_length=64, db_index=True)
    subject = models.CharField(max_length=256, blank=True)
    text_content = models.TextField()
    succeeded = models.BooleanField(blank=True, default=True)
