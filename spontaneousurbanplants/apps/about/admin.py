# about/admin.py

from django.contrib import admin

from .models import AboutContent, SourcesContent, CreditsContent

class AboutContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'visible',]
    list_editable = ['order', 'visible', ]

admin.site.register(AboutContent, AboutContentAdmin)
admin.site.register(SourcesContent)
admin.site.register(CreditsContent)
