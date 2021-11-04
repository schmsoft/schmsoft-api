from django.contrib.auth import models as auth_users


def get_active_users():
    users = auth_users.User.objects.filter(active=True)
    return users


def list_staff_users():
    users = auth_users.User.objects.filter(is_active=True, is_staff=True)

    return users
