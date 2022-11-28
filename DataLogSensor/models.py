from wsgiref.handlers import format_date_time
from django.db import models
from Device.models import Tipo,Sensor
from datetime import datetime

class Registro(models.Model):

    # inicialização das variaveis e seus parametros
    sensor = models.ForeignKey(Sensor, blank=False, null=False,on_delete=models.CASCADE,verbose_name = 'Identificação do Sensor')
    temperatura = models.CharField(max_length=8,blank=False, null=False,verbose_name = 'Temperatura')
    pressao = models.CharField(max_length=11,blank=False, null=False,verbose_name = 'Pressão')
    precipitacao = models.CharField(max_length=11,blank=False, null=True,verbose_name = 'Precipitação')
    altitude = models.CharField(max_length=11,blank=False, null=False,verbose_name = 'Altitude')
    pressa_nivel_mar = models.CharField(max_length=11,blank=False, null=False,verbose_name = 'Pressão a nível do mar')
    altitude_real= models.CharField(max_length=11,blank=False, null=False,verbose_name = 'Altitude real')
    data_registro = models.DateTimeField(auto_now=True,verbose_name='Data do registro') 
  
    