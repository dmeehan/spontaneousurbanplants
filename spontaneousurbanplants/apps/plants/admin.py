# plants/admin.py

from django.contrib import admin

from .models import Attribute, Plant


class PlantAdmin(admin.ModelAdmin):
    list_display = ['latin_name', 'common_name', 'hashtag',]
    raw_id_fields = ('attributes',)
   
    autocomplete_lookup_fields = {
        'm2m': ['attributes'],
    }

class AttributeAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'description',]
    list_editable = ['order', ]
    

admin.site.register(Attribute, AttributeAdmin)
admin.site.register(Plant, PlantAdmin)