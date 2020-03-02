from django.shortcuts import render, redirect
from django.contrib import messages #To send one-time flash/alert messages to the user on submit
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect #To redirect the new user to the required page
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm #We use it together with the email instead of the UserCreationForm # Adding the forms that weve just created in the forms template
''' Types of messages:
		messages.debug()
		messages.info()
		messages.success()
		messages.warning()
		messages.error()
		'''

# Create your views here.
def register(request):
	# To check for requests
	if request.method  == 'POST':
		form = UserRegisterForm(request.POST) #Data

		# To validate more on the data and fields sent by the user submits
		if form.is_valid():
			form.save() #If form is valid the passwords will be hashed and encrypted
			username = form.cleaned_data.get('username') #The validated form data will be in the form.cleaned_data dictionary
			messages.success(request, f'Your account has been created succesfully! You can now Login')
			return redirect('login') #Return /redirect to blog-home(Name given to the url pattern in our blog homepage)
			
	else: #Anything that is not a post request will create a blank form
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form}) #forms are instantiated with our request data in line18 above

@login_required #A decorator that adds functionalities to an existing function profile views to enable logins bf views profile
def profile(request):
	if request.method  == 'POST':
		u_form = UserUpdateForm(request.POST, instance = request.user) #Instantiating empty userform
		p_form = ProfileUpdateForm(request.POST,
								   request.FILES,
		 						   instance = request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been Updated succesfully!')
			return redirect('profile')

	else:
		u_form = UserUpdateForm(instance = request.user) #Instantiating empty userform
		p_form = ProfileUpdateForm(instance = request.user.profile)

	context = {
		'u_form': u_form,
		'p_form': p_form
			}
	return render(request, 'users/profile.html', context)