from rest_framework.views import APIView
from rest_framework.response import Response

from integrations.kopokopo import webhooks as kopokopo_webhooks


class KopoKopoWebhook(APIView):
    def post(self, request, *args, **kwargs):
        kopokopo_webhooks.handle()
        return Response({})
