from django.contrib import admin
from django.urls import path, include
from .views import posts
urlpatterns = [
    path('posts/' , posts)
]
