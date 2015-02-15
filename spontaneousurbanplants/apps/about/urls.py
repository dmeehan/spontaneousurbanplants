# about/urls.py
from django.conf.urls import url, patterns

from .views import AboutListView

urlpatterns = patterns('',
	url(r'^$', AboutListView.as_view(), name='about'),
)
