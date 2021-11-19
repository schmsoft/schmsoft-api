from django.contrib.auth import mixins as auth_mixins
from graphql_jwt.utils import get_credentials


class CodedExceptionMixin:
    EXCEPTION_CODE = "error"

    def __init__(self, *args, **kwargs) -> None:
        # Replace any message with an error code
        super().__init__(self.EXCEPTION_CODE)


class AuthTokenRequiredMixed(auth_mixins.AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        token = get_credentials(request)

        if not (token or request.user.is_authenticated):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
