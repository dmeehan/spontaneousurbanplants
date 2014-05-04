# instagram/models.py
import datetime
import inspect
import os
import requests

from django.conf import settings
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .client import get_api

api = get_api()

class InstagramImage(models.Model):
    """
    An instagram media object
    """
    remote_id = models.CharField(max_length=255, unique=True)
    caption = models.TextField(blank=True)
    raw_tags = models.TextField(blank=True)

    # media urls
    remote_thumbnail_url = models.URLField(blank=True)
    remote_low_resolution_url = models.URLField(blank=True)
    remote_standard_resolution_url = models.URLField(blank=True)

    # Location information
    location_name = models.CharField(max_length=255, blank=True)
    location_id = models.IntegerField(blank=True, null=True)

    # Geography information
    coordinates = models.PointField(null=True, blank=True)
    #latitude = models.DecimalField(max_digits=10, decimal_places=7, default=0, blank=True)
    #longitude = models.DecimalField(max_digits=10, decimal_places=7, default=0, blank=True)

    # Metadata
    created = models.DateTimeField()
    updated = models.DateTimeField()
    last_synced = models.DateTimeField()
    verified = models.BooleanField(default=False)

    # image cache
    image_file = models.ImageField(upload_to="images/instagram", 
                              blank=True, 
                              null=True)

    class Meta:
        ordering = ['-updated']

    def get_remote_data(self):
        try:
            media = api.media(self.remote_id)
            return media
        except:
            pass

    def download_remote_image(self):
        result = requests.get(self.remote_standard_resolution_url)
        img_temp = NamedTemporaryFile(delete=True)
        img_temp.write(result.content)
        img_temp.flush()

        self.image_file.save('%s.jpg' % self.remote_id, File(img_temp), save=True)

    def get_absolute_url(self):
        return reverse('instamedia_image_detail', args=[str(self.id)])

    def __unicode__(self):
        return u'Instagram Media: %s' % (self.remote_id)

    def thumbnail(self):
        return u'<img src="%s" />' % (self.remote_thumbnail_url)

    thumbnail.short_description = 'Image'
    thumbnail.allow_tags = True


class InstagramTag(models.Model):
    name = models.CharField(max_length=255)

    sync = models.BooleanField(default=True,
                               help_text='Sync existing instagram images with this tag to local database.')
    subscribe = models.BooleanField(default=True,
                                    help_text='Subscribe to realtime updates for this tag.')
    moderate = models.BooleanField(default=True,
                                   help_text='If true, new images will default to unverified.')
    subscription_id = models.IntegerField(blank=True, null=True)

    images = models.ManyToManyField(InstagramImage, blank=True, null=True)

    def get_remote_data(self):
        try:
            tag = api.tag(self.name)
            return tag
        except:
            pass
      
    def get_all_remote_images(self):
        try:
            data = api.tag_recent_media(tag_name=self.name, 
                                        count=100, max_pages=10000, 
                                        as_generator=True)  
            return data
        except:
            pass

    def get_recent_remote_images(self, count, max_id):
        try:
            data = api.tag_recent_media(count, max_id, self.name) 
            return data
        except:
            pass

    def sync_image(self, remote_image, moderate=False):
        try:
            obj = InstagramImage.objects.get(remote_id=remote_image.id)
            print('image %s already exists' % obj.remote_id)
            # TODO: check for updated fields and update
        except InstagramImage.DoesNotExist:
            obj = InstagramImage()
            obj.remote_id = remote_image.id
            obj.remote_standard_resolution_url = remote_image.get_standard_resolution_url()
            obj.remote_thumbnail_url = remote_image.images['thumbnail'].url
            obj.remote_low_resolution_url = remote_image.images['low_resolution'].url
            obj.created = remote_image.created_time
            obj.updated = datetime.datetime.now()
            obj.last_synced = datetime.datetime.now()

            if remote_image.caption:
                obj.caption = remote_image.caption.text

            if remote_image.tags:
                tag_list = []
                for tag in remote_image.tags:
                    tag_list.append(tag.name)
                    obj.raw_tags = " ".join(tag_list)

            if hasattr(remote_image, "location"):
                obj.location_name = remote_image.location.name
                obj.location_id = remote_image.location.id
                lat = remote_image.location.point.latitude
                lon = remote_image.location.point.longitude
                obj.coordinates = Point(lon, lat)

            if moderate:
                obj.verified = False
            else:
                obj.verified = True
                            
            obj.save()

            images = self.images.all()
            if obj not in images:
                self.images.add(obj)
                self.save()

            print('created new image %s' % obj.remote_id)


    def sync_remote_images(self, data):
        if inspect.isgenerator(data):
            for page in data:
                image_list = page[0]
                for image in image_list:
                    self.sync_image(image, moderate=self.moderate)
        else:
            for image in data:
                self.sync_image(image, moderate=self.moderate)

    
    def create_subscription(self):
        api.create_subscription(object='tag', 
                                object_id=self.name, 
                                aspect='media', 
                                callback_url=settings.INSTAGRAM_REALTIME_CALLBACK_URL)

    def delete_subscription(self):
        api.delete_subscriptions(id=self.subscription_id)


    def __unicode__(self):
        return u'%s' % (self.name)

    def save(self, *args, **kwargs):
        if not settings.DEBUG:
            if self.subscribe:
                if not self.subscription_id:
                    sub = api.create_subscription(object='tag', 
                                                  object_id=self.name, 
                                                  aspect='media', 
                                                  callback_url=settings.INSTAGRAM_REALTIME_CALLBACK_URL)
                    self.subscription_id = int(sub['data']['id'])
            else:
                if self.subscription_id:
                    api.delete_subscriptions(id=self.subscription_id)
                    self.subscription_id = None
            
        super(InstagramTag, self).save(*args, **kwargs)

        



@receiver(post_save, sender=InstagramTag)
def tag_post_save(sender, instance, created, **kwargs):
    if created and instance.sync:
        instance.sync_remote_images(instance.get_all_remote_images())


@receiver(post_delete, sender=InstagramTag)
def tag_post_delete(sender, instance, **kwargs):
    if instance.subscription_id:
        instance.delete_subscription()

@receiver(post_save, sender=InstagramImage)
def image_post_save(sender, instance, created, **kwargs):
    if not instance.image_file and instance.verified:
        instance.download_remote_image()


