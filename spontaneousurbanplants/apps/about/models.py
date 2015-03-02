# about/models.py
import markdown

from django.db import models

from positions.fields import PositionField

from apps.content.models import Content


class AboutContent(Content):
	"""Content block for about section. Includes image."""
	image = models.ImageField(upload_to='images/about', blank=True)
	
	order = PositionField()
	visible = models.BooleanField(default=True)

	class Meta:
		ordering = ["order"]
		verbose_name = "about text"
		verbose_name_plural = "about text"

	def __unicode__(self):
		return u'%s' % (self.title)

class SourcesContent(Content):
	"""Content block for data sources."""
	class Meta:
		verbose_name = "sources text"
		verbose_name_plural = "sources text"

class CreditsContent(Content):
	"""Content block for site credits."""
	class Meta:
		verbose_name = "credits text"
		verbose_name_plural = "credits text"