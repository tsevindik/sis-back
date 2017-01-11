import glob
import os

from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Removes all migrations."
    app_directory = "apps"

    def handle(self, *args, **options):
        try:
            for filename in glob.iglob("{0}/**/migrations/*.py".format(self.app_directory), recursive=True):
                if filename.split("/")[-1] != "__init__.py":
                    os.remove(filename)
        except OSError:
            print("File may not exist.")
