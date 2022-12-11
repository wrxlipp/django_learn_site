from django.urls import path, include, re_path
from . import views

urlpatterns = [
    re_path(r'([0-9]{4})', views.blog_main),
]

