from wsgiref.handlers import format_date_time
from django.db import models
from Device.models import Tipo,Sensor
from datetime import datetime

class Registro(models.Model):

    sensor = models.ForeignKey(Sensor, blank=False, null=False,on_delete=models.CASCADE,verbose_name = 'Identificação do Sensor')
    date= models.CharField(max_length=10,blank=True, null=False,verbose_name = 'Date')
    time= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'Time')
    mm_h= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'mm/hora')
    mm_dia= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'mm/dia')
    temp= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'Temperatura')
    umidade= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'Umidade')
    pressao= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'Pressao')
    vmed= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'Velocidade média')
    vmax= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'Velocidade máxima')
    direcao= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'Direção')
    uv= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'UV')
    w_m2= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'W/m2')
    data_registro = models.DateTimeField(auto_now=True,verbose_name='Data do registro') 
  
    
    