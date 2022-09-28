from django.contrib import admin
from . import views
#from Usuarios.views import userListView
from django.urls import path


urlpatterns = [
        path('register/', views.registerus, name='register'),
        path('listar/', views.listarUsu, name='empleados'),
        path('editar/<str:id>', views.updateusu, name='updateusu'),
        path('eliminar/<str:id>', views.deleteUser, name='deleteUser'),
        path('consultar/',views.consultusu, name='buscar usuarios'),
        path('listarbyid/<str:id>/',views.listusubyid, name='buscar id'),

        
    ]
    