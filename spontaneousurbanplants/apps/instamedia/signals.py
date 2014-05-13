# instagram/signals.py

import django.dispatch

image_added = django.dispatch.Signal(providing_args=[])
image_updated = django.dispatch.Signal(providing_args=[])

