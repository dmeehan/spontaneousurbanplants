# instagram/views.py

from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.http.response import HttpResponse
from django.views.generic import DetailView, ListView

from instagram import client, subscriptions

from .models import InstagramImage


INSTAGRAM_CLIENT_ID = getattr(settings, 'INSTAGRAM_CLIENT_ID', None)
INSTAGRAM_CLIENT_SECRET = getattr(settings, 'INSTAGRAM_CLIENT_SECRET', None)

CONFIG = {
    'client_id': INSTAGRAM_CLIENT_ID,
    'client_secret': INSTAGRAM_CLIENT_SECRET,
    'redirect_uri': 'http://127.0.0.1:8000/instagram/oauth_callback'
}

api = client.InstagramAPI(**CONFIG)


class LatestImagesView(ListView):
    queryset = InstagramImage.objects.filter(verified=True)[:20]
    template_name = 'index.html'

class ImageDetailView(DetailView):
    model=InstagramImage
    context_object_name = 'image'

class ImageListView(ListView):
     queryset = InstagramImage.objects.filter(verified=True)

def process_tag_update(update):
    print update

reactor = subscriptions.SubscriptionsReactor()
reactor.register_callback(subscriptions.SubscriptionType.TAG, process_tag_update)


def authenticate(request):
    try:
        url = api.get_authorize_url(scope=["likes","comments"])
        return HttpResponse('<a href="%s">Connect with Instagram</a>' % url)
    except Exception, e:
        return HttpResponse(e)


def instagram_callback(request):
    code = request.GET.get("code")
    if not code:
        return HttpResponse('Missing code')
    try:
        access_token, user_info = api.exchange_code_for_access_token(code)
        if not access_token:
            return HttpResponse('Could not get access token')
        
        authenticated_api = client.InstagramAPI(access_token=access_token)
        recent_media, next = authenticated_api.user_recent_media()
        photos = []
        for media in recent_media:
            photos.append('<img src="%s"/>' % media.images['thumbnail'].url)
        return HttpResponse(''.join(photos))
    except Exception, e:
        return HttpResponse(e)


def instagram_realtime_callback(request):
    """Handle instagram realtime API callbacks.

    If request is a GET then we assume that the request is an echo request
    Else we assume that we are receiving data from the source
    """
    if request.method == "POST":
        x_hub_signature = request.header.get('X-Hub-Signature')
        raw_response = request.body
        return HttpResponse(raw_response)
        try:
            reactor.process(CONFIG['client_secret'], raw_response, x_hub_signature)
        except subscriptions.SubscriptionVerifyError:
            return HttpResponse("Signature mismatch")
    else:
        mode = request.GET.get("hub.mode")
        challenge = request.GET.get("hub.challenge")
        verify_token = request.GET.get("hub.verify_token")
        if challenge: 
            return HttpResponse(challenge)

    
    