# plants/views.py

from django.views.generic import ListView, DetailView

from .models import Plant

class PlantListView(ListView):
    queryset = Plant.objects.filter(visible=True).order_by('latin_name')

class PlantDetailView(DetailView):
    queryset = Plant.objects.filter(visible=True)
    slug_field = 'hashtag'

	

