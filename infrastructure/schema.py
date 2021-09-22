import graphene

from graphene_django import DjangoObjectType
from django.contrib.auth import models as auth_models


class UserType(DjangoObjectType):
    class Meta:
        model = auth_models.User


class UserQuery(graphene.ObjectType):
    me = graphene.Field(UserType)

    def resolve_me(self, info):
        return info.context.user
