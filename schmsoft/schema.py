import graphene
from infrastructure import schema as infrastructure_schema


class Query(infrastructure_schema.UserQuery):
    pass


class Mutation():
    pass


SCHEMA = graphene.Schema(query=Query)
