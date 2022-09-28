from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegistrationForm
from django.contrib import messages

def registerus(request):
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

def listarUsu(request):
    users=User.objects.all()
    data={
            'users': users
        }
    print(users)
    return render(request, "listar.html", data)

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

def deleteUser(request, id):
    users = User.objects.get(id=id)
    users.delete()
    return redirect ('http://127.0.0.1:8000/usuarios/listar')


def listusubyid(request, id):
    users = User.objects.filter(id=id)
    contexto = {'users': users}
    return render(request, "listar.html",contexto)

def consultusu(request):
    id=request.POST['Id']
    url='http://127.0.0.1:8000/usuarios/listarbyid/'+id
    return redirect(url)
    