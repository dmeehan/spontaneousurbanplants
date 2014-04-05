# instagram/urls.py

from django.conf.urls import url, patterns

from .views import LatestMediaView

urlpatterns = patterns('',
	url(r'^$', LatestMediaView.as_view(), name='home'),
	url(r'^authenticate/$', 'apps.instamedia.views.authenticate', name='authenticate'),
	url(r'^subscribe/$', 'apps.instamedia.views.subscribe', name='subscribe'),
    url(r'^oauth_callback/$', 'apps.instamedia.views.instagram_callback', 
    	name='instagram_callback'),
    url(r'^realtime_callback/$', 'apps.instamedia.views.instagram_realtime_callback', 
    	name='instagram_realtime_callback'),

)