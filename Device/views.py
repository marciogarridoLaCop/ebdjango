from rest_framework import viewsets
from Device.models import Tipo,Sensor
from Device.serializer import TipoSerializer,SensorSerializer


class TipoViewSet(viewsets.ModelViewSet):
    """Exibindo todos tipos de sensores"""
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer

class SensorViewSet(viewsets.ModelViewSet):
    """Exibindo todos os sensores cadastrados"""
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer