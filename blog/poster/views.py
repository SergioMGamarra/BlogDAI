#enconding: utf-8

from django.shortcuts import render
from poster.models import *
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from poster.forms import *


# Create your views here.

def one_post(request, idpost):
	post = Post.objects.get(id=idpost)

	return render_to_response(
		"post.html",
		{
			"post":post,
		},
		context_instance=RequestContext(request)
	)

def home(request):
	posts = Post.objects.order_by("-creation_date")
	usuario = request.user

	return render_to_response(
		"home.html",
		{
			"posts":posts,
			"usuario":usuario,
		},
		context_instance=RequestContext(request)
	)

def posts_by_category(request, idcategory):
	usuario = request.user

	if idcategory == u'1':
		titulo_act = 'Django'
	elif idcategory == u'2':
		titulo_act = 'Bootstrap'
	category = Category.objects.get(id=idcategory)
	posts = category.post_set.order_by("-creation_date")

	return render_to_response(
		"category.html",
		{
			"usuario":usuario,
			"posts":posts,
			"titulo":titulo_act,
		},
		context_instance=RequestContext(request)
	)

def category(request):
	usuario = request.user

	return render_to_response(
		"category.html",{
			"usuario":usuario,
		},
		context_instance=RequestContext(request)
	)

def get_post(request, idpost):
	if request.method=='POST':
		formularioRelleno = CommentForm(request.POST)
		bodyRelleno = request.POST['body']
		postRelleno = Post.objects.get(id=idpost)
		item = Comment(author=request.user.username,body=bodyRelleno,post=postRelleno)
		item.save()
		comments = postRelleno.comment_set.order_by("-creation_date")
		titulo_act = postRelleno.title
		formularioComentarios = CommentForm()
		return render_to_response(
			"post.html", {
				"comments":comments,
				"titulo":titulo_act,
				"post":postRelleno,
				"FormComent":formularioComentarios,
			},
			context_instance=RequestContext(request)
		)


	else:	
		post = Post.objects.get(id=idpost)
		comments = post.comment_set.order_by("-creation_date")
		titulo_act = post.title
		formularioComentarios = CommentForm()
		return render_to_response(
			"post.html", {
				"comments":comments,
				"titulo":titulo_act,
				"post":post,
				"FormComent":formularioComentarios,
			},
			context_instance=RequestContext(request)
		)

def nuevo_usuario(request):
    if request.method=='POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = UserCreationForm()
    return render_to_response('nuevousuario.html',{'formulario':formulario}, context_instance=RequestContext(request))

def loginUser(request):

    if not request.user.is_anonymous():
        return HttpResponseRedirect('/loginUser')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        usuario = request.POST['username']
        clave = request.POST['password']
        acceso = authenticate(username=usuario, password=clave)
        if acceso is not None:
            if acceso.is_active:
                login(request, acceso)
                return HttpResponseRedirect('/')
            else:
                return render_to_response('/', context_instance=RequestContext(request))
        else:
        	error = 'Los datos introducidos no son correctos'
        	return render_to_response('/loginUser', {'error':error}, context_instance=RequestContext(request))
    else:
        formulario = AuthenticationForm()
    return render_to_response('login.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def privado(request):
	if request.method == 'POST':
		formulario = PostForm(request.POST)
		idcategoria = request.POST['Categoria']
		categoriaPost = Category.objects.get(id=idcategoria)
		nuevo_post = Post(title=request.POST['Titulo'], content=request.POST['Contenido'], description=request.POST['Descripcion'], category=categoriaPost )
		nuevo_post.save()
		return HttpResponseRedirect('/')

	else:
		formulario = PostForm()
		if request.user.username == 'admin':
			return render_to_response('privado.html',{'formulario':formulario}, context_instance=RequestContext(request))
		else:
			return HttpResponseRedirect('/')

@login_required(login_url='/loginUser')
def logoutUser(request):
	logout(request)
	return HttpResponseRedirect('/')
