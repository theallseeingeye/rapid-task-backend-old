from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os


# This sets up the user for the admin on the initial build of the api. AWS doesn't have
# a feature to setup the initial credentials on launch/deploy. This Command script allows
# us to tell AWS to create a superuser on build.

# To change the settings of the os.environ- Go to the aws eb environment- software configuration - environment variables


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username=os.environ["SUPERUSERNAME"]).exists():
            User.objects.create_superuser(
                os.environ['SUPERUSERNAME'],
                os.environ['SUPERUSEREMAIL'],
                os.environ['SUPERUSERPASSWORD']
            )
