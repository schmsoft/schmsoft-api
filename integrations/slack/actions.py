from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from django.conf import settings


def _client():
    return WebClient(token=settings.SLACK_BOT_TOKEN)


def send_message(channel, text):
    try:
        _client().chat_postMessage(channel=channel, text=text)
    except SlackApiError as err:
        pass


def send_notification(text):
    return send_message(settings.SLACK_NOTIFICATIONS_CHANNEL, text)
