# This is a form thats inhereits from user creation forms
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	# More fileds:
	email = forms.EmailField()

	class Meta: #Gives a nested namespace configuration in one place telling us the models that will be affected e.g form.save
	
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		