import graphene
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required


from contact import models as contact_models


class ContactRecordType(DjangoObjectType):
    class Meta:
        model = contact_models.ContactRecord


class ContactRecordQuery(graphene.ObjectType):
    contact_records = graphene.List(ContactRecordType)

    @login_required
    def resolve_contact_records(self, info):
        return list(contact_models.ContactRecord.objects.all())
