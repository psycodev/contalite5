
#from Empresas.views import empresaListView
from django.urls import path
from Empresas import views


urlpatterns = [
        path('register/', views.regEmp, name='register'),
        path('listar/', views.listemp, name='listarEmp'),
        path('listarbyid/<str:emp_id>', views.listempbyid, name='listarEmpbyid'),
        path('editar/<str:id>', views.updatetr, name='updateusu'),
        path('eliminar/<str:id>', views.deletetr, name='deleteUser'),
        path('consultar/',views.consulttr, name='buscar usuarios'),
        
    ]
