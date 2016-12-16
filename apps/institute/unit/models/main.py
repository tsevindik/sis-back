from django.utils.translation import ugettext_lazy as _
from django.db import models

from utils.models import time as time_models
from apps.course.course.models import Course
from apps.institute.facility.models import CampusBuilding


class UnitType(time_models.TimeStamp):
    pass


class Unit(time_models.TimeStamp):
    unit_type = models.ForeignKey(
        UnitType,
        verbose_name=_("Birim Türü")
    )


class UnitCourse(time_models.TimeStamp):
    course = models.ForeignKey(
        Course,
        verbose_name=_("Ders")
    )
    unit = models.ForeignKey(
        Unit,
        verbose_name=_("Birim")
    )


class UnitBuilding(time_models.TimeStamp):
    unit = models.ForeignKey(
        Unit,
        verbose_name=_("Birim")
    )
    campus_building = models.ForeignKey(
        CampusBuilding,
        verbose_name=_("Kampüs Binası")
    )
