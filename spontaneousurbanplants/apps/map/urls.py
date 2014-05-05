# map/urls.py

from django.conf.urls import url, patterns

from .views import MapView

urlpatterns = patterns('',
	url(r'^$', MapView.as_view() , name='map'),
)