# instagram/views.py
import simplejson

from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
from django.views.generic import DetailView, ListView


from instagram import client, subscriptions

#from notification import models as notification

from .models import InstagramImage, InstagramTag

from .client import get_api, INSTAGRAM_CLIENT_ID

api = get_api()
reactor = subscriptions.SubscriptionsReactor()


class LatestImagesView(ListView):
    queryset = InstagramImage.objects.filter(verified=True).order_by('?')[:8]
    template_name = 'index.html'

class ImageDetailView(DetailView):
    model=InstagramImage
    context_object_name = 'image'

class ImageListView(ListView):
     queryset = InstagramImage.objects.filter(verified=True)

def process_tag_update(update):
    try:
        for item in update:
            print 'process tag A'
            tag = InstagramTag.objects.get(hashtag__iexact=item['object_id'])
            tag.sync_remote_images(tag.get_recent_remote_images())
    except:
        print 'process tag B'
        tag = InstagramTag.objects.get(hashtag__iexact=update['object_id'])
        tag.sync_remote_images(tag.get_recent_remote_images())

    #notification.send(settings.SERVER_EMAIL, "image_submitted", 
    #    { "update": update, })

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

@csrf_exempt
def instagram_realtime_callback(request):
    """Handle instagram realtime API callbacks.

    If request is a GET then we assume that the request is an echo request
    Else we assume that we are receiving data from the source
    """
    if request.method == "POST":
        x_hub_signature = request.META.get('HTTP_X_HUB_SIGNATURE')
        raw_response = request.body
        data = simplejson.loads(raw_response)
        try:
            for item in data:
                print 'callback A'
                tag = InstagramTag.objects.get(hashtag__iexact=item['object_id'])
                tag.sync_remote_images(tag.get_recent_remote_images())
        except:
            print 'callback B'
            #tag = InstagramTag.objects.get(hashtag__iexact=data['object_id'])
            #tag.sync_remote_images(tag.get_recent_remote_images())
        try:
            reactor.process(INSTAGRAM_CLIENT_ID, raw_response, x_hub_signature)
        except subscriptions.SubscriptionVerifyError:
            return HttpResponse("Signature mismatch")
        except Exception as e:
            print >> sys.stderr, "Got error in reactor processing"
            exc_type, exc_value, exc_traceback = sys.exc_info()
            print >> sys.stderr, repr(traceback.format_exception(exc_type, exc_value,exc_traceback))
    else:
        mode = request.GET.get("hub.mode")
        challenge = request.GET.get("hub.challenge")
        verify_token = request.GET.get("hub.verify_token")
        if challenge: 
            return HttpResponse(challenge)
        else:
            return HttpResponse("test", mimetype='text/html')
    