from phonenumber_field import phonenumber


from django.conf import settings
from integrations.monyera.api import sms as monyera_api_sms
from django.contrib.auth import models as auth_models
from client import models as client_models
from contact import definitions as contact_definitions, models as contact_models


def contact(user, definition_key):
    pass


def contact_via_sms(user: auth_models.User, definition_key: str):
    business_owner = client_models.Owner.objects.get(user=user)
    message = contact_definitions.DEFINITIONS.get(definition_key).template.format()

    response = monyera_api_sms.contact(
        business_owner.phone_number.as_e164, text=message
    )

    return contact_models.ContactRecord.objects.create(
        sent_to=user,
        mechanism=contact_models.ContactRecord.Mechanisms.SMS,
        sent_to_phone_number=business_owner.phone_number,
        sent_from_sender_id=settings.SENDER_ID,
        definition_key=definition_key,
        text_content=message,
        succeeded=response["isSuccessful"],
    )
