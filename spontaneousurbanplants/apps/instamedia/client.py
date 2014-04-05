# instamedia/client.py

from django.conf import settings

from instagram.client import InstagramAPI

INSTAGRAM_CLIENT_ID = getattr(settings, 'INSTAGRAM_CLIENT_ID', None)
INSTAGRAM_CLIENT_SECRET = getattr(settings, 'INSTAGRAM_CLIENT_SECRET', None)

def get_api():
    return InstagramAPI(client_id=INSTAGRAM_CLIENT_ID, client_secret=INSTAGRAM_CLIENT_SECRET)

