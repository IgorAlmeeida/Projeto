from django.contrib import admin
from .models import Veiculo, Pessoa, Marca, Parametros


admin.site.register(Pessoa)
admin.site.register(Veiculo)
admin.site.register(Marca)
admin.site.register(Parametros)


# Register your models here.
