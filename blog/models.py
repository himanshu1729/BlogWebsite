from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    
    title = models.CharField(max_length = 100)
    
    content = models.TextField()
    
    ''' on_delete = cascade causes all posts to delete if we delete user'''
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    
    '''Notice that when passing default we passed the function itself'''
    '''and not the value like 'timezone.now() '''

    date_posted  = models.DateTimeField(default = timezone.now) 


    def __str__(self):
        return  self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', kwargs ={'pk':self.pk})


'''A model for storing Liked Posts'''
class Likes(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    post = models.ForeignKey(Post, on_delete = models.CASCADE)

    def __str__(self):
        return f"{str(self.user)} {str(self.post)}"
