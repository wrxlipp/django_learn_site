from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path(r'', views.blog_main), # domen.com/blog/
    path('register/', views.register),
    path('logout/', views.logout_request),
    path('login/', views.login_request),
    path('search_post/', views.search_post, name="search"),
    path('<slug>/', views.slug_process),
]

