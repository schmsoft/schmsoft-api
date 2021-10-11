import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth import models as auth_models

from infrastructure.decorators import login_required


class UserType(DjangoObjectType):
    class Meta:
        model = auth_models.User
        fields = ("id", "first_name", "last_name", "username", "email")


class UserQuery(graphene.ObjectType):
    me = graphene.Field(UserType)
    users = graphene.List(UserType)

    @login_required
    def resolve_me(self, info):
        return info.context.user

    @login_required
    def resolve_users(self, info):
        return auth_models.User.objects.all()
