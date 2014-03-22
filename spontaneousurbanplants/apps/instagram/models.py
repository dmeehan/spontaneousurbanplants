# instagram/models.py

from django.db import models

from instagram.client import InstagramAPI


class Hashtag(models.Model):
	"""
	An instagram Hashtag
	"""

	name = models.Charfield(max_length=100)
	sync = models.BooleanField(default=True)
	subscribe = models.BooleanField(default=True)

	active = models.BooleanField(default=True)

	def create_subscription():
		"""
		curl -F 'client_id=CLIENT-ID' \
     		 -F 'client_secret=CLIENT-SECRET' \
     		 -F 'object=tag' \
     		 -F 'aspect=media' \
             -F 'object_id=TAGNAME' \
             -F 'callback_url=http://YOUR-CALLBACK/URL' \
             https://api.instagram.com/v1/subscriptions/
     	"""
     	pass

     def sync_media(self):
     	#https://api.instagram.com/v1/tags/<tagname>/media/recent
     	pass
	


class Subscription(models.Model):
	"""
	A real time api subscription
	"""
	object_type = 
	aspect =

	active = models.BooleanField(default=True)

	def create_subscription():
		"""
		curl -F 'client_id=CLIENT-ID' \
     		 -F 'client_secret=CLIENT-SECRET' \
     		 -F 'object=tag' \
     		 -F 'aspect=media' \
             -F 'object_id=nofilter' \
             -F 'callback_url=http://YOUR-CALLBACK/URL' \
             https://api.instagram.com/v1/subscriptions/
     	"""

class TagSubscription(models.Model):


class LocationSubscription(models.Model):

class UserSubscription(models.Model):


#### code from mezzanine instagram gallery for reference


class InstagramMedia(models.Model):
    instagram_id = models.CharField(max_length=128, unique=True)
    created = models.DateTimeField(blank=True)
    caption = models.CharField(max_length=256, blank=True)
    comment_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    url = models.URLField(blank=True)
    thumbnail_url = models.URLField()
    standard_url = models.URLField()

    downloaded = models.BooleanField(default=False)

    destination = 'uploads/instagram'

    class Meta:
        verbose_name = _(u'Instagram Media')
        verbose_name_plural = _(u'Instagram Medias')
        ordering = ('-created',)
        get_latest_by = 'created'

    def __unicode__(self):
        return u'InstagramMedia: %s - %s' % (self.instagram_id, self.caption)

    def _download_to(self, url, destination=''):
        if not destination:
            destination = self.destination
        filename = os.path.basename(url).decode('utf-8')

        downloaded_file = requests.get(url)
        if downloaded_file.ok:
            path = os.path.join(destination, filename)
            return default_storage.save(path,
                                        ContentFile(downloaded_file.content))

    #
    # Public API
    #

    def download_media(self, destination=''):
        assert self.standard_url
        return self._download_to(self.standard_url, destination)

    def download_media_thumbnail(self, destination=''):
        assert self.thumbnail_url
        return self._download_to(self.thumbnail_url, destination)

    def to_mezzanine(self, gallery, thumbnail=False):
        if thumbnail is False:
            downloaded_file = self.download_media()
        else:
            downloaded_file = self.download_media_thumbnail()
        if downloaded_file:
            self.downloaded = True
            self.save()

            return GalleryImage(gallery=gallery, description=self.caption,
                                file=downloaded_file)

    @classmethod
    def fetch_medias(cls, count):
        try:
            last_media = cls.objects.latest()
        except InstagramMedia.DoesNotExist:
            last_media = None

        min_time = ''
        if last_media:
            min_time = time.mktime(last_media.created.utctimetuple())

        user = InstagramUser.objects.all()[0]
        api = InstagramAPI(access_token=user.access_token)
        medias = api.user_recent_media(min_timestamp=min_time, count=count)
        if not (medias and medias[0]):
            raise StopIteration

        for media in medias[0]:
            if cls.objects.filter(instagram_id=media.id).exists():
                # TODO: check and update metadata
                continue

            caption = media.caption and media.caption.text or u''
            insta_media = cls(instagram_id=media.id,
                              created=media.created_time,
                              caption=caption,
                              comment_count=media.comment_count,
                              like_count=media.like_count,
                              url=media.link or u'',
                              thumbnail_url=media.images['thumbnail'].url,
                              standard_url=media.get_standard_resolution_url())
            yield insta_media
