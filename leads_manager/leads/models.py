from django.db import models

class Lead(models.Model):
	""" Lead model
	"""
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100, unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	message = models.CharField(max_length=500, blank=True)
