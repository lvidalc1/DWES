from django.urls import path
from appProyectoServidor import views

urlpatterns = [
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

    # --- Usuarios (opcional, si decides agregar rutas más tarde) ---
    # Endpoint para login
    path('usuarios/login/', views.login_usuario, name='login_usuario'),
    # Endpoint para registro
    path('usuarios/registrar/', views.registrar_usuario, name='registrar_usuario'),
]
