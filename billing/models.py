from django.db import models
from django.db import models
from djmoney.models.fields import MoneyField
from infrastructure import model_utils
from model_utils.models import TimeStampedModel, SoftDeletableModel


class Payment(TimeStampedModel, SoftDeletableModel, model_utils.SchmsoftModel):
    class PaymentMethods(models.TextChoices):
        CASH = "CASH"
        CHECK = "CHECK"
        CREDIT_CARD = "CREDIT_CARD"
        MOBILE_MONEY = "MOBILE_MONEY"
        CRYPTOCURRENCY = "CRYPTOCURRENCY"
        BARTERING = "BARTERING"
        MONEY_ORDER = "MONEY_ORDER"
        ACH_OR_WIRE_TRANSFER = "ACH_OR_WIRE_TRANSFER"

    class MobileMoneyChannel(models.TextChoices):
        MPESA = "MPESA"
        AIRTEL_MONEY = "AIRTEL_MONEY"
        T_KASH = "T_KASH"

    class TransactionStatus(models.TextChoices):
        PENDING = "PENDING"
        COMPLETE = "COMPLETE"
        REVERSED = "REVERSED"
        TRANSFERRED = "TRANSFERRED"

    class TransactionType(models.TextChoices):
        INCOMING = "INCOMING"
        OUTGOING = "OUTGOING"

    class MobileMoneyChannelType(models.TextChoices):
        BUY_GOODS_TILL = "BUY_GOODS_TILL"
        PAYBILL = "PAYBILL"

    class CollectionPartner(models.TextChoices):
        KOPO_KOPO = "KOPO_KOPO"

    transaction_type = models.CharField(
        max_length=16, choices=models.TextChoices, default=TransactionType.INCOMING
    )
    payment_method = models.CharField(
        max_length=32,
        choices=PaymentMethods.choices,
        default=PaymentMethods.CASH,
    )
    mobile_money_channel = models.CharField(
        max_length=32, blank=True, choices=MobileMoneyChannel.choices
    )
    mobile_money_channel_type = models.CharField(
        max_length=32, blank=True, choices=MobileMoneyChannelType.choices
    )
    transacton_reference = models.CharField(max_length=64, blank=True)

    transaction_status = models.CharField(
        max_length=16,
        choices=TransactionStatus.choices,
        default=TransactionStatus.COMPLETE,
    )

    amount = MoneyField(
        max_digits=19, decimal_places=4, null=True, default_currency="KES"
    )

    # collection partner
    collected_through = models.CharField(
        max_length=64, blank=True, choices=CollectionPartner.choices
    )
    account_number = models.CharField(max_length=64, blank=True)
    partner_transaction_reference = models.CharField(max_length=64, blank=True)

    # sender / receiver details
    phone_number = models.CharField(max_length=20, blank=True)
    first_name = models.CharField(max_length=32, blank=True)
    middle_name = models.CharField(max_length=32, blank=True)
    last_name = models.CharField(max_length=32, blank=True)
