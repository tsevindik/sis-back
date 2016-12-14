from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import time as time_models
from apps.course.course.models import Course
from apps.institute.facility.models import CampusBuilding
from apps.institute.institute.models import University


class UnitType(time_models.TimeStamp):
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )


class UniversityUnit(time_models.TimeStamp):
    university = models.ForeignKey(
        University,
        verbose_name=_("Üniversite")
    )
    unit_type = models.ForeignKey(
        UnitType,
        verbose_name=_("Birim Türü")
    )


class UnitCourse(time_models.TimeStamp):
    course = models.ForeignKey(
        Course,
        verbose_name=_("Ders")
    )
    university_unit = models.ForeignKey(
        UniversityUnit,
        verbose_name=_("Birim")
    )


class UnitBuilding(time_models.TimeStamp):
    university_building = models.ForeignKey(
        UniversityUnit,
        verbose_name=_("Birim")
    )
    campus_building = models.ForeignKey(
        CampusBuilding,
        verbose_name=_("Kampüs Binası")
    )
