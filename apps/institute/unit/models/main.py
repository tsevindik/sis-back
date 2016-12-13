from django.utils.translation import ugettext_lazy as _
from django.db import models

from apps.course.course.models import Course
from apps.institute.facility.models import CampusBuilding
from apps.institute.institute.models import University
from .utils import AppTimeStamp


class UnitType(AppTimeStamp):
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )


class UniversityUnit(AppTimeStamp):
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )
    unit_type = models.ForeignKey(
        UnitType,
        verbose_name=_("Birim Türü")
    )


class UnitCourse(AppTimeStamp):
    course = models.ForeignKey(
        Course,
        verbose_name=_("Ders")
    )
    university_unit = models.ForeignKey(
        UniversityUnit,
        verbose_name=_("Üniversite Birimi")
    )


class UnitBuilding(AppTimeStamp):
    university_building = models.ForeignKey(
        UniversityUnit,
        verbose_name=_("Üniversite Birimi")
    )
    campus_building = models.ForeignKey(
        CampusBuilding,
        verbose_name=_("Kampüs Binası")
    )
