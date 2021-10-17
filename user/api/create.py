from django.contrib.auth import models as auth_models


class UserExists(Exception):
    ...


class PhoneNumberExists(UserExists):
    ...


def create_user_without_password(username, **kwargs):
    if auth_models.User.objects.filter(username__iexact=username).exists():
        raise PhoneNumberExists(
            "User with phone number {} already exists.".format(username)
        )

    user = auth_models.User(username=username, **kwargs)
    user.set_unusable_password()
    user.save()

    return user
