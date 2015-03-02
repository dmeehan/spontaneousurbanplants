# news/views.py
from django.views.generic import ListView, DetailView, ArchiveIndexView

from .models import NewsItem

class NewsDetailView(DetailView):
    model = NewsItem

class NewsListView(ListView):
    model = NewsItem

class NewsIndexView(ArchiveIndexView):
    model = NewsItem
    date_field="date_published"
