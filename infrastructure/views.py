from graphene_django.views import GraphQLView
from graphene_file_upload.django import FileUploadGraphQLView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied


class SchmsoftGraphQLView(FileUploadGraphQLView):
    ...
    # @staticmethod
    # def format_error(error):
    #     formatted_error = super(FileUploadGraphQLView).format_error(error)

    #     try:
    #         formatted_error["context"] = error.original_error.context
    #     except AttributeError:
    #         pass

    #     return formatted_error


class LoginRequiredSchmsoftGraphQLView(LoginRequiredMixin, SchmsoftGraphQLView):
    def handle_no_permission(self):
        raise PermissionDenied
