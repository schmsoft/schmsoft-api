from .mixins import CodedExceptionMixin


class CouldNotEmail(CodedExceptionMixin, Exception):
    EXCEPTION_CODE = "could-not-email"


class UserExists(CodedExceptionMixin, Exception):
    EXCEPTION_CODE = "user-exists"


class UserNotLoggedIn(CodedExceptionMixin, Exception):
    EXCEPTION_CODE = "user-not-logged-in"


class GraphQLExceptionMixin(Exception):
    def __init__(self, message, status=None):
        self.context = {}
        if status:
            self.context["status"] = status
        super().__init__(message)
