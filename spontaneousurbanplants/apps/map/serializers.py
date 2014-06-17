# map/serializers.py

from rest_framework import serializers
from rest_framework_gis import serializers as gis_serializers

from apps.instamedia.models import InstagramImage
from apps.plants.models import Plant


class ImageSerializer(gis_serializers.GeoFeatureModelSerializer):
	tags = serializers.SlugRelatedField(many=True, read_only=True,
                                        slug_field='name')

	#tags = serializers.RelatedField(many=True, read_only=True)

	plant = serializers.SerializerMethodField('get_plant')

	class Meta:
		model = InstagramImage
		geo_field = 'coordinates'
		#fields = ('tags', 'plant', 'caption', 'remote_thumbnail_url', 'remote_standard_resolution_url')
		fields = ('tags', 'caption', 'remote_thumbnail_url', 'remote_standard_resolution_url')
		#fields = ('caption', 'remote_thumbnail_url', 'remote_standard_resolution_url')

	def get_plant(self, obj):
		for tag in obj.tags.all():
			try:
				return Plant.objects.get(hashtag__iexact=tag.name)
			except Plant.DoesNotExist:
				return ""