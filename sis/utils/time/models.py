from django.utils.translation import ugettext_lazy as _
from django.db import models


DAYS_OF_WEEK = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday'),
)


class DateTimeInterval(models.Model):
    start_at = models.DateTimeField(verbose_name=_("Başlangıç Tarih ve Saati"))
    end_at = models.DateTimeField(verbose_name=_("Bitiş Tarih ve Saati"))


class DateInterval(models.Model):
    start_at = models.DateTimeField(verbose_name=_("Başlangıç Tarihi"))
    end_at = models.DateTimeField(verbose_name=_("Bitiş Tarihi"))


class DayTimeInterval(models.Model):
    start_day = models.CharField(max_length=1, choices=DAYS_OF_WEEK)
    start_time = models.DateTimeField(verbose_name=_("Başlangıç Saati"))
    end_day = models.CharField(max_length=1, choices=DAYS_OF_WEEK)
    end_time = models.DateTimeField(verbose_name=_("Bitiş Saati"))
