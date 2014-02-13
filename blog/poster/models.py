from django.db import models
from django.contrib.auth.models import User
from poster.models import *

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=200)

class Post(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	description = models.CharField(max_length=1000)
	category = models.ForeignKey(Category)
	creation_date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60)
    body = models.TextField()
    post = models.ForeignKey(Post)
