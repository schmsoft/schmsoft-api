from django.urls import re_path
from integrations.kopokopo import views as kopokopo_views

app_name = "integrations"
urlpatterns = [
    re_path(
        r"kopokopo/webhook/$",
        kopokopo_views.KopoKopoWebhook.as_view(),
        name="kopokopo-webhook-callback",
    ),
]
