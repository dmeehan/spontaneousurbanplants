# instamedia/tasks.
from .models import InstagramTag

def sync_all_tags():
    tags = InstagramTag.objects.all()
    for tag in tags:
        if tag.sync:
            tag.sync_remote_images(tag.get_recent_remote_images())

