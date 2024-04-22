from django.db import models
from django.contrib.auth.models import *

# Create your models here.
class Users(AbstractUser):
    image=models.ImageField(upload_to='users/images/')


    def __str__(self):
        return self.username