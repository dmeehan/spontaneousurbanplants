# plants/admin.py

from django.contrib import admin

from .models import Attribute, Plant


class PlantAdmin(admin.ModelAdmin):
    list_display = ['latin_name', 'common_name', 'hashtag',]
    raw_id_fields = ('attributes',)
   
    autocomplete_lookup_fields = {
        'm2m': ['attributes'],
    }

admin.site.register(Attribute)
admin.site.register(Plant, PlantAdmin)