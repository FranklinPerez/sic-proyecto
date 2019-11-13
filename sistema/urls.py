
from django.urls import path, include
from .views import *

app_name = 'sistema'
urlpatterns=[
	path('index/', index, name='index'),

	path('iniciarSesion', iniciarSesion, name='inicar_sesion'),
	path('autenticarUsuario', autenticarUsuario, name='autenticar_usuario'),
	path('cerrarSesion', cerrarSesion, name='cerrar_sesion'),
	
	]