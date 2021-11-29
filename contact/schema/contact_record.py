import graphene
from graphene_django import DjangoObjectType
from phonenumber_field.phonenumber import PhoneNumber

from django.contrib.auth import models as auth_models
from django.core.exceptions import BadRequest

from contact import models as contact_models
from integrations.monyera.api import sms as monyera_api_sms
from contact import api as contact_api


class ContactRecordType(DjangoObjectType):
    class Meta:
        model = contact_models.ContactRecord


class ContactRecordQuery(graphene.ObjectType):
    contact_records = graphene.List(
        ContactRecordType, user_id=graphene.ID(required=True)
    )

    def resolve_contact_records(self, info, user_id):
        qs = auth_models.User.objects.filter(id=user_id)

        if not qs.exists():
            raise BadRequest("Invalid user id: {}".format(user_id))

        return contact_models.ContactRecord.objects.filter(sent_to_id=user_id)


class SmsToNumbersMutation(graphene.Mutation):
    class Arguments:
        phone_numbers = graphene.List(graphene.String)
        text = graphene.String()

    success = graphene.Boolean()

    def mutate(self, info, phone_numbers, text):
        to = []
        for number in phone_numbers:
            standard_phone_number = PhoneNumber.from_string(number)
            if not standard_phone_number.is_valid():
                raise ValueError("Invalid phone number: {}.".format(number))

            to.append(standard_phone_number.as_e164)

        response = monyera_api_sms.contact(to, text)

        return SmsToNumbersMutation(success=response["isSuccessful"])


class SmsToUsersMutation(graphene.Mutation):
    class Arguments:
        user_ids = graphene.List(graphene.ID)
        text = graphene.String()

    contact_records = graphene.List(ContactRecordType)

    def mutate(self, info, user_ids, text):
        qs = auth_models.User.objects.filter(id__in=user_ids)
        if not qs.exists():
            raise BadRequest("Invalid user ids: {}.".format(user_ids))

        if not text.strip():
            raise ValueError("Text message cannot be empty.")

        contact_records = contact_api.contact_via_sms(qs.all(), text)

        return SmsToUsersMutation(contact_records=contact_records)


class ContactMutation(graphene.ObjectType):
    send_sms_to_numbers = SmsToNumbersMutation.Field()
    send_sms_to_users = SmsToUsersMutation.Field()
