from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Usuario, Evento, Reserva, Comentario


# GET: Listar todos los usuarios disponibles
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    data = [{"id": u.id, "username": u.username, "email": u.email, "biografia": u.biografia, "rol": u.rol} for u in usuarios]
    return JsonResponse(data, safe=False)


# GET: Listar todos los eventos disponibles
def listar_eventos(request):
    eventos = Evento.objects.all()
    data = [{"id": e.id, "titulo": e.titulo, "descripcion": e.descripcion, "fecha_hora": e.fecha_hora,
             "capacidad": e.capacidad, "imagen_url": e.imagen_url, "pelicula": e.pelicula,
             "organizador": e.organizador.username} for e in eventos]
    return JsonResponse(data, safe=False)


# GET: Listar todas las reservas disponibles
def listar_reservas(request):
    reservas = Reserva.objects.all()
    data = [{"id": r.id, "usuario": r.usuario.username, "evento": r.evento.id,
             "entradas": r.entradas, "estado": r.estado} for r in reservas]
    return JsonResponse(data, safe=False)


# GET: Listar todos los comentarios disponibles
def listar_comentarios(request):
    comentarios = Comentario.objects.all()
    data = [{"id": c.id, "usuario": c.usuario.username, "evento": c.evento.id,
             "texto": c.texto, "fecha_creacion": c.fecha_creacion} for c in comentarios]
    return JsonResponse(data, safe=False)


@csrf_exempt
def crear_usuario(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get("username")
            email = data.get("email")
            biografia = data.get("biografia", "")
            rol = data.get("rol")

            if not all([username, email, rol]):
                return JsonResponse({"error": "Faltan datos para crear el usuario."}, status=400)

            if rol not in ['organizador', 'participante']:
                return JsonResponse({"error": "Rol no válido."}, status=400)

            usuario = Usuario.objects.create_user(
                username=username,
                email=email,
                biografia=biografia,
                rol=rol
            )

            return JsonResponse({"id": usuario.id, "mensaje": "Usuario creado exitosamente."}, status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)


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
            organizador_id = data.get("organizador_id")  # Se recibe el ID del organizador

            if not all([titulo, descripcion, fecha_hora, capacidad, pelicula, organizador_id]):
                return JsonResponse({"error": "Faltan datos para crear el evento."}, status=400)

            # Buscar al organizador en la base de datos
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

            # Validar si los IDs existen
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

            # Validar si los IDs existen
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
