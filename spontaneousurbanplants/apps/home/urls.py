# home/urls.py

from django.conf.urls import url, patterns

from .views import LatestImagesWithBookView, FeaturedItems

urlpatterns = patterns('',
    url(r'^$', FeaturedItems.as_view(), name='home'),
    #url(r'^$', LatestImagesWithBookView.as_view(), name='home'),

)