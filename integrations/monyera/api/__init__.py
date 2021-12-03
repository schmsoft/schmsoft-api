import base64
import requests

from enum import Enum
from django.conf import settings
from requests.api import get


BASE_URL = "http://desma-api.herokuapp.com/v1/messaging/sms"


class Endpoints(Enum):
    SEND = "/send"
    BALANCE = "/balance"


class MonyeraException(Exception):
    def __init__(self, code: int, error: str, requests_exception=None):
        self.code = code
        self.error = error
        self.requests_exception = requests_exception


def _monyera_url(endpoint: Endpoints, url_params: list = None):
    url = BASE_URL + endpoint.value
    if url_params:
        url = url + "/" + "/".join(url_params)
    return url


def _headers(token):
    return {
        "Authorization": f"Basic {token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }


def _monyera_options(**kwargs):
    options = dict(
        senderId=kwargs.get("sender_id", settings.SENDER_ID),
        isFlash=kwargs.get("is_flash"),
        dispatchAt=kwargs.get("dispatch_at"),
        isUnicode=kwargs.get("is_unicode"),
    )

    return options


def _raise_monyera_error(response):
    ...


def send(to: str or list, text: str, **kwargs):
    data = dict(to=to, text=text, options=_monyera_options(**kwargs))

    token = get_token(settings.MONYERA_USERNAME, settings.MONYERA_PASSWORD)

    response = requests.post(
        _monyera_url(Endpoints.SEND),
        json=data,
        headers=_headers(token),
    )
    _raise_monyera_error(response)

    return response.json()


def get_token(username: str, password: str) -> str:
    username_password_string = f"{username}:{password}".encode("ascii")
    return base64.b64encode(username_password_string).decode("ascii")
