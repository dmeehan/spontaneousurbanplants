# instagram/models.py

from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.db import models

from instagram.bind import InstagramAPIError
from instagram.client import InstagramAPI


INSTAGRAM_CLIENT_ID = getattr(settings, 'INSTAGRAM_CLIENT_ID', None)
INSTAGRAM_CLIENT_SECRET = getattr(settings, 'INSTAGRAM_CLIENT_SECRET', None)

api = InstagramAPI(client_id=INSTAGRAM_CLIENT_ID, client_secret=INSTAGRAM_CLIENT_SECRET)


class InstagramMedia(models.Model):
	"""
	An instagram media object
	"""
	instagram_id = models.CharField(max_length=256, unique=True)
	standard_resolution_url = models.URLField()

	def __unicode__(self):
		return u'Instagram Media: %s' % (self.instagram_id)

class InstagramTag(models.Model):
	"""
	An instagram Hashtag
	"""

	name = models.CharField(max_length=100)
	sync = models.BooleanField(default=True,
                             help_text='Sync all media with this tag to local database.')
	subscribe = models.BooleanField(default=True,
                                  help_text='Subscribe to realtime updates for this tag.')
	moderate = models.BooleanField(default=True,
                                 help_text='If true, new media will default to hidden.')

	def get_media(self):
		gen = api.tag_recent_media(tag_name=self.name, count=100, max_pages=10000, as_generator=True)
		for page in gen:
		    media_list = page[0]
		    for media in media_list:
		    	try:
		    		obj = InstagramMedia.objects.get(instagram_id=media.id)
		    	except InstagramMedia.DoesNotExist:
		    		obj = InstagramMedia(instagram_id=media.id, 
		    			standard_resolution_url=media.get_standard_resolution_url())
		    		obj.save()

	def save(self, *args, **kwargs):
		if not self.pk:
			if self.sync:
				self.get_media()
		super(InstagramTag, self).save(*args, **kwargs)
    			

	def __unicode__(self):
		return u'%s' % (self.name)

	



