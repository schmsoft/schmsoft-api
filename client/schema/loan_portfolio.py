import graphene
from graphene_django import DjangoObjectType

from graphql_jwt.decorators import login_required

from client import models as client_models

from .owner import OwnerType


class LoanPortfolioType(DjangoObjectType):
    class Meta:
        model = client_models.LoanPortfolio


class LoanPortfolioInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    description = graphene.String(required=False)


class LoanPortfolioQuery(graphene.ObjectType):
    loan_portfolios = graphene.List(
        LoanPortfolioType, status=graphene.String(required=False)
    )
    loan_portfolio = graphene.Field(LoanPortfolioType, id=graphene.ID(required=True))

    @login_required
    def resolve_loan_portfolios(self, info, status=None):
        if status:
            return client_models.LoanPortfolio.filter(status=status)

        return client_models.LoanPortfolio.objects.all()

    @login_required
    def resolve_loan_portfolio(self, info, id):
        return client_models.LoanPortfolio.objects.get(id=id)


class CreateLoanPortlioMutation(graphene.Mutation):
    class Arguments:
        portfolio = LoanPortfolioInput(required=True)

    portfolio = graphene.Field(LoanPortfolioType)

    def mutate(self, info, portfolio):
        p = client_models.LoanPortfolio.objects.create(**portfolio)
        return CreateLoanPortlioMutation(portfolio=p)


class LoanPortfolioMutation(graphene.ObjectType):
    create_loan_portfolio = CreateLoanPortlioMutation.Field()
