# plants/models.py
from django.db import models


class Attribute(models.Model):
    """A descriptive aspect of a plant or plants.

    """
    name = models.CharField(max_length=255)
    hashtag = models.CharField(max_length=255, 
                               unique=True,
                               help_text='A unique hashtag indentifying this plant. Do not include #.')
    description = models.TextField(blank=True)

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

    attributes = models.ManyToManyField(Attribute, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.latin_name)
