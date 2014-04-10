# instagram/urls.py

from django.conf.urls import url, patterns

from .views import ImageDetailView, ImageListView

urlpatterns = patterns('',
	url(r'^images/$', ImageListView.as_view() , name='instamedia_image_list'),
	url(r'^images/(?P<pk>\d+)/$', ImageDetailView.as_view(), name='instamedia_image_detail'),
	url(r'^authenticate/$', 'apps.instamedia.views.authenticate', name='authenticate'),
	#url(r'^subscribe/$', 'apps.instamedia.views.subscribe', name='subscribe'),
    url(r'^oauth_callback/$', 'apps.instamedia.views.instagram_callback', 
    	name='instagram_callback'),
    url(r'^realtime_callback/$', 'apps.instamedia.views.instagram_realtime_callback', 
    	name='instagram_realtime_callback'),

)