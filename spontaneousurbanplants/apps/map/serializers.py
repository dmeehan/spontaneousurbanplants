# map/serializers.py
from datetime import datetime

from django.utils.formats import date_format
from django.utils import timezone

from rest_framework import serializers
from rest_framework_gis import serializers as gis_serializers

from apps.instamedia.models import InstagramImage
from apps.plants.models import Plant


class ImageSerializer(gis_serializers.GeoFeatureModelSerializer):
	
	tags = serializers.SlugRelatedField(many=True, read_only=True,
                                        slug_field='name')
	plant = serializers.SerializerMethodField('get_plant')
	date = serializers.SerializerMethodField('format_date')
	image_url = serializers.SerializerMethodField('get_image_url')

	class Meta:
		model = InstagramImage
		geo_field = 'coordinates'
		id_field = None
		fields = ('id', 'caption', 'plant', 'date', 'image_url')

	def get_plant(self, obj):
		for tag in obj.tags.all():
			try:
				plant = Plant.objects.filter(hashtag__iexact=tag.name).values()
				if plant:
					return plant[0]
			except Plant.DoesNotExist:
				return ""

	def format_date(self, obj):
		try:
			return date_format(timezone.localtime(obj.created), 'DATETIME_FORMAT')
		except:
			return ""

	def get_image_url(self, obj):
		try:
			return obj.image_file.url
		except:
			return obj.remote_standard_resolution_url