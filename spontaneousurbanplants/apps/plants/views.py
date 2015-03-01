# plants/views.py

from django.views.generic import ListView, DetailView

from .models import Plant

class PlantDetailView(DetailView):
    model = Plant

	

