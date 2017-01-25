from django.utils.translation import ugettext_lazy as _
from django.db import models

from ...user.models import UserAddress, UserPhone
from ...worker.models import WorkStatus, WorkerProfile


class StaffProfile(WorkerProfile):
    work_status = models.ManyToManyField(
        WorkStatus
    )


class StaffPhone(UserPhone):
    pass


class StaffAddress(UserAddress):
    pass
