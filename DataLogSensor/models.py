from wsgiref.handlers import format_date_time
from django.db import models
from Device.models import Tipo,Sensor
from datetime import datetime

class Registro(models.Model):

    estacao = models.ForeignKey(Sensor, blank=False, null=False,on_delete=models.CASCADE,verbose_name = 'Identificação da Estação')
    data= models.CharField(max_length=10,blank=True, null=False,verbose_name = 'Data')
    hora= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'Hora')
    temp_min= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'Temperatura Mínima')
    temp_max= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'Temperatura Máxima')
    temp_media= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'Temperatura Média')
    
    umidade_min= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'Umidade Mínima')
    umidade_max= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'Umidade Máxima')
    umidade_media= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'Umidade Média')

    vm_min= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'Velocidade Mínima')
    vm_max= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'Velocidade Máxima')
    vm_med= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'Velocidade Média')
   

    pressao_min= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'Pressao Mínima')
    pressao_max= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'Pressao Máxima')
    pressao_media= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'Pressao Média')

    direcao= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'Direção do vento')
    w_m2= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'W/m2')
    uv= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'UV')
    mm_ciclo= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'mm/ciclo')
    data_registro = models.DateTimeField(auto_now=True,verbose_name='Data do registro') 
  
    
    