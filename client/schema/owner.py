import graphene
from graphene_django import DjangoObjectType

from client import models as client_models


class OwnerType(DjangoObjectType):
    class Meta:
        model = client_models.Owner


class OwnerQuery(graphene.ObjectType):
    business_owners = graphene.List(OwnerType)

    def resolve_business_owners(self, info):
        return client_models.Owner.objects.alL()
