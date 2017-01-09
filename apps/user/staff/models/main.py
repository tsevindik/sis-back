from django.utils.translation import ugettext_lazy as _
from django.db import models

from apps.user.utils import models as user_models


class StaffProfile(user_models.WorkerProfile):
    pass


class StaffPhone(user_models.UserPhone):
    pass


class StaffAddress(user_models.UserAddress):
    pass
