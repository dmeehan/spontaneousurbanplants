# services/views.py

from django.views.generic import ListView

from .models import Service, ServicesContent

class ServiceListView(ListView):
    model = Service
    template_name = 'services.html'

    def get_context_data(self, **kwargs):
        context = super(ServiceListView, self).get_context_data(**kwargs)
        extra_context = {
            'introduction': ServicesContent.objects.first(),
        }
        context.update(extra_context)
        return context