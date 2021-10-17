from client import models as client_models


def update_or_create_owner(owner_input, **kwargs):
    owner, _ = client_models.Owner.objects.update_or_create(**owner_input, **kwargs)
    return owner


def update_owner_passport_photo(owner, passport_photo):
    owner.passport_photo.save(passport_photo.name, passport_photo, save=True)
