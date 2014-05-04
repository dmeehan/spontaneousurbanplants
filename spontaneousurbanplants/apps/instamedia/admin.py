# instagram/admin.py

from django.contrib import admin
from django.contrib import messages

from .models import InstagramImage, InstagramTag

def make_verified(modeladmin, request, queryset):
    queryset.update(verified=True)

make_verified.short_description = "Mark selected images as verified"

class InstagramImageAdmin(admin.ModelAdmin):
    list_display = ['thumbnail', 'remote_id', 'created', 'updated', 'last_synced', 'verified']
    list_editable = ['verified']
    actions = [make_verified]

class InstagramTagAdmin(admin.ModelAdmin):
    list_display = ['name', 'sync', 'subscribe', 'moderate']

admin.site.register(InstagramImage, InstagramImageAdmin)
admin.site.register(InstagramTag, InstagramTagAdmin)