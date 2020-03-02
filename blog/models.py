from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User #Post and user models are having a rlnship i.e the one to many relationship
from django.urls import reverse 


class Post(models.Model):
	title = models.CharField(max_length = 100) #To create constraints in that field
	content = models.TextField() #Unrestricted field with many characters
	# date_posted = models.DateTimeField(auto_now = True) #To automatically set the updated time to now
	date_posted = models.DateTimeField(default = timezone.now) #To set the datetime to default as provided by the timezone of the user(import timezone)

	author = models.ForeignKey(User, on_delete = models.CASCADE) #If a user made a post and deleted their account, we need to set the post to none and deelete the post as well ussing thee cascade
	
	def __str__(self):
		return self.title
		
	# To tell django to get the urls of any specific instance of a post
	def get_absolute(self):
		return reverse('post-detail', kwargs = {'pk': self.pk})
