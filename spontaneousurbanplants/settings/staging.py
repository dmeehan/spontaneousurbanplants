from production import *

DEBUG=True

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'middleware.ExceptionLoggingMiddleware'
)


INSTALLED_APPS += (
	'debug_toolbar',  
)

INTERNAL_IPS = ('127.0.0.1',)

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

