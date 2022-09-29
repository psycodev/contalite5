from django import forms
from Transacciones.models import Transaccion
from django.contrib.auth.forms import UserCreationForm

class TransaccionForm(UserCreationForm):
   
    class Meta: 
        model= Transaccion
        fields=[
            'tipo',
            'usuario',
            'concepto',
            'monto',   
        ]
        labels ={
            'tipo':'Tipo de Transaccion',
            'usuario':'Usuario que realiza',
            'concepto':'Concepto',
            'monto':"Monto",
        }
    Widgets ={
           # 'id_tr': forms.TextInput(attrs={'class':'form-control'}),
            'tipo': forms.TextInput(attrs={"class":"form"}), #forms.Select(attrs={"class":"form"})
            'usuario': forms.Select(attrs={"class":"form"}),
            'concepto': forms.TextInput(attrs={'class':'form-control'}),   
            'monto': forms.TextInput(attrs={'class':'form-control'}),
        }
