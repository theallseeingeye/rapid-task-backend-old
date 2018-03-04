from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.core.exceptions import ImproperlyConfigured
# import json
import os


# This sets up the user for the admin on the initial build of the api. AWS doesn't have
# a feature to setup the initial credentials on launch/deploy. This Command script allows
# us to tell AWS to create a superuser on build.

# JSON-based secrets module. This is where it looks for the secret key file and reads it.
# with open('secrets.json') as f:
#     secrets = json.loads(f.read())
#
#
# def get_secret(setting, secrets=secrets):
#     # Get the secret variable or return explicit exception.
#     try:
#         return secrets[setting]
#     except KeyError:
#         error_msg = 'Set the {0} environment variable'.format(setting)
#         raise ImproperlyConfigured(error_msg)
#

class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username=os.environ("SUPERUSERNAME")).exists():
            User.objects.create_superuser(
                os.environ('SUPERUSERNAME'),
                os.environ('SUPERUSEREMAIL'),
                os.environ('SUPERUSERPASSWORD')
            )
