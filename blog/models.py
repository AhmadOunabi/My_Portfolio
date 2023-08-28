from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField(max_length=1000)
    image=models.ImageField(upload_to='blog')
    tag=TaggableManager()
    created_date=models.DateTimeField(default=timezone.now())
    
    def __str__(self) :
        return str(self.title)

