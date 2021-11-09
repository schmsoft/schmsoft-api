import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth import models as auth_models

from graphql_jwt.decorators import login_required, superuser_required

from client import models as client_models


class LoanPortfolioType(DjangoObjectType):
    class Meta:
        model = client_models.LoanPortfolio


class LoanPortfolioInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    description = graphene.String(required=True)


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


class AddLoanPortlioMutation(graphene.Mutation):
    class Arguments:
        portfolio = LoanPortfolioInput(required=True)

    portfolio = graphene.Field(LoanPortfolioType)

    def mutate(self, info, portfolio):
        loan_portfolio = client_models.LoanPortfolio.objects.create(**portfolio)
        return AddLoanPortlioMutation(portfolio=loan_portfolio)


class UpdateLoanPortfolioMutation(graphene.Mutation):
    class Arguments:
        portfolio_id = graphene.ID(required=True)
        portfolio = LoanPortfolioInput()

    portfolio = graphene.Field(LoanPortfolioType)

    @login_required
    def mutate(self, info, portfolio_id, portfolio):
        loan_portfolio = client_models.LoanPortfolio.objects.get(id=portfolio_id)

        client_models.LoanPortfolio.objects.filter(id=portfolio_id).update(**portfolio)

        return UpdateLoanPortfolioMutation(portfolio=loan_portfolio)


class AssignPortfolioManagerMutation(graphene.Mutation):
    class Arguments:
        portfolio_id = graphene.ID(required=True)
        user_id = graphene.ID(required=True)

    success = graphene.Boolean()

    @login_required
    @superuser_required
    def mutate(self, info, portfolio_id, user_id):
        portfolio = client_models.LoanPortfolio.objects.filter(id=portfolio_id).first()

        if portfolio is None:
            raise Exception("Invalid loan portfolio")

        owner = auth_models.User.objects.get(id=user_id)
        portfolio.owners.add(owner)

        return AssignPortfolioManagerMutation(success=True)


class UnAssignPortfolioManagerMutation(graphene.Mutation):
    class Arguments:
        portfolio_id = graphene.ID(required=True)
        user_id = graphene.ID(required=True)

    success = graphene.Boolean()

    @login_required
    @superuser_required
    def mutate(self, info, portolio_id, user_id):
        portfolio = client_models.LoanPortfolio.objects.filter(id=portolio_id).first()

        if portfolio is None:
            raise Exception("Invalid loan portfolio")

        owner = auth_models.User.objects.get(id=user_id)
        portfolio.owners.remove(owner)

        return UnAssignPortfolioManagerMutation(success=True)


class UpdatePortfolioManagers(graphene.Mutation):
    class Arguments:
        portfolio_id = graphene.ID(required=True)
        user_ids = graphene.List(graphene.ID, required=True)

    success = graphene.Boolean()

    @login_required
    @superuser_required
    def mutate(self, info, portfolio_id, user_ids):
        portfolio = client_models.LoanPortfolio.objects.get(id=portfolio_id)
        if portfolio is None:
            raise Exception("Invalid portfolio")

        owners = auth_models.User.objects.filter(id__in=user_ids)
        portfolio.owners.clear()
        portfolio.owners.set(owners)

        return UpdatePortfolioManagers(success=True)


class LoanPortfolioMutation(graphene.ObjectType):
    add_loan_portfolio = AddLoanPortlioMutation.Field()
    update_loan_portfolio = UpdateLoanPortfolioMutation.Field()
    assign_portfolio_manager = AssignPortfolioManagerMutation.Field()
    un_assign_portfolio_manager = UnAssignPortfolioManagerMutation.Field()
    update_portfolio_managers = UpdatePortfolioManagers.Field()
