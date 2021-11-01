import graphene
from graphene_django import DjangoObjectType
from graphene_file_upload.scalars import Upload

from graphql_jwt.decorators import login_required

from client import models as client_models
from client.api import owner as client_api_owner


class OwnerType(DjangoObjectType):
    # gender = graphene.Field(graphene.String, source="gender")
    # marital_status = graphene.Field(graphene.String, source="marital_status")
    # total_monthly_income = graphene.Field(
    #     graphene.Decimal, source="total_monthly_income"
    # )

    class Meta:
        model = client_models.Owner


class OwnerInput(graphene.InputObjectType):
    role_definition = graphene.String()
    business_id = graphene.ID()
    identification_method = graphene.String(required=True)
    identification_number = graphene.String(required=True)
    phone_number = graphene.String(required=True)
    total_monthly_income = graphene.Decimal()
    number_of_dependants = graphene.Int()
    gender = graphene.String(required=True)
    marital_status = graphene.String()
    passport_photo = Upload()


class OwnerQuery(graphene.ObjectType):
    business_owners = graphene.List(OwnerType)

    def resolve_business_owners(self, info):
        return client_models.Owner.objects.all()


class AddOwnerMutation(graphene.Mutation):
    class Arguments:
        owner = OwnerInput()

    owner = graphene.Field(OwnerType)

    @login_required
    def mutate(self, info, owner):
        owner = client_api_owner.update_or_create_owner(owner)

        return AddOwnerMutation(owner=owner)


class UploadOwnerPhotoMutation(graphene.Mutation):
    class Arguments:
        owner_id = graphene.ID(required=True)
        passport_photo = Upload(required=True)

    passport_photo_link = graphene.String()

    @login_required
    def mutate(self, info, owner_id, passport_photo):
        owner = client_models.Owner.objects.get(id=owner_id)
        client_api_owner.update_owner_passport_photo(
            owner=owner, passport_photo=passport_photo
        )

        return UploadOwnerPhotoMutation(passport_photo_link=owner.passport_photo.url)


class OwnerMutation(graphene.ObjectType):
    add_owner = AddOwnerMutation.Field()
    upload_owner_photo = UploadOwnerPhotoMutation.Field()
