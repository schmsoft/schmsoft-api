from schmsoft.settings import *

DEBUG = True

GRAPHQL_JWT = {
    "JWT_VERIFY_EXPIRATION": True,
    "JWT_LONG_RUNNING_REFRESH_TOKEN": True,
    "JWT_EXPIRATION_DELTA": timedelta(days=3),
    "JWT_REFRESH_EXPIRATION_DELTA": timedelta(days=7),
}

# When generating reversed URLs, use HTTP
DEFAULT_URL_SCHEME = "http"
