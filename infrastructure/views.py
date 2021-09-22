from django.shortcuts import render
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured, PermissionDenied
from django.contrib.auth.views import redirect_to_login


class AccessMixin:
    """Anstract CBV mixin that gives access mixin the same customizable functionality"""

    login_url = None
    permission_denied_message = ""
    raise_exception = False
    redirect_field_name = REDIRECT_FIELD_NAME

    def get_login_url(self):
        """Override this method to override the login_url attribute"""
        login_url = self.login_url or settings.LOGIN_URL
        if not login_url:
            raise ImproperlyConfigured(
                "{0} is missing the login_url attribute. Define {0}.login_url, settings.LOGIN_URL or override {0}.get_login_url().".format(
                    self.__class__.__name__
                )
            )
        return str(login_url)

    def get_permission_denied_message(self):
        """Override this method to override the permission_denied_message attribute"""
        return self.permission_denied_message

    def get_redirect_field_name(self):
        """Override this method to override the redirect_field_name attribute"""
        return self.redirect_field_name

    def handle_no_permission(self):
        if self.raise_exception or self.request.user.is_authenticated:
            raise PermissionDenied(self.get_permission_denied_message())

        return redirect_to_login(
            self.request.get_full_path(),
            self.get_login_url(),
            self.get_redirect_field_name(),
        )

