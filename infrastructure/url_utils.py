from django.conf import settings
from django.contrib.sites.models import Site


def absolute_url(path, base_url=None, scheme=None):
    if not scheme:
        scheme = settings.DEFAULT_URL_SCHEME
    if not base_url:
        base_url = Site.objects.get_current().domain

    return "%s://%s%s" % (scheme, base_url, path)
