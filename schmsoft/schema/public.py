import graphene

from user.schema import auth as user_schema_auth


class Query(graphene.ObjectType):
    test = graphene.String()

    def resolve_test(self, info):
        return "Just a Test"


class Mutation(user_schema_auth.AuthMutation, graphene.ObjectType):
    ...


PUBLIC_SCHEMA = graphene.Schema(query=Query, mutation=Mutation)
