from django.contrib import admin
from django.urls import path, include
from .views import home,projects

urlpatterns = [
    path('', home),
    path('projects/', projects),
]
