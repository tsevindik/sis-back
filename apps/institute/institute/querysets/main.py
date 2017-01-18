from django.db import models


class UniversityConfigQuerySet(models.QuerySet):
    def get_single(self):
        return self.all()[:1].get()


class UniversityQuerySet(models.QuerySet):
    def get_primary(self):
        return self.get(is_primary=True)
