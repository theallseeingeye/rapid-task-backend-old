from .base import *
import os

DEBUG = True

ALLOWED_HOSTS = [
    'backend-init-deploy-test.us-west-2.elasticbeanstalk.com',
    '.rapidtask.com'
    ]


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

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']


# Forces the use of cookies over HTTPS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# This prevents access to the stored data from JavaScript
SESSION_COOKIE_HTTPONLY = True

# Django honeypot admin page settings
# This will send any logged attempts to the /admin page to all the administrator's emails.
ADMIN_HONEYPOT_EMAIL_ADMIN = True

# Django email settings
# Note: This will need to be changed for production setting using a different email service.
# Google is not a transactional email service and not made for web applications.
EMAIL_BACKEND = 'django.cor.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'sikstrom@rapidtask.com'
EMAIL_HOST_PASSWORD = os.environ['EMAIL_PASSWORD']
EMAIL_USE_TLS = True
# EMAIL_USE_SSL = True
# EMAIL_SSL_CERTFILE = None
# EMAIL_SSL_KEYFILE = None
# EMAIL_TIMEOUT = None

# HTTP Strict Transport Security - Forces browsers to use HTTPS
# The time is telling the browser how long to remember the forced redirect to HTTPS
SECURE_HSTS_SECONDS = 3600 # This is 1 hour- change to one year after testing is done. Google wants to see 63072000 after all the testings are done.
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SECURE_CONTENT_TYPE_NOSNIFF = True # Ensures that browsers to identify content types correctly.
SECURE_BROWSER_XSS_FILTER = True # Helps prevents XSS attacks
SECURE_SSL_REDIRECT = True

X_FRAME_OPTIONS = 'DENY' # Change to SAMEORIGIN if we choose to use iframes with google maps.

CORS_ORIGIN_WHITELIST = (
    'www.rapidtask.com',
    'rapidtask.com',
)