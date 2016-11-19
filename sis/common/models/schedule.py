from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...institute.facility.models import CampusPlace
from .time import DateTimeInterval, TimeStamp


ATTENDANCE_STATUS = (
    (0, _('Var')),
    (1, _('Yok')),
    (2, _('Geç')),
    (3, _('Mazeretli'))
)


class CampusEvent(DateTimeInterval):
    place = models.ForeignKey(
        CampusPlace,
        null=True,
        blank=True
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
