# map/views.py
from django.contrib.gis.geos import Polygon
from django.views.generic import TemplateView

from rest_framework import viewsets

from apps.plants.models import Plant, Attribute, Category
from apps.instamedia.models import InstagramImage

from .serializers import ImageSerializer

########## Mixins ##########

class BBoxMixin(object):
    def get_queryset(self):
        queryset = super(BBoxMixin, self).get_queryset()
        bbox = self.request.QUERY_PARAMS.get('bbox', None)
        if bbox:
            try:
                p1x, p1y, p2x, p2y = (float(n) for n in bbox.split(','))
            except ValueError:
                raise APIException("Not valid bbox string in parameter %s."
                               % bbox)

            poly = Polygon.from_bbox((p1x, p1y, p2x, p2y))
            queryset = queryset.filter(coordinates__contained=poly)
        return queryset

class MapView(TemplateView):
    
    template_name = "map/map.html"

    def get_context_data(self, **kwargs):
        context = super(MapView, self).get_context_data(**kwargs)
        image_id = self.request.GET.get('image_id', None)
        plants = Plant.objects.filter(visible=True)
        attributes = Attribute.objects.filter(visible=True)
        categories = Category.objects.filter(visible=True)
        context.update({
            'plant_list': plants,
            'attribute_list': attributes,
            'category_list': categories
        })

        if image_id:
            context.update({'image_id': image_id,})

        return context
    
class ImageApiViewSet(BBoxMixin, viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows Images to be consumed as geojson
    """

    def get_queryset(self):
        queryset = InstagramImage.objects.all()
        tag = self.request.QUERY_PARAMS.get('tag', None)
        if tag:
            queryset = queryset.filter(tags__name__iexact=tag)
        return queryset
    
    serializer_class = ImageSerializer
    paginate_by = None
