import base64
import requests

from enum import Enum
from django.conf import settings


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


def _auth_headers(token):
    return {"Authorization": f"Basic {token}"}


def _raise_monyera_error(response):
    ...


def send(
    data: dict,
):
    token = get_token(settings.MONYERA_USERNAME, settings.MONYERA_PASSWORD)

    if "options" in data:
        data.options["senderId"] = settings.SENDER_ID
    else:
        data.update(options=dict(senderId=settings.SENDER_ID))

    response = requests.post(
        _monyera_url(Endpoints.SEND),
        data=data,
        headers=_auth_headers(token),
    )
    _raise_monyera_error(response)

    return response.json()


def get_token(username: str, password: str) -> str:
    username_password_string = f"{username}:{password}".encode("ascii")
    return base64.b64encode(username_password_string).decode("ascii")
