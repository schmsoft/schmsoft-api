from graphql_jwt.decorators import user_passes_test

from .exceptions import UserNotLoggedIn


login_required = user_passes_test(lambda u: u.is_authenticated, exc=UserNotLoggedIn)
