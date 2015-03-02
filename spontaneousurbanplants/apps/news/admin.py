# news/admin.py

from django.contrib import admin

from .models import NewsItem, NewsItemImage

class NewsImageInline(admin.StackedInline):
    model = NewsItemImage
    fields = ('image', 'name', 'caption',
              'is_main', 'order' )
    extra = 0

    # Grappelli options
    allow_add = True
    sortable_field_name = "order"

class NewsItemAdmin(admin.ModelAdmin):
    inlines = [
       NewsImageInline,
    ]

    prepopulated_fields = {"slug": ("title",)}

class NewsItemImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'admin_thumbnail_view','news_item')


admin.site.register(NewsItem, NewsItemAdmin)
admin.site.register(NewsItemImage, NewsItemImageAdmin)
