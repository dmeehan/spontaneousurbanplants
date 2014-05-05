# map/views.py
from django.views.generic import TemplateView

from rest_framework import viewsets

from apps.plants.models import Plant, Attribute
from apps.instamedia.models import InstagramImage

from .serializers import ImageSerializer

class MapView(TemplateView):
	
	template_name = "map/map.html"

	def get_context_data(self, **kwargs):
		context = super(MapView, self).get_context_data(**kwargs)
		plants = Plant.objects.all()
		attributes = Attribute.objects.all()
		context.update({
			'plant_list': plants,
			'attribute_list': attributes
		})

		return context
	
class ImageApiViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Images to be consumed as geojson
    """

    queryset = InstagramImage.objects.filter(verified=True)

    serializer_class = ImageSerializer
    paginate_by = None