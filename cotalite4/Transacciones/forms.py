from django import forms
from Transacciones.models import Transaccion


class TransaccionForm(forms.ModelForm):
   
    class Meta: 
        model= Transaccion
        fields=[
            'tipo',
            'usuario',
            'monto',  
            'concepto',
             
        ]
        labels ={
            'tipo':'Tipo de Transaccion',
            'usuario':'Usuario que realiza',
            'monto':"Monto",
            'concepto':'Concepto',
            
        }
    Widgets ={
           # 'id_tr': forms.TextInput(attrs={'class':'form-control'}),
            'tipo': forms.TextInput(attrs={"class":"form"}), #forms.Select(attrs={"class":"form"})
            'usuario': forms.Select(attrs={"class":"form"}),
            'monto': forms.NumberInput(attrs={'class':'form-control'}),
            'concepto': forms.TextInput(attrs={'class':'form-control'}),   
            
        }
