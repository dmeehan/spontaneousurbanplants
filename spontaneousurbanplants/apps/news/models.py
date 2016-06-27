# news/models.py
import datetime
import markdown

from django.db import models
from django.db.models import permalink

from positions.fields import PositionField

class NewsItem(models.Model):
    """An article entry for a news item.

    """
    title = models.CharField(max_length=255)
    excerpt = models.TextField(blank=True)
    body = models.TextField()

    # Fields to store generated HTML.
    excerpt_html = models.TextField(editable=False, blank=True)
    body_html = models.TextField(editable=False, blank=True)

    # metadata
    featured = models.BooleanField(default=False)
    featured_image = models.ImageField(upload_to="images/news", blank=True, null=True)
    date_published = models.DateTimeField(default=datetime.datetime.now)
    slug = models.SlugField(unique_for_date='date_published')

    STATUS_PUBLISHED = 1
    STATUS_HIDDEN = 2
    STATUS_DRAFT = 3
    STATUS_CHOICES = (
        (STATUS_PUBLISHED, 'Published'),
        (STATUS_HIDDEN, 'Hidden'),
        (STATUS_DRAFT, 'Draft'),
    )

    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES,
        default=STATUS_DRAFT,
        help_text="Only content with published status will be publicly displayed.")

    class Meta:
        ordering = ['-date_published']
        get_latest_by = 'date_published'

    def render_markup(self):
        """Turns any markup into HTML"""
        self.body_html = markdown.markdown(self.body)
        self.excerpt_html = markdown.markdown(self.excerpt)

    def get_previous_newsitem(self):
        return self.get_previous_by_date_published(status=self.STATUS_PUBLISHED)

    def get_next_newsitem(self):
        return self.get_next_by_date_published(status=self.STATUS_PUBLISHED)  

    @permalink
    def get_absolute_url(self):
        return ('newsitem_detail', None, {
            'year': self.date_published.year,
            'month': self.date_published.strftime('%b').lower(),
            'day': self.date_published.day,
            'slug': self.slug
        })

    def save(self, force_insert=False, force_update=False):
        self.render_markup()
        super(NewsItem, self).save(force_insert, force_update)

    def __unicode__(self):
        return u'%s' % (self.title)


class NewsItemImage(models.Model):
    """Image for a news item.

    """

    image_file = models.ImageField(upload_to="images/news")
    title = models.CharField(max_length=255, blank=True)
    caption = models.TextField(null=True, blank=True)
    
    news_item = models.ForeignKey(NewsItem)

    visible = models.BooleanField(default=True, 
        help_text="This image is publicly available.")
    order = PositionField()
    is_main = models.BooleanField('Main image', default=False)


    def __unicode__(self):
        if self.title:
            return u'%s' % self.title
        elif self.order:
            n = self.order + 1
            return u'%s image %d' % (self.news_item.title, n)
        else:
            return u'%s image 1' % self.news_item.title
