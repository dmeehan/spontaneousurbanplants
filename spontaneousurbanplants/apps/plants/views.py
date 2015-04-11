# plants/views.py

from django.views.generic import ListView, DetailView

from .models import Plant

class PlantListView(ListView):
    model = Plant

class PlantDetailView(DetailView):
    model = Plant
    slug_field = 'hashtag'

	

