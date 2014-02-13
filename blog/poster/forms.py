#encoding:utf-8 
from django.forms import ModelForm
from django import forms
from poster.models import Comment

class CommentForm(forms.Form):
	body = forms.CharField(widget= forms.Textarea,label='Comentario', required=True)


class PostForm(forms.Form):
	CATEGORY_CHOICES = (
        (1, u'Django'),
        (2, u'Bootstrap'),)
	Titulo = forms.CharField(label='Titulo del post', required=True)
	Contenido = forms.CharField(label='Contenido', widget=forms.Textarea, required=True)
	Descripcion = forms.CharField(label='Breve descripción', required=True)
	Categoria = forms.ChoiceField(choices=CATEGORY_CHOICES, initial='Django', required=True) 
