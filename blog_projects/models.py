from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Title: {self.title} Blog: {self.text}'
    
#Create Description model here
class Description(models.Model):
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'descriptions'
        
    def __str__(self):
        return f'{self.text[:80]}'
    

    
