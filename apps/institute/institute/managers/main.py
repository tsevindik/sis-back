from django.db import models


class UniversityConfigManager(models.Manager):
    def get(self):
        return self.all()[:1].get()
