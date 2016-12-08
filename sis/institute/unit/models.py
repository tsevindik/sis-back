from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...course.course.models import Course
from ...institute.facility.models import CampusBuilding
from ...common.models.time import TimeStamp
from ..institute.models import University


class UnitType(TimeStamp):
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )


class UniversityUnit(TimeStamp):
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )
    unit_type = models.ForeignKey(
        UnitType,
        verbose_name=_("Birim Türü")
    )


class UnitCourse(TimeStamp):
    course = models.ForeignKey(
        Course,
        verbose_name=_("Ders")
    )
    university_unit = models.ForeignKey(
        UniversityUnit,
        verbose_name=_("Üniversite Birimi")
    )


class UnitBuilding(TimeStamp):
    university_building = models.ForeignKey(
        UniversityUnit,
        verbose_name=_("Üniversite Birimi")
    )
    campus_building = models.ForeignKey(
        CampusBuilding,
        verbose_name=_("Kampüs Binası")
    )


# add translation models
from .trans_models import *
