from django.db import models
from tools.models import Tool
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    purchased_tools = models.ManyToManyField(Tool, blank=True)
    
    def __str__(self):
        return f'Profile of {self.user.username}'