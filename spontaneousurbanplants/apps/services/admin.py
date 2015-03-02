# services/admin.py
from django.contrib import admin

from .models import ServicesContent, Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['attribute', 'order',]
    list_editable = ['order',]

admin.site.register(Service, ServiceAdmin)
admin.site.register(ServicesContent)
