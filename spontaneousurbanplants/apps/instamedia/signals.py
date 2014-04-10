# instagram/signals.py

import django.dispatch

image_added = django.dispatch.Signal(providing_args=["image", "request"])
image_updated = django.dispatch.Signal(providing_args=["image", "request"])

ready_to_sync = django.dispatch.Signal(providing_args=["tag", "request"])