from django.contrib import admin
from django.urls import path, include

from blog.models import Blog
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:blog_id>/', views.detail, name='detail'),

]