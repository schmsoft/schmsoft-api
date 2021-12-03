from schmsoft.settings import *

DEBUG = True

GRAPHQL_JWT = {
    "JWT_EXPIRATION_DELTA": timedelta(days=7),
}

# When generating reversed URLs, use HTTP
DEFAULT_URL_SCHEME = "http"
