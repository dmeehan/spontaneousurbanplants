from production import *

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'middleware.py'
)


INSTALLED_APPS += (
	'debug_toolbar',  
)

INTERNAL_IPS = ('127.0.0.1',)

