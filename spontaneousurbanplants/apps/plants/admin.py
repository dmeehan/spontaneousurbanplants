# plants/admin.py

from django.contrib import admin

from .models import Attribute, Plant


class PlantAdmin(admin.ModelAdmin):
    list_display = ['latin_name', 'order', 'visible', 'common_name', 'hashtag',]
    list_editable = ['order', 'visible' ]
    raw_id_fields = ('attributes',)
   
    autocomplete_lookup_fields = {
        'm2m': ['attributes'],
    }

class AttributeAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'visible', 'description',]
    list_editable = ['order', 'visible' ]
    

admin.site.register(Attribute, AttributeAdmin)
admin.site.register(Plant, PlantAdmin)