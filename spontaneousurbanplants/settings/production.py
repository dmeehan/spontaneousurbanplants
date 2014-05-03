import os

from base import *


#==============================================================================
# Site
#==============================================================================
# See: https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
#ALLOWED_HOSTS = ['spontaneousurbanplants.org', 'www.spontaneousurbanplants.org', 'smtp.webfaction.com']


#==============================================================================
# Email
#==============================================================================
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = 'smtp.webfaction.com'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = os.environ.get('DJANGO_EMAIL_HOST_PASSWORD', '')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = 'futuregreen'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = '587'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_USE_TLS = 'True'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = 'admin@spontaneousurbanplants.org'

DEFAULT_FROM_EMAIL = 'Spontaneous Urban Plants <info@spontaneousurbanplants.org>'


#==============================================================================
# Installed Apps
#==============================================================================



#==============================================================================
#  Celery
#==============================================================================


BROKER_URL = "redis://localhost:6379/0"

#==============================================================================
#  Databases
#==============================================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ.get('DJANGO_DB_NAME', ''),
        'USER': os.environ.get('DJANGO_DB_USER', ''),
        'PASSWORD': os.environ.get('DJANGO_DB_PASSWORD', ''),
        'HOST': 'localhost',
        'PORT': '',
    }
}
