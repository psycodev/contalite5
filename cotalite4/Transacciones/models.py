from .choices import trans
from django.db import models
from django.contrib.auth.models import User

#creamos los modelos de xlas tablas que vamos a usar

class Transaccion(models.Model):
    id_tr=models.AutoField(auto_created=True,unique=True,primary_key=True)
    #tipo=models.Choices(trans)
    tipo=models.CharField("tipo", max_length=20, choices=trans, default= 'Elija una opcion')
    fecha_tr=models.DateField(auto_now=True)
    usuario=models.ForeignKey(User,related_name="transaccion", on_delete=models.CASCADE)
    concepto=models.TextField("Concepto",max_length=500,null=False) 
    monto=models.IntegerField("Monto",null=False) 


