# plants/models.py
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from positions.fields import PositionField

from apps.instamedia.models import InstagramTag, InstagramImage


class Attribute(models.Model):
    """A descriptive aspect of a plant or plants.

    """
    name = models.CharField(max_length=255)
    hashtag = models.CharField(max_length=255, 
                               unique=True,
                               help_text='A unique hashtag indentifying this plant. Do not include #.')
    description = models.TextField(blank=True)
    icon = models.ImageField(upload_to="images/icons", 
                              blank=True, 
                              null=True)

    visible = models.BooleanField(default=True)
    order = PositionField()

    class Meta:
      ordering = ["order"]

    @staticmethod
    def autocomplete_search_fields():
        return ("name__icontains", "hashtag__icontains")

    def __unicode__(self):
        return u'%s' % (self.name)


class Plant(models.Model):
    """An individual plant species.

    """
    latin_name = models.CharField(max_length=255)
    common_name = models.CharField(max_length=255)
    hashtag = models.CharField(max_length=100, 
                               unique=True,
                               help_text='A unique hashtag indentifying this plant. Do not include #.')
    description = models.TextField(blank=True)
    icon = models.ImageField(upload_to="images/icons", 
                              blank=True, 
                              null=True)

    attributes = models.ManyToManyField(Attribute, blank=True, null=True)
    images = models.ManyToManyField(InstagramImage, blank=True, null=True)

    visible = models.BooleanField(default=True)
    order = PositionField()

    def __unicode__(self):
        return u'%s' % (self.latin_name)


@receiver(post_save, sender=Attribute)
def attribute_post_save(sender, instance, created, **kwargs):
    InstagramTag.objects.get_or_create(name=instance.hashtag)

@receiver(post_save, sender=Plant)
def plant_post_save(sender, instance, created, **kwargs):
    InstagramTag.objects.get_or_create(name=instance.hashtag)
