# services/urls.py

from django.conf.urls import url, patterns

from .views import ServiceListView

urlpatterns = patterns('',
	url(r'^$', ServiceListView.as_view(), name='services'),
)