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
        fields = ['id', 'sensor', 'temperatura', 'pressao','altitude','pressa_nivel_mar','altitude_real','data_registro']

class RegistroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Registro
        fields = ['id', 'sensor', 'temperatura', 'pressao','altitude','pressa_nivel_mar','altitude_real','data_registro']
        
    def validate(self, data):
        if temperarura_valida(data['temperatura']):
            raise serializers.ValidationError({'temperatura':"A temperatura precisa ter um valor numérico"})
        if not temperarura_tamanho(data['temperatura']):
            raise serializers.ValidationError({'temperatura':"A temperatura precisa ter um valor no máximo 5 dígitos"})   
        if pressao_valida(data['pressao']):
            raise serializers.ValidationError({'pressao':"A pressão precisa ter um valor numérico"})
        if altitude_valida(data['altitude']):
            raise serializers.ValidationError({'altitude':"A altiude precisa ter um valor numérico"})
        if pressao_nivel_valida(data['pressa_nivel_mar']):
            raise serializers.ValidationError({'pressa_nivel_mar':"A Pressão a nível do mar precisa ter um valor numérico"})
        if altidude_real_valida(data['altitude_real']):
            raise serializers.ValidationError({'altitude_real':"A Altidude real precisa ter um valor numérico"})
        
        return data
