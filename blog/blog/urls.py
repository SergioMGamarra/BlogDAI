from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',

	url (
		r'^post/(?P<idpost>[0-9]+)/$',
		'poster.views.get_post',
		name="getpost_post",
	),
    
	url (
		r'^category/(?P<idcategory>[0-9]+)/$',
		'poster.views.posts_by_category',
		name="posts_by_category"
	),

	url (
		r'^$',
		'poster.views.home',
		name='home',
	),

	url (
		r'^home',
		'poster.views.home',
		name='home',
	),

	url (
		r'^categorys',
		'poster.views.category',
		name='category',
	),

    url(
    	r'^admin/', 
    	include(admin.site.urls),
    ),

    url(
    	r'^usuario/nuevo$',
    	'poster.views.nuevo_usuario',
    ),

    url(
    	r'^cerrar/$', 
    	'poster.views.logoutUser'
    ),

    url(
    	r'^loginUser',
    	'poster.views.loginUser',
    	name ='loginUser',
    ),

    url(
    	r'^privado',
    	'poster.views.privado'
    ),

)
