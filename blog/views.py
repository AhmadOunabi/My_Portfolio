from django.shortcuts import render
from .models import Post
# Create your views here.


def posts(request):
    pass
    return render(request, 'posts.html',)
