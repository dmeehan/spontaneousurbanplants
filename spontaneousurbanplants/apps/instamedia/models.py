# instagram/models.py
import inspect
import os
import requests

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils import timezone

from notification import models as notification
from easy_thumbnails.files import get_thumbnailer

from .client import get_api
from .signals import image_added

api = get_api()

class InstagramImage(models.Model):
    """
    An instagram media object
    """
    remote_id = models.CharField(max_length=255, unique=True)
    caption = models.TextField(blank=True)
    raw_tags = models.TextField("remote tags", blank=True)
    username = models.CharField(max_length=255, blank=True, null=True)

    tags = models.ManyToManyField('InstagramTag', blank=True, null=True)

    # media urls
    remote_thumbnail_url = models.URLField(blank=True)
    remote_low_resolution_url = models.URLField(blank=True)
    remote_standard_resolution_url = models.URLField(blank=True)

    # Location information
    location_name = models.CharField(max_length=255, blank=True)
    location_id = models.IntegerField(blank=True, null=True)

    # Geography information
    coordinates = models.PointField(null=True, blank=True)

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
        if result.status_code == 200:
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(result.content)
            img_temp.flush()

            self.image_file.save('%s.jpg' % self.remote_id, File(img_temp), save=True)

    def get_absolute_url(self):
        return reverse('instamedia_image_detail', args=[str(self.id)])

    def __unicode__(self):
        return u'Instagram Media: %s' % (self.remote_id)

    @property
    def image_url(self):
        if self.image_file:
            return self.image_file.url
        else:
            return self.remote_standard_resolution_url

    def thumbnail(self):
        try:
            options = {'size': (150, 150), 'crop': True}
            thumbnail_url = get_thumbnailer(self.image_file).get_thumbnail(options).url
            return u'<img src="%s" />' % (thumbnail_url)
        except:
            return u'<img src="%s" />' % (self.remote_thumbnail_url)

    def display_tags(self):
        return ', '.join([ tag.name for tag in self.tags.all() ])
    

    display_tags.short_description = 'local tags'
    display_tags.allow_tags = True

    thumbnail.short_description = 'Image'
    thumbnail.allow_tags = True


class InstagramTag(models.Model):
    name = models.CharField(max_length=255)

    sync = models.BooleanField(default=True,
                               help_text='Sync existing instagram images with this tag to local database.')
    subscribe = models.BooleanField(default=False,
                                    help_text='Subscribe to realtime updates for this tag.')
    moderate = models.BooleanField(default=True,
                                   help_text='If true, new images will default to unverified.')
    subscription_id = models.IntegerField(blank=True, null=True)


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

    def get_recent_remote_images(self, count=10, max_pages=1):
        try:
            data = api.tag_recent_media(tag_name=self.name, 
                                        count=count, max_pages=max_pages, 
                                        as_generator=True) 
            return data
        except:
            pass

    def sync_image(self, remote_image, moderate=False):
        try:
            obj = InstagramImage.objects.get(remote_id=remote_image.id)
            current_tags = obj.tags.all()
            if remote_image.tags:
                new_tag_list = []
                for remote_tag in remote_image.tags:
                    new_tag_list.append(remote_tag.name)
                    try:
                        local_tag = InstagramTag.objects.get(name__iexact=remote_tag.name)
                        if local_tag not in current_tags:
                            obj.tags.add(local_tag)
                    except:
                        pass
                new_raw_tags =  " ".join(new_tag_list)
                if new_raw_tags != obj.raw_tags:
                    obj.raw_tags = new_raw_tags
                    obj.updated = timezone.now()
            if obj.caption:
                if obj.caption != remote_image.caption.text:
                    obj.caption = remote_image.caption.text
                    obj.updated = timezone.now()
            if not obj.username:
                obj.username = remote_image.user.username
                obj.last_synced = timezone.now()
            obj.save()
            print('updated image %s' % remote_image.user.username)
        except InstagramImage.DoesNotExist:
            obj = InstagramImage()
            obj.remote_id = remote_image.id
            obj.username = remote_image.user.username
            obj.remote_standard_resolution_url = remote_image.get_standard_resolution_url()
            obj.remote_thumbnail_url = remote_image.images['thumbnail'].url
            obj.remote_low_resolution_url = remote_image.images['low_resolution'].url
            obj.created = remote_image.created_time
            obj.updated = timezone.now()
            obj.last_synced = timezone.now()
            obj.username = remote_image.user.username

            if remote_image.caption:
                obj.caption = remote_image.caption.text

            if remote_image.tags:
                tag_list = []
                for tag in remote_image.tags:
                    tag_list.append(tag.name)
                    try:
                        local_tag = InstagramTag.objects.get(name__iexact=remote_tag.name)
                        obj.tags.add(local_tag)
                    except:
                        pass

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

            tags = obj.tags.all()
            if self not in tags:
                obj.tags.add(self)
                obj.save()

            notify_list = User.objects.filter(is_superuser=True)
            notification.send(notify_list, 
                      "image_submitted", 
                      { "tag": self , "image": obj })

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

    def image_count(self):
        return self.instagramimage_set.count()

    image_count.short_description = 'image count'
    image_count.allow_tags = True


    @staticmethod
    def autocomplete_search_fields():
        return ("name__icontains",)


    def __unicode__(self):
        return u'%s' % (self.name)


@receiver(post_save, sender=InstagramTag)
def tag_post_save(sender, instance, created, **kwargs):
    if instance.sync:
        instance.sync_remote_images(instance.get_all_remote_images())
    if instance.subscribe:
        if not instance.subscription_id:
            sub = api.create_subscription(object='tag', 
                                          object_id=instance.name, 
                                          aspect='media', 
                                          callback_url=settings.INSTAGRAM_REALTIME_CALLBACK_URL)
            instance.subscription_id = int(sub['data']['id'])
            instance.save()
    else:
        if instance.subscription_id:
            api.delete_subscriptions(id=instance.subscription_id)
            instance.subscription_id = None
            instance.save()


@receiver(post_delete, sender=InstagramTag)
def tag_post_delete(sender, instance, **kwargs):
    if instance.subscription_id:
        instance.delete_subscription()

@receiver(post_save, sender=InstagramImage)
def image_post_save(sender, instance, created, **kwargs):
    if not instance.image_file and instance.verified:
        instance.download_remote_image()

@receiver(image_added, sender=InstagramTag)
def image_submitted_action(sender, instance, **kwargs):
    notify_list = User.objects.filter(is_superuser=True)
    notification.send(notify_list, 
                      "image_submitted", 
                      { "image": instance })
