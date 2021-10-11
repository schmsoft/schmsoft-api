class CodeExceptionMixin:
    EXCEPTION_CODE = "error"

    def __init__(self, *args, **kwargs) -> None:
        # Replace any message with an error code
        super().__init__(self.EXCEPTION_CODE)


class CouldNotEmail(CodeExceptionMixin, Exception):
    EXCEPTION_CODE = "could-not-email"


class UserExists(CodeExceptionMixin, Exception):
    EXCEPTION_CODE = "user-exists"


class UserNotLoggedIn(CodeExceptionMixin, Exception):
    EXCEPTION_CODE = "user-not-logged-in"


class GraphQLExceptionMixin(Exception):
    def __init__(self, message, status=None):
        self.context = {}
        if status:
            self.context["status"] = status
        super().__init__(message)
