from django.contrib import admin
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView

from .views import LatestImagesWithBookView


# See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#hooking-adminsite-instances-into-your-urlconf
admin.autodiscover()

# api machinery
from rest_framework import routers

from apps.map.views import ImageApiViewSet

router = routers.DefaultRouter()
router.register(r'images', ImageApiViewSet, base_name='api-image')


# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns = patterns('',
    # Admin panel and documentation:
    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', LatestImagesWithBookView.as_view(), name='home'),

    url(r'^feed/', include('apps.instamedia.urls')),

    url(r'^map/', include('apps.map.urls')),

    url(r'^about/', include('apps.about.urls')),

    url(r'^services/', include('apps.services.urls')),

    url(r'^book/', include('apps.publications.urls')),

    url(r'^plants/', include('apps.plants.urls')),

    url(r'^news/', include('apps.news.urls')),

    # api
    url(r"^api/", include(router.urls)),
    url(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
