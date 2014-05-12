# instamedia/tasks.
from .models import InstagramTag

@task
def sync_all_tags():
    tags = InstagramTag.objects.all()
    for tag in tags:
        tag.sync_remote_images(tag.get_recent_remote_images())

