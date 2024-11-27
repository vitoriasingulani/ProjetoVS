
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    # rota, view responsável, nome de referência
    # usuários.com
    path('', views.home ,name='home'),
    #usuários.com/usuarios
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
]
