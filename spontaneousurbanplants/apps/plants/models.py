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
                               help_text='A unique hashtag indentifying this attribute. Do not include #.')
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
        

class Category(models.Model):
    """ Categories to group plants.

    """
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    icon = models.ImageField(upload_to="images/icons", 
                              blank=True, 
                              null=True)

    visible = models.BooleanField(default=True)
    order = PositionField()

    class Meta:
      ordering = ["order"]
      verbose_name_plural = 'categories'

    @staticmethod
    def autocomplete_search_fields():
        return ("name__icontains",)

    def __unicode__(self):
        return u'%s' % (self.name)

class Plant(models.Model):
    """An individual plant species.
    
    """
    icon = models.ImageField(upload_to="images/icons", 
                              blank=True, 
                              null=True)
    latin_name = models.CharField(max_length=255)
    common_name = models.CharField(max_length=255)
    hashtag = models.CharField(max_length=100, 
                               unique=True,
                               help_text='A unique hashtag indentifying this plant. Do not include #.')
    description = models.TextField(blank=True)
    #flowers = models.TextField(blank=True)
    #habitat = models.TextField(blank=True)
    #origin = models.CharField(max_length=255)
    #stormwater = models.FloatField(help_text="Stormwater retention in gallons")
    #carbon = models.FloatField(help_text="CO2 sequestration in pounds")
    #energy = models.FloatField(help_text="Energy savings in kWh")

    attributes = models.ManyToManyField(Attribute, blank=True, null=True)
    categories = models.ManyToManyField(Category, blank=True, null=True)
    images = models.ManyToManyField(InstagramImage, blank=True, null=True)

    visible = models.BooleanField(default=True)
    order = PositionField()

    class Meta:
      ordering = ["order", "latin_name"]

    def __unicode__(self):
        return u'%s' % (self.latin_name)


'''class AttributeDescription(models.Model):
  """Specific information about a species' performance

  """
  attribute = models.ForignKey(Attribute)
  plant = models.ForignKey(Plant)
  description = models.TextField(blank=True)

  visible = models.BooleanField(default=True)

class TimeSpan(models.Model):
  """Abstract model for monthly span of time

  """
  begin = 
  end =

  class Meta:
    abstract = True

class Bloom(TimeSpan):
  color = 

class Leaf(TimeSpan):
  color = 

class Dispersal(TimeSpan):
  pass 
'''

'''@receiver(post_save, sender=Attribute)
def attribute_post_save(sender, instance, created, **kwargs):
    InstagramTag.objects.get_or_create(name=instance.hashtag)

@receiver(post_save, sender=Plant)
def plant_post_save(sender, instance, created, **kwargs):
    InstagramTag.objects.get_or_create(name=instance.hashtag)
'''
