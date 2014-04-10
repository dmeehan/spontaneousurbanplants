from django.contrib import admin
from django.conf.urls import patterns, include, url

from django.views.generic import TemplateView

from apps.instamedia.views import LatestImagesView


# See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#hooking-adminsite-instances-into-your-urlconf
admin.autodiscover()


# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns = patterns('',
    # Admin panel and documentation:
    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', LatestImagesView.as_view(), name='home'),

     url(r'^feed/', include('apps.instamedia.urls')),

    url(r'^about/', TemplateView.as_view(template_name='about.html'), name="about"),
)