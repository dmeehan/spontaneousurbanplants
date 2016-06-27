#views.py

from django.views.generic import TemplateView

from apps.instamedia.models import InstagramImage
from apps.publications.models import Publication

class LatestImagesWithBookView(TemplateView):
    template_name = 'index.html'

    def random_images(self):
        return InstagramImage.objects.filter(verified=True).order_by('?')[:7]

    def book(self):
        return Publication.objects.first()


class FeaturedItems(TemplateView):
    template_name = 'index.html'

    def featured_plants(self):
        return Plant.objects.filter(featured=True, visible=True)

    def featured_news(self):
        return NewsItem.objects.filter(featured=True, visible=True)

    def book(self):
        return Publication.objects.first()