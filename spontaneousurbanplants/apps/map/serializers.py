# map/serializers.py
from datetime import datetime

from django.utils import formats

from rest_framework import serializers
from rest_framework_gis import serializers as gis_serializers

from apps.instamedia.models import InstagramImage
from apps.plants.models import Plant


class ImageSerializer(gis_serializers.GeoFeatureModelSerializer):
	
	tags = serializers.SlugRelatedField(many=True, read_only=True,
                                        slug_field='name')
	plant = serializers.SerializerMethodField('get_plant')
	plant_url = serializers.SerializerMethodField('get_plant_url')
	common_name = serializers.SerializerMethodField('get_plant_common_name')
	latin_name = serializers.SerializerMethodField('get_plant_latin_name')
	date = serializers.SerializerMethodField('format_date')
	image_url = serializers.Field(source='image_url')

	class Meta:
		model = InstagramImage
		geo_field = 'coordinates'
		id_field = None
		fields = ('id', 'caption', 'image_url', 'plant_url', 'date', 'latin_name', 'common_name')

	def get_plant(self, obj):
		for tag in obj.tags.all():
			try:
				return Plant.objects.get(hashtag__iexact=tag.name)
			except Plant.DoesNotExist:
				return ""

	def get_plant_common_name(self, obj):
		for tag in obj.tags.all():
			try:
				return Plant.objects.filter(hashtag__iexact=tag.name).values_list('common_name', flat=True).distinct()
			except DoesNotExist:
				return ""

	def get_plant_latin_name(self, obj):
		for tag in obj.tags.all():
			try:
				return Plant.objects.filter(hashtag__iexact=tag.name).values_list('latin_name', flat=True).distinct()
			except DoesNotExist:
				return ""

	def get_plant_url(self, obj):
		for tag in obj.tags.all():
			try:
				plant = Plant.objects.get(visible=True, hashtag__iexact=tag.name)
				return plant.get_absolute_url
			except Plant.DoesNotExist:
				return ""

	def format_date(self, obj):
		try:
			return formats.date_format(obj.created, "DATETIME_FORMAT")
		except:
			return ""