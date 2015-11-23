from django.contrib import admin
from .models import Post

# This registers the 'Post' model class object created in models.py
admin.site.register(Post)
