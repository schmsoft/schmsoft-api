"""schmsoft URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include, re_path
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import RedirectView

from infrastructure import views as infrastructure_views

from django.conf import settings

from schmsoft.schema import public as schmsoft_schema_public


urlpatterns = [
    re_path(r"^$", RedirectView.as_view(url="admin/")),
    path("grappelli/", include("grappelli.urls")),  # grappelli URLS
    path("admin/", admin.site.urls),
    path("integrations/", include("integrations.urls")),
    path(
        "graphql",
        csrf_exempt(
            infrastructure_views.LoginRequiredSchmsoftGraphQLView.as_view(
                graphiql=settings.DEBUG
            )
        ),
    ),
    path(
        "graphql-public",
        csrf_exempt(
            infrastructure_views.SchmsoftGraphQLView.as_view(
                graphiql=settings.DEBUG, schema=schmsoft_schema_public.PUBLIC_SCHEMA
            )
        ),
    ),
]
