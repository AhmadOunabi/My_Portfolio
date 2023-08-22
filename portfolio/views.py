from django.shortcuts import render,redirect
from .models import User, Project, Education,Experience,Language,Skill
from .forms import ContactForm
# Create your views here.

def home(request):
    user=User.objects.get(name='Ahmad')
    context={'user':user}
    return render(request, 'home.html', context)


def projects(request):
    projects=Project.objects.all()
    context={'projects':projects}
    return render(request, 'projects.html',context)



def resume(request):
    educations=Education.objects.all()
    experiences=Experience.objects.all()
    languages=Language.objects.all()
    skills=Skill.objects.all()
    context={'educations':educations, 'languages':languages, 'skills':skills,'experiences':experiences}
    return render(request, 'resume.html',context)



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
            
    else:
        form=ContactForm()
    
    return render(request,'contact.html',{'form':form})