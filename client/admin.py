from django.contrib import admin

from client import models as client_models


class BusinessAdmin(admin.ModelAdmin):
    ...


class OwnerAdmin(admin.ModelAdmin):
    ...


class LoanPortfolioAdmin(admin.ModelAdmin):
    ...


# Register your models here.
admin.site.register(client_models.Business, BusinessAdmin)
admin.site.register(client_models.Owner, OwnerAdmin)
admin.site.register(client_models.LoanPortfolio, LoanPortfolioAdmin)
