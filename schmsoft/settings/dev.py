from schmsoft.settings import *

DEBUG = True

GRAPHQL_JWT = {
    "JWT_EXPIRATION_DELTA": timedelta(days=7),
}
