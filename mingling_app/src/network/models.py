from django.db import models
from django.conf import settings

class SignUp(models.Model):
	full_name = models.CharField(max_length=120, blank=False, null=True)
	img_link = models.TextField(max_length=120, blank=False, null=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.full_name

class Mingler(models.Model): 
	full_name = models.CharField(max_length=120, default='Anna')
	img_path = models.ImageField(upload_to='media/', default = 'pic_folder/None/no-img.jpg')
	my_hashtags = models.TextField(blank=False, null=True) # TODO: Need to change it
	looking_for_hashtags = models.TextField(blank=False, null=True) # TODO: Need to change it
	description = models.TextField(max_length=2000, blank=False, null=True)
	email = models.CharField(max_length=120, blank=False, default='none')
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.full_name






