# settings/base.py

import os
from datetime import timedelta
from os.path import abspath, basename, dirname, join, normpath
from sys import path

from djcelery import setup_loader

from django.core.urlresolvers import reverse_lazy

#==============================================================================
# Path 
#==============================================================================

# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(DJANGO_ROOT)

# Absolute filesystem path to project container folder:
PROJECT_ROOT = dirname(SITE_ROOT) 

# Absolute filesystem path to project container folder:
APP_ROOT = normpath(join(DJANGO_ROOT, 'apps')),

# Site name:
SITE_NAME = basename(DJANGO_ROOT)

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(DJANGO_ROOT)
path.append(APP_ROOT)


#==============================================================================
# Managers 
#==============================================================================

ADMINS = (
    ('Douglas Meehan', 'dmeehan@gmail.com'),
)

MANAGERS = ADMINS

#==============================================================================
# Site 
#==============================================================================

SITE_ID = 1

# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

#==============================================================================
# Debugging
#==============================================================================

# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG


#==============================================================================
# Secret Key 
#==============================================================================

# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '87hq#$x_zu_=r)polio0q1y*$ii2z4wt82cqpx=167wt4lsa83$')


#==============================================================================
# Localization
#==============================================================================

TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
USE_I18N = True    #internationalization machinery
USE_L10N = True    #format dates, numbers and calendars according to locale
USE_TZ = False

#==============================================================================
# Database Configuration
#==============================================================================
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'sup',
        'USER': 'sup',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}

#==============================================================================
# Fixtures
#==============================================================================

# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    normpath(join(SITE_ROOT, 'fixtures')),
)


#==============================================================================
# Static assets
#==============================================================================

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = normpath(join(PROJECT_ROOT, 'assets'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/assets/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    normpath(join(DJANGO_ROOT, 'static')),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

#==============================================================================
# Uploaded assets 
#==============================================================================

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = normpath(join(PROJECT_ROOT, 'media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'

#==============================================================================
# Templates
#==============================================================================


# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs

TEMPLATE_DIRS = (
    normpath(join(DJANGO_ROOT, 'templates')),
)

#==============================================================================
# Middleware
#==============================================================================


# See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES = (
    # Default Django middleware.
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


#==============================================================================
# Project URLS
#==============================================================================


# See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = 'urls'



#==============================================================================
# Messages
#==============================================================================

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'


#==============================================================================
# Authentication
#==============================================================================

AUTH_USER_MODEL = 'auth.User'
LOGIN_URL = reverse_lazy('admin:index')


#==============================================================================
# Installed Apps
#==============================================================================

DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # gis add-ons
    'django.contrib.gis',

    # Useful template tags:
    'django.contrib.humanize',

    # Admin panel and documentation:
    'grappelli.dashboard',
    'grappelli',
    'django.contrib.admin',
    # 'django.contrib.admindocs',
)

THIRD_PARTY_APPS = (
    'compressor', # static file management
    'djsupervisor', # process mgmt
    'endless_pagination', # AJAX pagination
    'leaflet', # maps
    'notification', # event notifications
    'rest_framework', # api
    'rest_framework_gis', # api geo add-ons
)

# Apps specific for this project go here.
LOCAL_APPS = (
    'apps.about',
    'apps.instamedia',
    'apps.map',
    'apps.news',
    'apps.plants',
    'apps.services',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


#==============================================================================
# Logging
#==============================================================================

 
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
            },
        }
}

#==============================================================================
# Server Configuration
#==============================================================================

# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'wsgi.application'

SERVER_PORT = os.environ.get("SERVER_PORT", "8000")

#==============================================================================
# Compression 
#==============================================================================


COMPRESS_PRECOMPILERS = (
    ('text/x-sass', 'sass {infile} {outfile}'),
    ('text/x-scss', 'sass --scss {infile} {outfile}'),
)

# See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_ENABLED

# See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_CSS_FILTERS
COMPRESS_CSS_FILTERS = [
    'compressor.filters.template.TemplateFilter',
]

# See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_JS_FILTERS
COMPRESS_JS_FILTERS = [
    'compressor.filters.template.TemplateFilter',
]

#==============================================================================
# Caching
#==============================================================================

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}


#==============================================================================
# ASync
#==============================================================================

# See: http://celery.readthedocs.org/en/latest/configuration.html#celery-task-result-expires
CELERY_TASK_RESULT_EXPIRES = timedelta(minutes=30)

# See: http://docs.celeryproject.org/en/master/configuration.html#std:setting-CELERY_CHORD_PROPAGATES
CELERY_CHORD_PROPAGATES = True

# See: http://celery.github.com/celery/django/
setup_loader()

#==============================================================================
# API
#==============================================================================

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny',),
    'PAGINATE_BY': 10
}


#==============================================================================
# Admin
#==============================================================================

GRAPPELLI_ADMIN_TITLE = 'Spontanous Urban Plants'
GRAPPELLI_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'

#==============================================================================
# Front End Assets
#==============================================================================


#==============================================================================
# API keys 
#==============================================================================

INSTAGRAM_CLIENT_ID = os.environ.get('INSTAGRAM_CLIENT_ID', '')
INSTAGRAM_CLIENT_SECRET = os.environ.get('INSTAGRAM_CLIENT_SECRET', '')

INSTAGRAM_REALTIME_CALLBACK_URL = 'http://spontaneousurbanplants.org/feed/realtime_callback/'



#==============================================================================
# Other 3rd Party
#==============================================================================

NOTIFICATION_BACKENDS = [
    ("email", "notification.backends.email.EmailBackend"),
]

LEAFLET_CONFIG = {
    'TILES': 'http://api.tiles.mapbox.com/v3/mnegret.i9i0hhj2/{z}/{x}/{y}.png'
}


#==============================================================================
# Local App Configuration
#==============================================================================

