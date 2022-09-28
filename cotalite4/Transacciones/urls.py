from . import views
from django.urls import path


urlpatterns = [
        path('register/', views.registertr, name='register'),
        path('listar/', views.listartr, name='transacciones'),
        path('editar/<str:id>', views.updatetr, name='updatetr'),
        path('eliminar/<str:id>', views.deletetr, name='deletetr'),
        path('consultar/',views.consulttr, name='redireccionamiento transaccioens'),
        path('listarbyid/<str:id>/',views.listtrbyid, name='buscar idtr'),
        ]
    