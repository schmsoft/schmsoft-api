import graphene
from graphene_django import DjangoObjectType

from client import models as client_models


class BusinessType(DjangoObjectType):
    class Meta:
        model = client_models.Business


class BusinessQuery(graphene.ObjectType):
    businesses = graphene.List(BusinessType)
