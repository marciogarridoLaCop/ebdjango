from django.contrib import admin
from DataLogSensor.models import Registro

class Dados(admin.ModelAdmin):
    list_display = fields = ('id', 'sensor', 'date','time','mm_h','mm_dia','temp','umidade','pressao','vmed','vmax','direcao','uv','w_m2','data_registro')
    list_display_links = ('id', 'sensor')
    search_fields = ('sensor',)
    list_per_page = 100
    ordering =('data_registro',)

admin.site.register(Registro,Dados)
