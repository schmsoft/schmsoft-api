from collections import namedtuple

from contact.templates import sms as templates_sms
from contact import models as contact_models

ContactDefinition = namedtuple(
    "ContactDefinition",
    ["definition_key", "template", "subject", "mechanism", "template_id"],
)


# Test
SMS_TEMPLATE_TEST = "test"


DEFINITIONS = {
    SMS_TEMPLATE_TEST: ContactDefinition(
        SMS_TEMPLATE_TEST,
        templates_sms.TEST,
        None,
        contact_models.ContactRecord.Mechanisms.SMS,
        None,
    )
}
