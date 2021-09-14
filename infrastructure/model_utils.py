import hashids
import string

from django.db.models import Manager, Model
from django.contrib.contenttypes.models import ContentType


EXTERNAL_IDS_MIN_LENGTH = 12
EXTERNAL_IDS_MAX_LENGTH = 16
EXTERNAL_HASH_IDS = hashids.Hashids(
    alphabet="{0}{1}".format(string.digits, string.ascii_lowercase),
    salt="smallbusinesseswithmoney",
    min_length=EXTERNAL_IDS_MIN_LENGTH,
)


class ExternalIdManagerMixin:
    def get_by_external_id(self, external_id, **kwargs):
        return self.get(
            pk=internal_id_from_model_and_external_id(self.model, external_id), **kwargs
        )


def internal_id_from_model_and_external_id(model, external_id):
    ...


def external_id_from_instance(instance):
    return EXTERNAL_HASH_IDS.encode(
        ContentType.objects.get_for_model(instance).id,
        instance.id,
    )


class ExternalIdManager(ExternalIdManagerMixin, Manager):
    pass


class ExternalIdModel(Model):
    objects = ExternalIdManager()

    class Meta:
        abstract = True

    @classmethod
    def get_internal_id(cls, external_id):
        return internal_id_from_model_and_external_id(cls, external_id)

    @property
    def external_id(self):
        return external_id_from_instance(self)


class SchmsoftModel(ExternalIdModel):
    objects = ExternalIdManager()

    class Meta:
        abstract = True

    @property
    def is_unsaved(self):
        return not self.id

    