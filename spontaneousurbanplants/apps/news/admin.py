# news/admin.py
from django.contrib import admin

from grappelli.forms import GrappelliSortableHiddenMixin

from .models import NewsItem, NewsItemImage

class NewsImageInline(GrappelliSortableHiddenMixin, admin.StackedInline):
    model = NewsItemImage
    extra = 0

    # Grappelli options
    allow_add = True
    sortable_field_name = "order"

class NewsItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'featured']
    list_editable = ['status', 'featured' ]

    inlines = [
       NewsImageInline,
    ]

    prepopulated_fields = {"slug": ("title",)}

class NewsItemImageAdmin(admin.ModelAdmin):
    list_display = ('image_file', 'news_item')


admin.site.register(NewsItem, NewsItemAdmin)
admin.site.register(NewsItemImage, NewsItemImageAdmin)
