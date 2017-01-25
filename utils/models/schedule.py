from django.utils.translation import ugettext_lazy as _
from django.db import models

from apps.property.facility import models as facility_models
from .time import DateTimeInterval


IMPLEMENTATION_TYPE = (
    (0, _('Uzak')),
    (1, _('Yerel'))
)


class CampusEvent(DateTimeInterval):
    building_room = models.ForeignKey(
        facility_models.BuildingRoom,
        null=True,
        blank=True,
        verbose_name=_("Yer")
    )

    class Meta:
        abstract = True
