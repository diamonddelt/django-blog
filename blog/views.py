from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
    # the 'posts' variable becomes the 'QuerySet'
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})
