from django.contrib import admin
from .models import Post #To include the models

admin.site.register(Post) #To register our posts with the admin site