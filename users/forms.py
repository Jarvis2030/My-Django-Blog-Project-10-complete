# This is a form thats inhereits from user creation forms
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
	# More fileds:
	email = forms.EmailField()

	class Meta: #Gives a nested namespace configuration in one place telling us the models that will be affected e.g form.save
	
		model = User
		fields = ['username', 'email', 'password1', 'password2']

# Creating new froms to enable users to update their own info from the GUI.
# This will inherit from the ModelForm
class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta: #Gives a nested namespace configuration in one place telling us the models that will be affected e.g form.save
		model = User
		fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile #Name of model
		fields = ['image']