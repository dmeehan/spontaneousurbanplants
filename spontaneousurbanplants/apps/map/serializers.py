# map/serializers.py

from rest_framework import serializers
from rest_framework_gis import serializers as gis_serializers

from apps.instamedia.models import InstagramImage
from apps.plants.models import Plant


class ImageSerializer(gis_serializers.GeoFeatureModelSerializer):
	
	tags = serializers.SlugRelatedField(many=True, read_only=True,
                                        slug_field='name')
	plant = serializers.SerializerMethodField('get_plant')
	image_url = serializers.Field(source='image_url')

	class Meta:
		model = InstagramImage
		geo_field = 'coordinates'
		id_field = None
		fields = ('id', 'caption', 'image_url')

	def get_plant(self, obj):
		for tag in obj.tags.all():
			try:
				return Plant.objects.get(hashtag__iexact=tag.name)
			except Plant.DoesNotExist:
				return ""