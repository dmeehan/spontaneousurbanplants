# about/admin.py

from django.contrib import admin

from .models import About, Sources, Credits

class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'visible',]
    list_editable = ['order', 'visible', ]

admin.site.register(About, AboutAdmin)
admin.site.register(Sources)
admin.site.register(Credits)
