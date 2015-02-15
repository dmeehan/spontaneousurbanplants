# content/models.py
import markdown

from django.db import models

class Content(models.Model):
	"""Abstract content block"""
	title = models.CharField(max_length=255)
	text = models.TextField(blank=True)

	# Fields to store generated HTML. 
	text_html = models.TextField(editable=False, blank=True)
	
	class Meta:
		abstract = True

	def render_markup(self):
		"""Turns markup into HTML"""
		self.text_html = markdown.markdown(self.text)
	
	def save(self, force_insert=False, force_update=False):
		self.render_markup()
		super(Content, self).save(force_insert, force_update)

	def __unicode__(self):
		return u'%s' % (self.title)