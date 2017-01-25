from django.utils.translation import ugettext_lazy as _
from django.db import models


DAYS_OF_WEEK = (
    (0, _('Pazartesi')),
    (1, _('Salı')),
    (2, _('Çarşamba')),
    (3, _('Perşembe')),
    (4, _('Cuma')),
    (5, _('Cumartesi')),
    (6, _('Pazar')),
)


class TimeStamp(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Oluşturulma Zamanı")
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Güncellenme Zamanı")
    )

    class Meta:
        abstract = True


class DateTimeInterval(TimeStamp):
    start_at = models.DateTimeField(
        verbose_name=_("Başlangıç Zamanı")
    )
    end_at = models.DateTimeField(
        verbose_name=_("Bitiş Zamanı")
    )

    class Meta:
        abstract = True


class DateInterval(TimeStamp):
    start_at = models.DateTimeField(
        verbose_name=_("Başlangıç Tarihi")
    )
    end_at = models.DateTimeField(
        verbose_name=_("Bitiş Tarihi")
    )

    class Meta:
        abstract = True


class DayTimeInterval(TimeStamp):
    start_day = models.CharField(
        max_length=1,
        choices=DAYS_OF_WEEK,
        verbose_name=_("Başlangıç Günü")
    )
    start_time = models.TimeField(
        verbose_name=_("Başlangıç Saati")
    )
    end_day = models.CharField(
        max_length=1,
        choices=DAYS_OF_WEEK,
        verbose_name=_("Bitiş Günü")
    )
    end_time = models.TimeField(
        verbose_name=_("Bitiş Saati")
    )

    class Meta:
        abstract = True
