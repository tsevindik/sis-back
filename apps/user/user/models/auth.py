from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.postgres.fields import JSONField

from config.settings.common import AUTH_USER_MODEL
from utils.models import time as time_models


class UserPermission(time_models.TimeStamp):
    """
    Attributes:
        user: user having specified permissions
        data: all permission related data
            Sample JSON:
                {
                    rowLevelPermission: {
                        isPermitted: boolean,       // Is permitted to change?
                        forAll: boolean,            // Is permitted to change all?
                        permittedIds: [number],     // If not permitted to change all, then permitted to change what?
                    }, ...
                    , modelLevelPermission: boolean, ...
                }
            Row Level Permissions: university, unit, program, course, section
            Model Level Permissions: nothing for now
    """
    user = models.OneToOneField(
        AUTH_USER_MODEL,
        verbose_name=_("Kullanıcı")
    )
    data = JSONField(
        verbose_name=_("Veri")
    )
