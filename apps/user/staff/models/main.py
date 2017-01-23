from django.utils.translation import ugettext_lazy as _
from django.db import models

from apps.user.utils import models as user_models
from apps.user.worker.models import WorkStatus


class StaffProfile(user_models.WorkerProfile):
    work_status = models.ManyToManyField(
        WorkStatus
    )


class StaffPhone(user_models.UserPhone):
    pass


class StaffAddress(user_models.UserAddress):
    pass
