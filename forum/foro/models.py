from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from string import join
from settings import MEDIA_ROOT

# Create your models here.

class Forum (models.Model):
	titulo = models.CharField(max_length=60)

	# Constructor
	def __unicode__(self):
		return self.title

class Hebra(models.Model):
	titulo = models.CharField(max_length=60)
	creador = models.ForeignKey(User, blank=True, null = True)
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	forum = models.ForeignKey(Forum)

	#Constructor

	def __unicode__(self):
		return unicode(self.creator) + " - " + self.title

class Post(models.Model):
	titulo = models.CharField(max_length=60)
	creador = models.ForeignKey(User, blank=True, null = True)
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	hebra = models.ForeignKey(Hebra)
	cuerpo = models.TextField(max_length=10000)

	def __unicode__(self):
		return u"%s - %s - %s" % (self.creador, self.hebra, self.titulo)

	def short(self):
		return u"%s - %s \n %s" % (self.creador, self.titulo, self.fecha_creacion.strftime("%b %d, %I:%M %p"))
	short.allow_tags = True

class Forum_Admin (admin.ModelAdmin):
	pass

class Hebra_Admin (admin.ModelAdmin):
	lista_display = ["titulo","forum","creador","fecha_creacion"]
	lista_filter = ["titulo", "creador"]

class Post_Admin (admin.ModelAdmin):
	campo_busqueda = ["titulo", "creador"]
	lista_display = ["titulo","forum","creador","fecha_creacion"]

# Gestión admin

admin.site.register(Forum, Forum_Admin)
admin.site.register(Hebra, Hebra_Admin)
admin.site.register(Post, Post_Admin)