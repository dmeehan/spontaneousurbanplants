# plants/admin.py

from django.contrib import admin

from apps.instamedia.models import InstagramImage

from .models import Attribute, Category, Plant, AttributeDescription

class AttributeDescriptionInline(admin.TabularInline):
    model = AttributeDescription


class PlantAdmin(admin.ModelAdmin):

    list_display = ['latin_name', 'order', 'thumbnail', 'image_count', 'common_name', 'hashtag', 'visible', 'featured']
    list_editable = ['order', 'visible', 'featured' ]
    raw_id_fields = ('attributes', 'categories', 'lead_image')
   
    autocomplete_lookup_fields = {
        'm2m': ['attributes', 'categories'], 
    }

    inlines = [
        AttributeDescriptionInline,
    ]

class AttributeAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'visible', 'description',]
    list_editable = ['order', 'visible' ]
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'visible', 'description',]
    list_editable = ['order', 'visible' ]

admin.site.register(Attribute, AttributeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Plant, PlantAdmin)