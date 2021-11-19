import graphene
from graphene.types.inputobjecttype import InputObjectType
from graphene_django import DjangoObjectType
from django.contrib.auth import models as auth_models

from infrastructure.decorators import login_required

from user.api import list as user_api_list


class UserType(DjangoObjectType):
    name = graphene.String()

    class Meta:
        model = auth_models.User
        exclude = ("password",)

    def resolve_name(self, info):
        return "{} {}".format(self.first_name, self.last_name).strip()


class UserInput(InputObjectType):
    first_names = graphene.String()
    last_name = graphene.String()
    email = graphene.String()


class UserQuery(graphene.ObjectType):
    me = graphene.Field(UserType)
    users = graphene.List(UserType)
    staff_users = graphene.List(UserType)

    def resolve_me(self, info):
        return info.context.user

    def resolve_users(self, info):
        return auth_models.User.objects.all()

    def resolve_staff_users(self, info):
        return list(user_api_list.list_staff_users())
