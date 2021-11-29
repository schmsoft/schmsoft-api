from django.conf import settings

from integrations.monyera import api as monyera_api


def contact(
    to: list or str,
    text: str,
    sender_id=settings.SENDER_ID,
    is_flash=False,
    is_unicode=False,
    dispatch_at=None,
):
    return monyera_api.send(
        to,
        text,
        sender_id=sender_id,
        is_flash=is_flash,
        is_unicode=is_unicode,
        dispatch_at=dispatch_at,
    )
