# about/views.py
from django.views.generic import ListView

from .models import About, Sources, Credits

class AboutListView(ListView):
    queryset = About.objects.filter(visible=True)
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutListView, self).get_context_data(**kwargs)
        extra_context = {
            'sources': Sources.objects.first(),
            'credits': Credits.objects.first(),  
        }
        context.update(extra_context)
        return context