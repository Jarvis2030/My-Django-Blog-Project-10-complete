from django.db import models
# To add profile pics to our users
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.for user profiles

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE) #One 2 one rlnshhipwith the user hence parse it as an argument
	# CASCADE == delete the user posts too when their acc is deleted
	image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')


	def __str__(self):
		return f'{self.user.username} Profile'

		# Remember to run your migrations for the db to take effect ofg the changes.
	
	#Profile pic resizing 
	def save(self):
		super().save()

		img = Image.open(self.image.path)
		# Checking image size for resize
		if img.height or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size) # To resave

			img.save(self.image.path) #This saves and overwrites the older image uploaded by the user you can check online for any other resizing algorithms
