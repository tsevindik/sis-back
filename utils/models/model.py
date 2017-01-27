from django.utils.translation import ugettext_lazy as _
from django.db import models


class SisModel(models.Model):
    class Meta:
        default_permissions = (("read", _("Can read")), ("add", _("Can add")),
                               ("change", _("Can change")), ("delete", _("Can delete")))
        abstract = True
