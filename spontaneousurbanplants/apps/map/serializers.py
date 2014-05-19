# map/serializers.py

from rest_framework import serializers
from rest_framework_gis import serializers as gis_serializers

from apps.instamedia.models import InstagramImage

class ImageSerializer(gis_serializers.GeoFeatureModelSerializer):
	tags = serializers.SlugRelatedField(many=True, read_only=True,
                                        slug_field='name')
	class Meta:
		model = InstagramImage
		geo_field = 'coordinates'

