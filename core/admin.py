from django.contrib import admin
from .models import (
    Marca, 
    Veiculo, 
    Pessoa, 
    Parametros, 
    MovRotativo,
    Mensalista,
    MovMensalista
)

class MovRotativoAdmin(admin.ModelAdmin):
    list_display = ('checkin', 'checkout', 'valor_hora', 'pago', 'total', 'horas_total', 'veiculo')

    # Just to get object "MovRotativo" and your "veiculo" (Don't need, but i will left here as exemple)
    #def veiculo(self, obj):
    #    return obj.veiculo

class MovMensalistaAdmin(admin.ModelAdmin):
    list_display = ('mensalista', 'dt_pgto', 'total')


admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
admin.site.register(Parametros)
admin.site.register(Mensalista)
admin.site.register(MovMensalista, MovMensalistaAdmin)
admin.site.register(MovRotativo, MovRotativoAdmin)

# Register your models here.
