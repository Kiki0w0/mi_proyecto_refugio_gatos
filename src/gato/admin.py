from django.contrib import admin

from gato.models import Categoria, Gato, SolicitudAdopcion

admin.site.register(Categoria)


@admin.register(Gato)
class GatoAdmin(admin.ModelAdmin):
    list_display = ("categoria", "nombre", "edad", "sexo", "descripcion", "disponibilidad")
    list_filter = ("categoria","sexo")
    search_fields = ("nombre", "categoria__nombre")

admin.site.register(SolicitudAdopcion)
