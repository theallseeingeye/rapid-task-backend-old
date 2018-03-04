from .base import *


# import json
#
# from django.core.exceptions import ImproperlyConfigured
#
# # JSON-based secrets module. This is where it looks for the secret key file and reads it.
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
# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = get_secret('SECRET_KEY')


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rapidtaskdatabase',
        'USER': 'postgres',
        'PASSWORD': get_secret('DATABASE_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    },
}