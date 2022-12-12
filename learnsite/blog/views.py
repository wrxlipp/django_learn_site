from django.shortcuts import render
from .models import Post
# Create your views here.

def blog_main(request, *args):
    data_dict  ={
        "posts": Post.objects.all()
    }
    return render(request, 'blog_main.html', data_dict)
