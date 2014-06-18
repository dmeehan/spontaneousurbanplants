# plants/tasks.py
from apps.instamedia.models import InstagramImage

def associate_images(plant):
	""" Associate images tagged with the plant hashtag with the Plant object

		Takes a Plant object as an argument.
	"""
	images = InstagramImage.objects.filter(tags__name__iexact=plant.hashtag)
	for image in images:
		Plant.images.add(image)
		Plant.save()
		print("Associated %s with %s") % (plant, image)

