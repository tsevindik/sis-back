from django.utils.translation import ugettext_lazy as _
from django.db import models

from apps.institute.facility import models as facility_models
from .time import DateTimeInterval, TimeStamp


ATTENDANCE_STATUS = (
    (0, _('Var')),
    (1, _('Yok')),
    (2, _('Geç')),
    (3, _('Mazeretli'))
)

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


class Attendance(TimeStamp):
    status = models.CharField(
        max_length=1,
        choices=ATTENDANCE_STATUS,
        verbose_name=_("Durum")
    )

    class Meta:
        abstract = True