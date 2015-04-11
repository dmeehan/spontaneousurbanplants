# plants/urls.py
from django.conf.urls import url, patterns

from .views import PlantListView, PlantDetailView

urlpatterns = patterns('',
	url(r'^$', PlantListView.as_view(), name='plants'),
	url(r'^(?P<slug>[-\w]+)/$', PlantDetailView.as_view(), name='plant_detail'),
)

