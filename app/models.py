from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class myCustomUser(AbstractUser):
    username = models.CharField(max_length=20, unique="True", blank=False)
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    userChoice = [
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
        ('Admin', 'Admin')
    ]
    userType = models.CharField(max_length=50, choices=userChoice, default='None', null=True, blank=True)

    isVarified = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(myCustomUser, on_delete=models.CASCADE)
    picture = models.ImageField(blank=True)

    def __str__(self):
        return self.title