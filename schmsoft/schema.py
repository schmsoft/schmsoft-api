import graphene

from infrastructure.schema import (
    auth as infrastructure_schema_auth,
    user as infrastructure_schema_user,
)
from client.schema import (
    business as client_schema_business,
    owner as client_schema_owner,
    loan_portfolio as client_loan_portfolio,
)


class Query(
    infrastructure_schema_user.UserQuery,
    client_schema_business.BusinessQuery,
    client_schema_owner.OwnerQuery,
    client_loan_portfolio.LoanPortfolioQuery,
):
    ...


class Mutation(
    infrastructure_schema_auth.AuthMutation,
    client_loan_portfolio.LoanPortfolioMutation,
    client_schema_business.BusinessMutation,
):
    ...


SCHEMA = graphene.Schema(query=Query, mutation=Mutation)
