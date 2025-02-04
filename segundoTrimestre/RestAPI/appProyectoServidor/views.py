from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Usuario, Evento, Reserva, Comentario

# --- Eventos ---
def listar_eventos(request):
    eventos = Evento.objects.all()
    data = [{"id": e.id, "titulo": e.titulo, "descripcion": e.descripcion, "fecha_hora": e.fecha_hora,
             "capacidad": e.capacidad, "imagen_url": e.imagen_url, "pelicula": e.pelicula,
             "organizador": e.organizador.username} for e in eventos]
    return JsonResponse(data, safe=False)


# --- Reservas ---
def listar_reservas(request):
    # Obtener el usuario_id desde los parámetros de la query string (opcional)
    usuario_id = request.GET.get('usuario_id')

    # Si no se proporciona usuario_id, devolver todas las reservas
    if not usuario_id:
        reservas = Reserva.objects.all()  # Devuelve todas las reservas
    else:
        # Intentar obtener el usuario correspondiente al usuario_id proporcionado
        try:
            usuario = Usuario.objects.get(id=usuario_id)
            reservas = Reserva.objects.filter(usuario=usuario)
        except Usuario.DoesNotExist:
            return JsonResponse({"error": "Usuario no encontrado."}, status=400)

    # Preparar la respuesta con las reservas del usuario (o todas si no se proporcionó usuario_id)
    data = [{"id": r.id, "evento": r.evento.id, "entradas": r.entradas, "estado": r.estado} for r in reservas]

    return JsonResponse(data, safe=False)


# --- Comentarios ---
def listar_comentarios(request):
    # Obtener el evento_id desde los parámetros de la query string
    evento_id = request.GET.get('evento_id')

    if evento_id:  # Si se proporciona evento_id, filtrar por evento
        try:
            evento = Evento.objects.get(id=evento_id)
        except Evento.DoesNotExist:
            return JsonResponse({"error": "Evento no encontrado."}, status=404)

        comentarios = Comentario.objects.filter(evento=evento)
    else:  # Si no se proporciona evento_id, devolver todos los comentarios
        comentarios = Comentario.objects.all()

    # Si no hay comentarios, se puede devolver un mensaje vacío
    if not comentarios.exists():
        return JsonResponse({"mensaje": "No hay comentarios disponibles."}, status=200)

    # Preparar la respuesta con los comentarios
    data = [{"id": c.id, "usuario": c.usuario.username, "texto": c.texto, "fecha": c.fecha_creacion} for c in comentarios]


    return JsonResponse(data, safe=False)


@csrf_exempt
def crear_evento(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            titulo = data.get("titulo")
            descripcion = data.get("descripcion")
            fecha_hora = data.get("fecha_hora")
            capacidad = data.get("capacidad")
            pelicula = data.get("pelicula")
            organizador_id = data.get("organizador_id")

            if not all([titulo, descripcion, fecha_hora, capacidad, pelicula, organizador_id]):
                return JsonResponse({"error": "Faltan datos para crear el evento."}, status=400)

            try:
                organizador = Usuario.objects.get(id=organizador_id)
            except Usuario.DoesNotExist:
                return JsonResponse({"error": "El organizador no existe."}, status=400)

            evento = Evento.objects.create(
                titulo=titulo,
                descripcion=descripcion,
                fecha_hora=fecha_hora,
                capacidad=capacidad,
                pelicula=pelicula,
                organizador=organizador
            )

            return JsonResponse({"id": evento.id, "mensaje": "Evento creado exitosamente."}, status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def crear_reserva(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            usuario_id = data.get("usuario_id")
            evento_id = data.get("evento_id")
            entradas = data.get("entradas")

            if not all([usuario_id, evento_id, entradas]):
                return JsonResponse({"error": "Faltan datos para crear la reserva."}, status=400)

            try:
                usuario = Usuario.objects.get(id=usuario_id)
                evento = Evento.objects.get(id=evento_id)
            except (Usuario.DoesNotExist, Evento.DoesNotExist):
                return JsonResponse({"error": "Usuario o evento no encontrado."}, status=400)

            reserva = Reserva.objects.create(
                usuario=usuario,
                evento=evento,
                entradas=entradas,
            )

            return JsonResponse({"id": reserva.id, "mensaje": "Reserva creada exitosamente."}, status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def crear_comentario(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            usuario_id = data.get("usuario_id")
            evento_id = data.get("evento_id")
            texto = data.get("texto")

            if not all([usuario_id, evento_id, texto]):
                return JsonResponse({"error": "Faltan datos para crear el comentario."}, status=400)

            try:
                usuario = Usuario.objects.get(id=usuario_id)
                evento = Evento.objects.get(id=evento_id)
            except (Usuario.DoesNotExist, Evento.DoesNotExist):
                return JsonResponse({"error": "Usuario o evento no encontrado."}, status=400)

            comentario = Comentario.objects.create(
                usuario=usuario,
                evento=evento,
                texto=texto
            )

            return JsonResponse({"id": comentario.id, "mensaje": "Comentario creado exitosamente."}, status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def login_usuario(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Método no permitido. Usa POST.'}, status=405)

    try:
        datos = json.loads(request.body.decode('utf-8'))

        username = datos.get('username')
        password = datos.get('password')

        if not username or not password:
            return JsonResponse({'error': 'Los campos "username" y "password" son obligatorios.'}, status=400)

        try:
            usuario = Usuario.objects.get(username=username)
        except Usuario.DoesNotExist:
            return JsonResponse({'error': 'Credenciales inválidas. Usuario no encontrado.'}, status=401)

        return JsonResponse({
            'mensaje': 'Inicio de sesión exitoso.',
            'usuario': {
                'id': usuario.id,
                'username': usuario.username,
                'rol': usuario.rol,
            }
        }, status=200)

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Formato de JSON inválido.'}, status=400)
    except Exception as e:
        return JsonResponse({'error': f'Error inesperado: {str(e)}'}, status=500)


@csrf_exempt
def registrar_usuario(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Método no permitido. Usa POST.'}, status=405)

    try:
        datos = json.loads(request.body.decode('utf-8'))

        username = datos.get('username')
        password = datos.get('password')
        rol = datos.get('rol', 'participante')
        biografia = datos.get('biografia', '')

        if not username or not password:
            return JsonResponse({'error': 'Los campos "username" y "password" son obligatorios.'}, status=400)

        if not str(password).isdigit():
            return JsonResponse({'error': 'La contraseña debe contener únicamente números.'}, status=400)

        if Usuario.objects.filter(username=username).exists():
            return JsonResponse({'error': 'El username ya está en uso. Elige otro.'}, status=409)

        nuevo_usuario = Usuario(
            username=username,
            rol=rol,
            biografia=biografia
        )

        nuevo_usuario.set_password(str(password))
        nuevo_usuario.save()

        return JsonResponse({
            'mensaje': 'Usuario registrado exitosamente.',
            'usuario': {
                'id': nuevo_usuario.id,
                'username': nuevo_usuario.username,
                'rol': nuevo_usuario.rol,
                'biografia': nuevo_usuario.biografia
            }
        }, status=201)

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Formato de JSON inválido.'}, status=400)
    except Exception as e:
        return JsonResponse({'error': f'Error inesperado: {str(e)}'}, status=500)
