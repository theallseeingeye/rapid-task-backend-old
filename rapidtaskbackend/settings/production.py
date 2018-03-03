from .base import *

DEBUG = True

ALLOWED_HOSTS = ['poopyassworks.us-west-2.elasticbeanstalk.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['RDS_DB_NAME'],
        'USER': os.environ['RDS_USERNAME'],
        'PASSWORD': os.environ['RDS_PASSWORD'],
        'HOST': os.environ['RDS_HOSTNAME'],
        'PORT': os.environ['RDS_PORT']
    },
}

SECRET_KEY = os.environ("DJANGO_SECRET_KEY")