from django.core.exceptions import ObjectDoesNotExist
from django.db import models

from apps.institute.institute.models import main


class TransQuerySet(models.QuerySet):
    def get_by_language(self, language_code):
        return self.get(language_code=language_code)

    def get_by_default_language(self):
        university_config = main.UniversityConfig.objects.get()
        return self.get(language_code=university_config.default_language)

    def get_by_language_or_default(self, language_code):
        try:
            return self.get(language_code=language_code)
        except ObjectDoesNotExist:  # TODO: There must be a proper way
            return self.get_by_default_language()

    class Meta:
        abstract = True