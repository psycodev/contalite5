
#from Empresas.views import empresaListView
from django.urls import path
from Empresas.views import regEmp,listemp, listempbyid


urlpatterns = [
        path('register/', regEmp, name='register'),
        path('listar/', listemp, name='listarEmp'),
        path('listarbyid/<str:emp_id>', listempbyid, name='listarEmpbyid'),
    ]
