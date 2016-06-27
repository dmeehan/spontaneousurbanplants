# plants/models.py
from django.core.urlresolvers import reverse
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
      verbose_name_plural = "categories"

    @staticmethod
    def autocomplete_search_fields():
        return ("name__icontains",)

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
    lead_image = models.ForeignKey(InstagramImage, blank=True, null=True)
    description = models.TextField(blank=True)
    flowers = models.TextField(blank=True)
    habitat = models.TextField(blank=True)
    origin = models.CharField(blank=True, max_length=255)
    seasonality_chart = models.ImageField(upload_to="images/plants", 
                              blank=True, 
                              null=True)
    stormwater = models.FloatField(blank=True, null=True, 
      help_text="Stormwater retention per plant in gallons")
    carbon = models.FloatField(blank=True, null=True, 
      help_text="CO2 sequestration per plant in pounds")
    energy = models.FloatField(blank=True, null=True, 
      help_text="Energy savings per plant in kWh")

    attributes = models.ManyToManyField(Attribute, blank=True, null=True)
    categories = models.ManyToManyField(Category, blank=True, null=True)

    icon = models.ImageField(upload_to="images/icons", 
                              blank=True, 
                              null=True)

    featured = models.BooleanField(default=False)
    featured_image = models.ImageField(upload_to="images/plants")
    visible = models.BooleanField(default=True)
    order = PositionField()

    class Meta:
      ordering = ["order", "latin_name"]

    def thumbnail(self):
        if self.lead_image:
          return u'<img src="%s" />' % (self.lead_image.remote_thumbnail_url)
        else:
          return u''

    def get_images(self):
      return InstagramImage.objects.filter(tags__name__iexact=self.hashtag).filter(verified=True)

    def get_absolute_url(self):
        return reverse('plant_detail', args=[str(self.hashtag)])

    def image_count(self):
      return self.get_images().count()

    def get_stormwater_total(self):
        if self.stormwater:
          return self.image_count() * self.stormwater
        else:
          return 0

    def __unicode__(self):
        return u'%s' % (self.latin_name)

    image_count.short_description = 'image count'
    thumbnail.short_description = 'lead image'
    thumbnail.allow_tags = True


class AttributeDescription(models.Model):
  """Specific information about a species' performance

  """
  attribute = models.ForeignKey(Attribute)
  plant = models.ForeignKey(Plant)
  description = models.TextField(blank=True)

  visible = models.BooleanField(default=True)



@receiver(post_save, sender=Attribute)
def attribute_post_save(sender, instance, created, **kwargs):
    InstagramTag.objects.get_or_create(name=instance.hashtag)

@receiver(post_save, sender=Plant)
def plant_post_save(sender, instance, created, **kwargs):
    InstagramTag.objects.get_or_create(name=instance.hashtag)
