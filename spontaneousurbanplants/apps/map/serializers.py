# map/serializers.py

from rest_framework_gis import serializers as gis_serializers

from apps.instamedia.models import InstagramImage

class ImageSerializer(gis_serializers.GeoFeatureModelSerializer):
	class Meta:
		model = InstagramImage
		geo_field = 'coordinates'

		fields = ()