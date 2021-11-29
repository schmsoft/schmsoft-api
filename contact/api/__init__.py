from django.core.exceptions import BadRequest
from phonenumber_field import phonenumber


from django.conf import settings
from integrations.monyera.api import sms as monyera_api_sms
from django.contrib.auth import models as auth_models
from client import models as client_models
from contact import definitions as contact_definitions, models as contact_models


def contact(user, definition_key):
    pass


def contact_via_sms(
    users: list[auth_models.User],
    text=None,
    definition_key: str = None,
):
    business_owner_phones = []
    for owner in client_models.Owner.objects.filter(user__in=users):
        business_owner_phones.append(owner.phone_number.as_e164)

    message = text

    if not message:
        message = contact_definitions.DEFINITIONS.get(definition_key).template

    if not message:
        raise ValueError("Text message cannot be empty.")

    response = monyera_api_sms.contact(business_owner_phones, text=text)

    contact_records = []
    for user in users:
        record = contact_models.ContactRecord.objects.create(
            sent_to=user,
            mechanism=contact_models.ContactRecord.Mechanisms.SMS,
            sent_to_phone_number=user.owner.phone_number,
            sent_from_sender_id=settings.SENDER_ID,
            definition_key=definition_key,
            text_content=message,
            succeeded=response["isSuccessful"],
        )
        contact_records.append(record)

    return contact_records
