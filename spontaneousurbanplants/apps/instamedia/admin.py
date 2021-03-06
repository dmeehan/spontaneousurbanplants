# instagram/admin.py

from django.contrib import admin
from django.contrib import messages

from leaflet.admin import LeafletGeoAdmin

from .models import InstagramImage, InstagramTag

def make_verified(modeladmin, request, queryset):
    queryset.update(verified=True)

make_verified.short_description = "Mark selected images as verified"

class InstagramImageAdmin(LeafletGeoAdmin):
    fields = ['remote_id', 'tags', 'username', 'image_file', 'verified', 'created', 'coordinates']
    list_display = ['thumbnail', 'verified', 'username', 
                    'caption', 'raw_tags', 'display_tags', 
                    'created', 'updated', 'last_synced',]
    list_editable = ['verified',]
    raw_id_fields = ('tags',)

    list_filter = ('tags__name', 'verified')

    autocomplete_lookup_fields = {
        'm2m': ['tags'],
    }

class InstagramTagAdmin(admin.ModelAdmin):
    list_display = ['name', 'sync', 'subscribe', 'moderate', 'image_count']

admin.site.register(InstagramImage, InstagramImageAdmin)
admin.site.register(InstagramTag, InstagramTagAdmin)
