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
        fields = ['estacao',]


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
        fields = ['id', 'estacao', 'data','hora','temp_min','temp_max','temp_media','umidade_min','umidade_max','umidade_media',
    'vm_min','vm_max','vm_media','pressao_min','pressao_max','pressao_media','direcao','w_m2','uv','mm_ciclo','data_registro']

class RegistroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Registro
        fields = ['id', 'estacao', 'data','hora','temp_min','temp_max','temp_media','umidade_min','umidade_max','umidade_media',
    'vm_min','vm_max','vm_media','pressao_min','pressao_max','pressao_media','direcao','w_m2','uv','mm_ciclo','data_registro']
        
   
