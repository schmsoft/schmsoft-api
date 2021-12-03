from enum import Enum, unique
import k2connect

from django.conf import settings
from django.urls import reverse
from integrations.kopokopo import api as kopokopo_api
from infrastructure import url_utils

k2connect.initialize(
    settings.KOPOKOPO_CLIENT_ID,
    settings.KOPOKOPO_CLIENT_SECRET,
    settings.KOPOKOPO_BASE_URL,
)


@unique
class KopoKopoWebhookEvents(Enum):
    BUYGOODS_TRANSACTION_RECEIVED = "buygoods_transaction_received"
    BUYGOODS_TRANSACTION_REVERSED = "buygoods_transaction_reversed"
    B2B_TRANSACTION_RECEIVED = "b2b_transaction_received"
    M2M_TRANSACTION_RECEIVED = "m2m_transaction_received"
    SETTLEMENT_TRANSACTION_COMPLETED = "settlement_transfer_completed"
    CUSTOMER_CREATED = "customer_created"


@unique
class KopoKopoWebhookSubscriptionScopes(Enum):
    COMPANY = "company"
    TILL = "till"


def _access_token():
    token_service = k2connect.TokenService
    access_token_request = token_service.request_access_token()
    access_token = token_service.get_access_token(access_token_request)
    return access_token


def subscribe(
    event_type: str[KopoKopoWebhookEvents],
):
    if event_type not in list(KopoKopoWebhookEvents):
        raise ValueError("Invalid event type")
    k2_webhook_url = url_utils.absolute_url(
        reverse("integrations:kopokopo-webhook-callback")
    )

    payload = dict(
        access_token=_access_token(),
        event_type=event_type,
        webhook_endpoint=k2_webhook_url,
        scope=KopoKopoWebhookSubscriptionScopes.COMPANY,
    )

    webhook_service = k2connect.WebhookService
    subscription_location = webhook_service.create_subscription(**payload)

    # persist to database
    