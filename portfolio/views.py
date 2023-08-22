from django.shortcuts import render
from .models import User, Project

# Create your views here.

def home(request):
    user=User.objects.get(name='Ahmad')
    context={'user':user}
    return render(request, 'home.html', context)


def projects(request):
    projects=Project.objects.all()
    context={'projects':projects}
    return render(request, 'projects.html',context)
