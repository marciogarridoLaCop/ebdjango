from django.contrib import admin
from django.urls import path,include
from DataLogSensor.views import RegistroViewSet,ListaRegistro
from Device.views import TipoViewSet,SensorViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tipo', TipoViewSet, basename='Tipo')
router.register('sensor', SensorViewSet, basename='Sensor')
router.register('datalogsensor', RegistroViewSet, basename='Registro')
                         



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
    path('sensorespecifico/<int:pk>/', ListaRegistro.as_view()),
]