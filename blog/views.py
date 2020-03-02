from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView, 
	DetailView, 
	CreateView,
	UpdateView,
	DeleteView
)
from .models import Post
# from django.http import HttpResponse


'''Types of views
DeleteView
CreateView
ListView
UpdateView
'''

def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html',context)


class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html' # <app>/<model>_<viewstype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted']

class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form): #To validate forms by the user bf being posted each post must have an author
		form.instance.author = self.request.user #Set the user to the current logged in user
		return super().form_valid(form) #To validate the from with the author

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form): #To validate forms by the user bf being posted each post must have an author
		form.instance.author = self.request.user #Set the user to the current logged in user
		return super().form_valid(form) #To validate the from with the author

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			# Allow them to update the post
			return True

		return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			# Allow them to update the post
			return True

		return False


def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})
