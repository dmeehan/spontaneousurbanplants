# plants/admin.py

from django.contrib import admin

from .models import Attribute, Plant

admin.site.register(Attribute)
admin.site.register(Plant)