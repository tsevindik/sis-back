from django.utils.translation import ugettext_lazy as _
from django.db import models


class University(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name=_("İsim"))
