# news/admin.py

from django.contrib import admin

from .models import NewsItem, NewsItemImage

class NewsImageInline(admin.StackedInline):
    model = NewsItemImage
    extra = 1

    # Grappelli options
    allow_add = True
    sortable_field_name = "order"

class NewsItemAdmin(admin.ModelAdmin):
    inlines = [
       NewsImageInline,
    ]

    prepopulated_fields = {"slug": ("title",)}

class NewsItemImageAdmin(admin.ModelAdmin):
    list_display = ('image_file', 'news_item')


admin.site.register(NewsItem, NewsItemAdmin)
admin.site.register(NewsItemImage, NewsItemImageAdmin)
