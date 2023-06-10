from django.contrib import admin
from DataLogSensor.models import Registro

class Dados(admin.ModelAdmin):
    list_display = fields = ('id', 'estacao', 'data','hora','temp_min','temp_max','temp_media','umidade_min','umidade_max','umidade_media',
    'vm_min','vm_max','vm_media','pressao_min','pressao_max','pressao_media','direcao','w_m2','uv','mm_ciclo','data_registro')
    list_display_links = ('id', 'estacao')
    search_fields = ('estacao',)
    list_per_page = 50
    ordering =('data_registro',)

admin.site.register(Registro,Dados)
