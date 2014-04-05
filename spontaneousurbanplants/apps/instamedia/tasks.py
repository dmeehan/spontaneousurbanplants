# instamedia/tasks.
from celery import task

@task(name='sync_images_for_tag')
def sync_images_for_tag(instance):
    instance.sync_remote_images()