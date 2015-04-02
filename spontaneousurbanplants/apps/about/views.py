# about/views.py
from django.views.generic import ListView

from .models import AboutContent, SourcesContent, CreditsContent

class AboutListView(ListView):
    queryset = AboutContent.objects.filter(visible=True)
    template_name = 'about.html'
    #context_object_name = 'about'

    def get_context_data(self, **kwargs):
        context = super(AboutListView, self).get_context_data(**kwargs)
        extra_context = {
            'sources': SourcesContent.objects.first(),
            'credits': CreditsContent.objects.first(),  
        }
        context.update(extra_context)
        return context