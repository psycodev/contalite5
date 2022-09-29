from django.shortcuts import render
from django.shortcuts import redirect
from Transacciones.models import Transaccion
from .forms import TransaccionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate

def registerTr(request):
    if request.method =='POST':
        form=TransaccionForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['usuario']
            messages.success(request, f'Transaccion creada por {username} creado con exito')
            return redirect ('http://127.0.0.1:8000/')
    else:
        form=TransaccionForm()
    context={ 'form':form}
    return render(request, 'crearTransaccion-Contalite.html', context)

@login_required
def listartr(request):
    tr=Transaccion.objects.all()
    data={
            'trans': tr
        }
    print(tr)
    return render(request, "visualizarTransaccionContalite.html", data)

@login_required
def updatetr(request, id):
    Trans = Transaccion.objects.get(id_tr=id)
    if request.method == 'GET':
        form=TransaccionForm(instance=Trans)
    else:
        form=TransaccionForm(request.POST, instance=Trans)
        if form.is_valid():
            form.save()
        return redirect("http://127.0.0.1:8000/transacciones/listar")
    return render(request, 'crearTransaccion-Contalite.html', {'form':form}) 

@login_required
def deletetr(request, id):
    tr = Transaccion.objects.get(id_tr=id)
    tr.delete()
    return redirect ('http://127.0.0.1:8000/transacciones/listar')

@login_required
def listusubyid(request, id):
    tr = Transaccion.objects.filter(id=id)
    contexto = {'trans': tr}
    return render(request, "visualizarTransaccionContalite.html",contexto)

@login_required
def consulttr(request):
    id=request.POST['Id']
    url='http://127.0.0.1:8000/transacciones/listarbyid/'+id
    return redirect(url)
