import graphene

from user.schema import user as user_schema_user
from client.schema import (
    business as client_schema_business,
    owner as client_schema_owner,
    loan_portfolio as client_loan_portfolio,
)
from contact.schema import contact_record as contact_schema_contact_record


class Query(
    user_schema_user.UserQuery,
    client_schema_business.BusinessQuery,
    client_schema_owner.OwnerQuery,
    client_loan_portfolio.LoanPortfolioQuery,
    contact_schema_contact_record.ContactRecordQuery,
):
    ...


class Mutation(
    client_loan_portfolio.LoanPortfolioMutation,
    client_schema_business.BusinessMutation,
):
    ...


SCHEMA = graphene.Schema(query=Query, mutation=Mutation)
