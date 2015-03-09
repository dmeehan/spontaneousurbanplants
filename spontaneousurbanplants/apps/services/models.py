# services/models.py
import markdown

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
	image = models.ImageField(upload_to="images/services", blank=True, null=True)
	text = models.TextField(blank=True)

	# Fields to store generated HTML. 
	text_html = models.TextField(editable=False, blank=True)

	attribute = models.ForeignKey(Attribute)
	order = PositionField()

	class Meta:
		ordering = ["order"]

	def render_markup(self):
		"""Turns markup into HTML"""
		self.text_html = markdown.markdown(self.text)
	
	def save(self, force_insert=False, force_update=False):
		self.render_markup()
		super(Service, self).save(force_insert, force_update)

	def __unicode__(self):
		return u'%s' % (self.attribute.name)

