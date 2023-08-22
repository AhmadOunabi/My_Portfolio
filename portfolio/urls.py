from django.contrib import admin
from django.urls import path, include
from .views import home , projects , resume , contact

urlpatterns = [
    path('', home),
    path('projects/', projects),
    path('resume/', resume),
    path('contact/', contact),
]
