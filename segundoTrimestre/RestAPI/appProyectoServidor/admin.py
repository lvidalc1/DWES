from django.contrib import admin

from django.contrib import admin
from .models import Usuario, Evento, Reserva, Comentario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo_electronico', 'rol')
    search_fields = ('nombre', 'correo_electronico')

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descripcion', 'fecha_hora', 'capacidad', 'organizador')
    list_filter = ('fecha_hora', 'organizador')
    search_fields = ('titulo', 'descripcion')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'evento', 'entradas', 'estado')
    list_filter = ('estado',)
    search_fields = ('usuario__nombre', 'evento__titulo')

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'evento', 'fecha_creacion', 'texto')
    search_fields = ('usuario__nombre', 'evento__titulo')

