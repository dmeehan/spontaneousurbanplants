# instagram/admin.py

from django.contrib import admin
from django.contrib import messages

from .models import InstagramImage, InstagramTag

def make_verified(modeladmin, request, queryset):
    queryset.update(verified=True)

make_verified.short_description = "Mark selected images as verified"

class TagInline(admin.TabularInline):
    model = InstagramTag

class InstagramImageAdmin(admin.ModelAdmin):
    list_display = ['thumbnail', 'remote_id', 'created', 'updated', 'last_synced', 'verified']
    list_editable = ['verified']
    inlines = [
        TagInline,
    ]

class InstagramTagAdmin(admin.ModelAdmin):
    list_display = ['name', 'sync', 'subscribe', 'moderate']

admin.site.register(InstagramImage, InstagramImageAdmin)
admin.site.register(InstagramTag, InstagramTagAdmin)