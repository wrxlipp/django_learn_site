from django.urls import path, include, re_path
from . import views

urlpatterns = [
    re_path(r'', views.blog_main), # domen.com/blog/
]

