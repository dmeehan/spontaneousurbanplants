# instagram/views.py

from instagram import client, subscriptions


def process_tag_update(update):
    print update

def create_subscription(request):
	pass
	In order to verify the subscription, 
	your server must respond to the GET request with the hub.challenge parameter only:

def process_update(request):
	if request.method == 'GET':
    	response = request.GET.get('hub.challenge')
    	return HttpResponse(response)
	elif request.method == 'POST':
    	#process update


@route('/realtime_callback')
@post('/realtime_callback')
def on_realtime_callback():
    mode = request.GET.get("hub.mode")
    challenge = request.GET.get("hub.challenge")
    verify_token = request.GET.get("hub.verify_token")
    if challenge: 
        return challenge
    else:
        x_hub_signature = request.header.get('X-Hub-Signature')
        raw_response = request.body.read()
        try:
            reactor.process(CONFIG['client_secret'], raw_response, x_hub_signature)
        except subscriptions.SubscriptionVerifyError:
            print "Signature mismatch"


reactor = subscriptions.SubscriptionsReactor()
reactor.register_callback(subscriptions.SubscriptionType.TAG, process_tag_update)