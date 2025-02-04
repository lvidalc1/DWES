from django.urls import path
from appProyectoServidor import views

urlpatterns = [
    # --- Usuarios ---
    # Endpoint para listar usuarios
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    # Endpoint para crear un usuario
    path('usuarios/crear/', views.crear_usuario, name='crear_usuario'),
    # Endpoint para actualizar un usuario
    #path('usuarios/<int:usuario_id>/', views.actualizar_usuario, name='actualizar_usuario'),
    # Endpoint para eliminar un usuario
    #path('usuarios/<int:usuario_id>/eliminar/', views.eliminar_usuario, name='eliminar_usuario'),

    # --- Eventos ---
    # Endpoint para listar eventos
    path('eventos/', views.listar_eventos, name='listar_eventos'),
    # Endpoint para crear un evento
    path('eventos/crear/', views.crear_evento, name='crear_evento'),
    # Endpoint para actualizar un evento
    #path('eventos/<int:evento_id>/', views.actualizar_evento, name='actualizar_evento'),
    # Endpoint para eliminar un evento
    #path('eventos/<int:evento_id>/eliminar/', views.eliminar_evento, name='eliminar_evento'),

    # --- Reservas ---
    # Endpoint para listar reservas
    path('reservas/', views.listar_reservas, name='listar_reservas'),
    # Endpoint para crear una reserva
    path('reservas/crear/', views.crear_reserva, name='crear_reserva'),
    # Endpoint para actualizar una reserva
    #path('reservas/<int:reserva_id>/', views.actualizar_reserva, name='actualizar_reserva'),
    # Endpoint para eliminar una reserva
    #path('reservas/<int:reserva_id>/eliminar/', views.eliminar_reserva, name='eliminar_reserva'),

    # --- Comentarios ---
    # Endpoint para listar comentarios
    path('comentarios/', views.listar_comentarios, name='listar_comentarios'),
    # Endpoint para crear un comentario
    path('comentarios/crear/', views.crear_comentario, name='crear_comentario'),
    # Endpoint para actualizar un comentario
    #path('comentarios/<int:comentario_id>/', views.actualizar_comentario, name='actualizar_comentario'),
    # Endpoint para eliminar un comentario
    #path('comentarios/<int:comentario_id>/eliminar/', views.eliminar_comentario, name='eliminar_comentario'),
]