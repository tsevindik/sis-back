from django.db import models


class UniversityConfigQuerySet(models.QuerySet):
    def get_single(self):
        return self.all()[:1].get()

    def get_primary_university(self):
        return self.prefetch_related('primary_university').get_single().primary_university


class UniversityQuerySet(models.QuerySet):
    pass
