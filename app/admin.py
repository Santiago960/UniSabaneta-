from django.contrib import admin

from .models import (
    Materia,
    Ingles,
    Horario,
    Perfil
)


# MATERIAS
class MateriaAdmin(admin.ModelAdmin):

    list_display = (
        'nombre',
        'semestre',
        'creditos'
    )

    search_fields = (
        'nombre',
    )

    list_filter = (
        'semestre',
    )


# INGLES
class InglesAdmin(admin.ModelAdmin):

    list_display = (
        'nivel',
        'descripcion'
    )

    search_fields = (
        'nivel',
    )


# HORARIOS
class HorarioAdmin(admin.ModelAdmin):

    list_display = (
        'materia',
        'profesor',
        'salon',
        'hora'
    )

    search_fields = (
        'materia',
        'profesor'
    )


# PERFIL
class PerfilAdmin(admin.ModelAdmin):

    list_display = (
        'usuario',
        'nombre_completo'
    )

    search_fields = (
        'usuario__username',
        'nombre_completo'
    )


# REGISTROS
admin.site.register(Materia, MateriaAdmin)

admin.site.register(Ingles, InglesAdmin)

admin.site.register(Horario, HorarioAdmin)

admin.site.register(Perfil, PerfilAdmin)


# PERSONALIZACIÓN ADMIN
admin.site.site_header = "Administración UniSabaneta"

admin.site.site_title = "UniSabaneta"

admin.site.index_title = "Panel Administrativo Universitario"

admin.site.empty_value_display = "Sin información"