# instagram/admin.py

from django.contrib import admin

from .models import InstagramMedia, InstagramTag

admin.site.register(InstagramMedia)
admin.site.register(InstagramTag)