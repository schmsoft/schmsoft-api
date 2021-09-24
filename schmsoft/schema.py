import graphene

from infrastructure.schema import (
    auth as infrastructure_schema_auth,
    user as infrastructure_schema_user,
)
from client.schema import (
    business as client_schema_business,
    owner as client_schema_owner,
)


class Query(
    infrastructure_schema_user.UserQuery,
    client_schema_business.BusinessQuery,
    client_schema_owner.OwnerQuery,
    graphene.ObjectType,
):
    pass


class Mutation(infrastructure_schema_auth.AuthMutation, graphene.ObjectType):
    pass


SCHEMA = graphene.Schema(query=Query, mutation=Mutation)
