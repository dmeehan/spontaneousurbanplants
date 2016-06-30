#views.py

from django.views.generic import TemplateView

from apps.instamedia.models import InstagramImage
from apps.publications.models import Publication
from apps.news.models import NewsItem
from apps.plants.models import Plant

class LatestImagesWithBookView(TemplateView):
    template_name = 'index.html'

    def random_images(self):
        return InstagramImage.objects.filter(verified=True).order_by('?')[:7]

    def book(self):
        return Publication.objects.first()


class FeaturedItems(TemplateView):
    template_name = 'landing.html'

    def featured_plants(self):
        return Plant.objects.filter(featured=True, visible=True)

    def featured_news(self):
        return NewsItem.objects.filter(featured=True)

    def book(self):
        return Publication.objects.first()