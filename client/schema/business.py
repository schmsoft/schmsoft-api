from inspect import Arguments
from os import name
import graphene
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required

from client import models as client_models
from client.schema import owner as client_schema_owner
from client.api import owner as client_api_owner
from user.api import create as user_api_create


class BusinessType(DjangoObjectType):
    class Meta:
        model = client_models.Business


class CountryInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    code = graphene.String()


class StateInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    code = graphene.String()
    country = CountryInput()


class LocalityInput(graphene.InputObjectType):
    id = graphene.ID(required=False)
    name = graphene.String(required=False)
    postal_code = graphene.String(required=False)
    state = StateInput()


class AddressInput(graphene.InputObjectType):
    id = graphene.ID(required=False)
    street_number = graphene.String(required=False)
    route = graphene.String(required=False)
    locality = LocalityInput()


class BusinessInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    description = graphene.String(required=False)
    business_type = graphene.String(required=True)
    registration_number = graphene.String(required=False)
    status = graphene.String(required=False)
    current_location = AddressInput()
    years_in_current_location = graphene.Int(required=False)
    operating_capital = graphene.Decimal()
    operating_capital_currency = graphene.String()
    daily_sales = graphene.Decimal()
    daily_sales_currency = graphene.String()


class BusinessQuery(graphene.ObjectType):
    businesses = graphene.List(BusinessType)
    business = graphene.Field(BusinessType, id=graphene.ID(required=True))

    @login_required
    def resolve_businesses(self, info):
        return client_models.Business.objects.all()

    @login_required
    def resolve_business(self, info, id):
        return client_models.Business.objects.get(id=id)


class AddBusinessMutation(graphene.Mutation):
    class Arguments:
        business = BusinessInput()
        owner = client_schema_owner.OwnerInput()

    business = graphene.Field(BusinessType)

    def mutate(self, info, business, owner):
        business = client_models.Business.objects.create(**business)
        user = user_api_create.create_user_without_password(username=owner.phone_number)
        owner = client_api_owner.update_or_create_owner(
            owner_input=owner, business_id=business.id, user=user
        )

        return AddBusinessMutation(business=business)


class BusinessMutation(graphene.ObjectType):
    add_business = AddBusinessMutation.Field()
