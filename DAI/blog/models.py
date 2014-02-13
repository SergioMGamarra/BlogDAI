from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_lenght=200)

class Post(models.Model):
	author = models.ForeignKey(User, related_name='posts')
	

