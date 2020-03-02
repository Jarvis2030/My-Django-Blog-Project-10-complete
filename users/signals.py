#This file is to enable our users to create create accounts other thatn the admin himself

from django.db.models.signals import post_save

# a post save signal which alerts us when an account is created
from django.contrib.auth.models import User #Sender
from django.dispatch import receiver #Who receives these create_account signals
#IMport profiles

from .models import Profile 

#Function to create user accounts and send signal using the @receive decorator
@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user = instance)


#Function to save user accounts and send signal susing the @receive decorator
@receiver(post_save, sender = User)
def save_profile(sender, instance, **kwargs):
	instance.profile.save() 