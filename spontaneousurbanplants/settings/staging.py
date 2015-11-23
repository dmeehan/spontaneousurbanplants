import os

from base import *

#==============================================================================
# Debugging
#==============================================================================

DEBUG = True

#==============================================================================
# Site
#==============================================================================
# See: https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = ['test.spontaneousurbanplants.org']

SITE_ID = 4


##==============================================================================
# Email Configuration
#==============================================================================
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


#==============================================================================
# Installed Apps
#==============================================================================

#INSTALLED_APPS += (
	#'debug_toolbar',  
#)

#DEBUG_TOOLBAR_PATCH_SETTINGS = False

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

#==============================================================================
# Caching
#==============================================================================
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}



