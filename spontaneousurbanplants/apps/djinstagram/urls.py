# instagram/urls.py

from django.conf.urls import url, patterns

urlpatterns = patterns('',
	url(r'^$', 'apps.djinstagram.views.home', name='home'),
	url(r'^authenticate/$', 'apps.djinstagram.views.authenticate', name='authenticate'),
	url(r'^subscribe/$', 'apps.djinstagram.views.subscribe', name='subscribe'),
    url(r'^oauth_callback/$', 'apps.djinstagram.views.instagram_callback', 
    	name='instagram_callback'),
    url(r'^realtime_callback/$', 'apps.djinstagram.views.instagram_realtime_callback', 
    	name='instagram_realtime_callback'),

)