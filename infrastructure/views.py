from graphene_file_upload.django import FileUploadGraphQLView
from django.core.exceptions import PermissionDenied
from infrastructure import exceptions as infrastructure_exceptions
from .mixins import AuthTokenRequiredMixed


class SchmsoftGraphQLView(FileUploadGraphQLView):
    @staticmethod
    def format_error(error):
        formatted = FileUploadGraphQLView.format_error(error)

        original_error = getattr(error, "original_error", None)
        if original_error and isinstance(
            original_error, infrastructure_exceptions.CodedExceptionMixin
        ):
            formatted["message"] = getattr(original_error, "EXCEPTION_CODE", None)
        return formatted


class LoginRequiredSchmsoftGraphQLView(AuthTokenRequiredMixed, SchmsoftGraphQLView):
    def handle_no_permission(self):
        raise PermissionDenied
