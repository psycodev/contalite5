from django.shortcuts import render
from Empresas.forms import registrarUsuario
from Empresas.models import Empresa

def regEmp(request):
    if request.method == 'POST':
        form = registrarUsuario(request.POST)
        if form.is_valid():
            form.save()
    else:
        form =registrarUsuario()    
    return render(request, "registrarEmp.html",{'form':form})

def listemp(request):
    empresas = Empresa.objects.all()
    contexto = {'empresas':empresas}
    return render(request, "listarEmp.html",contexto)

def listempbyid(request, emp_id):
    empresas = Empresa.objects.filter(emp_id=emp_id)
    contexto = {'empresas':empresas}
    return render(request, "listarEmp.html",contexto)
