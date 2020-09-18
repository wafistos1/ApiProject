
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employee")
    phone = models.CharField(blank=True, max_length=200)
    picture = models.ImageField(default='default.jpg', upload_to='picture/')
    
    

    def __str__(self):
        return self.user.username

  
class CilentUser(models.Model):
    pass