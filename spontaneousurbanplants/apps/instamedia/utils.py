#instamedia/utils.py
from django.core.urlresolvers import reverse_lazy
from django.http import HttpRequest

def get_callback_url():
	return HttpRequest.build_absolute_uri(reverse_lazy('instagram_callback'))


def get_realtime_callback_url():
	return HttpRequest.build_absolute_uri(reverse_lazy('instagram_realtime_callback'))