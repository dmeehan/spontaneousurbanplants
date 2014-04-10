# instagram/admin.py

from django.contrib import admin
from django.contrib import messages

from .models import InstagramImage, InstagramTag

class InstagramImageAdmin(admin.ModelAdmin):
    list_display = ['thumbnail', 'remote_id', 'created', 'updated', 'last_synced', 'verified']
    list_editable = ['verified']

class InstagramTagAdmin(admin.ModelAdmin):
    list_display = ['name', 'sync', 'subscribe', 'moderate']

admin.site.register(InstagramImage, InstagramImageAdmin)
admin.site.register(InstagramTag, InstagramTagAdmin)