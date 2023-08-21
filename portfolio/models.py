from django.db import models

# Create your models here.
class User (models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to= 'portfolio')
    description=models.TextField(max_length=1000)
    email=models.EmailField()
    twiter=models.URLField()
    github=models.URLField()
    linkedin=models.URLField()
    
    def __str__(self):
        return self.name
    

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=50)
    image = models.ImageField(max_length=50)
    
    def __str__(self):
        return self.name


class Experience(models.Model):
    descriptipon=models.TextField(max_length=1000)
    start_date=models.DateField()
    end_date=models.DateField()
    status=models.CharField(max_length=50)
    company=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    
    def __str__(self):
        return self.status


class Education(models.Model):
    description = models.TextField(max_length=1000)
    start_date=models.DateField()
    end_date=models.DateField()
    degree=models.CharField(max_length=50)
    university=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    
    def __str__(self):
        return self.degree

class Skill(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
class Language(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name