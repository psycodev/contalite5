from django.contrib import admin
from . import views
#from Usuarios.views import userListView
from django.urls import path


urlpatterns = [
        path('register/', views.registerTr, name='register'),
        path('listar/', views.listartr, name='empleados'),
        path('editar/<str:id>', views.updatetr, name='updateusu'),
        path('eliminar/<str:id>', views.deletetr, name='deleteUser'),
        path('consultar/',views.consulttr, name='buscar usuarios'),
        path('listarbyid/<str:id>/',views.listusubyid, name='buscar id'),
        #path('logout/', views.logout_request, name='logout'),
        #path('', views.adminview, name='vista page admin'),        
    ]
    