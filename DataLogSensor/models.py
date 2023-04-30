from wsgiref.handlers import format_date_time
from django.db import models
from Device.models import Tipo,Sensor
from datetime import datetime

class Registro(models.Model):

    sensor = models.ForeignKey(Sensor, blank=False, null=False,on_delete=models.CASCADE,verbose_name = 'Identificação do Sensor')
    date= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'Date')
    time= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'Time')
    mm_h= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'mm_h')
    mm_dia= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'mm_dia')
    temp= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'temp')
    umidade= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'umidade')
    pressao= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'pressao')
    vmed= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'vmed')
    vmax= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'vmax')
    direcao= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'dir')
    uv= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'uv')
    w_m2= models.CharField(max_length=8,blank=True, null=False,verbose_name = 'w_m2')
    data_registro = models.DateTimeField(auto_now=True,verbose_name='Data do registro') 
  
    
    