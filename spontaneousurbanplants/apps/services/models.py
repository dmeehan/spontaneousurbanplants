# services/models.py
from django.db import models

from positions.fields import PositionField

from apps.content.models import Content
from apps.plants.models import Attribute


class ServicesContent(Content):
	"""Content block for services text. """
	
	visible = models.BooleanField(default=True)

	class Meta:
		verbose_name = "services text"
		verbose_name_plural = "services text"

	def __unicode__(self):
		return u'%s' % (self.title)


class Service(models.Model):
	"""A model to display attributes

	"""
	image = models.ImageField(upload_to="images/services")

	attribute = models.ForeignKey(Attribute)
	order = PositionField()

	class Meta:
		ordering = ["order"]

	def __unicode__(self):
		return u'%s' % (self.attribute.name)

