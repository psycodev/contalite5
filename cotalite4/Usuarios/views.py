from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate

def register(request):
    if request.method =='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado con exito')
            return redirect ('http://127.0.0.1:8000/')
    else:
        form=RegistrationForm()
    context={ 'form':form}
    return render(request, 'registrar.html', context)

@login_required
def listarUsu(request):
    users=User.objects.all()
    data={
            'users': users
        }
    print(users)
    return render(request, "listar.html", data)

@login_required
def updateusu(request, id):
    users = User.objects.get(id=id)
    if request.method == 'GET':
        form=RegistrationForm(instance=users)
    else:
        form=RegistrationForm(request.POST, instance=users)
        if form.is_valid():
            form.save()
        return redirect("http://127.0.0.1:8000/usuarios/listar")
    return render(request, 'registrar.html', {'form':form}) 

@login_required
def deleteUser(request, id):
    users = User.objects.get(id=id)
    users.delete()
    return redirect ('http://127.0.0.1:8000/usuarios/listar')

@login_required
def listusubyid(request, id):
    users = User.objects.filter(id=id)
    contexto = {'users': users}
    return render(request, "listar.html",contexto)

@login_required
def consultemp(request):
    id=request.POST['Id']
    url='http://127.0.0.1:8000/usuarios/listarbyid/'+id
    return redirect(url)

def logout_request(request):
    logout(request)
    messages.info(request,"Saliste Exitosamente")
    return redirect ('http://127.0.0.1:8000/accounts/login/')