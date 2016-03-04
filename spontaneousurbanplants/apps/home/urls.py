# home/urls.py

from django.conf.urls import url, patterns

from .views import LatestImagesWithBookView

urlpatterns = patterns('',
    url(r'^$', LatestImagesWithBookView.as_view(), name='home'),
)