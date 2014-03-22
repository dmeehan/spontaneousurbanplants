# instagram/urls.py

from django.conf.urls import url, patterns

urlpatterns = patterns('',
    url(r'^$', 'apps.instagram.views.process_update', name='instagram_process_update'),
)