from rest_framework import serializers
from DataLogSensor.models import Registro
from Device.models import Tipo,Sensor
from DataLogSensor.validators import *
from django_filters import rest_framework as filters

class RegistroFilter(filters.FilterSet):
    inicio = filters.DateFilter(field_name="data_registro", lookup_expr="gte")
    fim = filters.DateFilter(field_name="data_registro", lookup_expr="lte")
    class Meta:
        model = Registro
        fields = ['sensor',]


class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = '__all__'


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'

class VisualizarRegistroSerializer(serializers.ModelSerializer):

    sensor = serializers.ReadOnlyField(source='sensor.sensor')
    class Meta:
        model = Registro
        fields = ['id', 'sensor', 'date','time','mm_h','mm_dia','temp','umidade','pressao','vmed','vmax','direcao','uv','w_m2','data_registro']

class RegistroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Registro
        fields = ['id', 'sensor', 'date','time','mm_h','mm_dia','temp','umidade','pressao','vmed','vmax','direcao','uv','w_m2','data_registro']
        
   
