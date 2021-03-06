# news/urls.py
from django.conf.urls import url, patterns
from django.views.generic import ListView, DetailView, TemplateView, DateDetailView, MonthArchiveView

from .models import NewsItem
from .views import NewsIndexView

urlpatterns = patterns('', 

    url(r'^$', TemplateView.as_view(template_name="news/news.html"), name = "news"),
    #url(r'^$', NewsIndexView.as_view(), name = 'news'),

    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',
      DateDetailView.as_view(model=NewsItem, context_object_name = "news",
                              date_field="date_published", template_name = "news/newsitem_detail.html"),
        name = 'newsitem_detail'),
    #url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$',
    #    MonthArchiveView.as_view(model=NewsItem,
    #                             context_object_name = "news_list",
    #                             date_field="date_published"),
    #    name='news_archive_month'
    #),
)
