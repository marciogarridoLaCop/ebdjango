from django.contrib import admin
from Device.models import Tipo,Sensor

class Tipos(admin.ModelAdmin):
    list_display = ('id','nome')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20
admin.site.register(Tipo,Tipos)


class Sensores(admin.ModelAdmin):
    list_display = ('id','sensor','local','observacao')
    list_display_links = ('id', 'sensor')
    search_fields = ('sensor',)
    list_per_page = 20

admin.site.register(Sensor,Sensores)