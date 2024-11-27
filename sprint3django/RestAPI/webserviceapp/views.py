from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Tlibros

# Create your views here.
def pagina_de_prueba(request):
	return HttpResponse("<h1>Hola caracola</h1>");

def devolver_libros(request):
	lista = Tlibros.objects.all()
	respuesta_final=[]
	for fila_sql in lista:
		diccionario = {}
		diccionario['id']=fila_sql.id
		diccionario['titulo']=fila_sql.nombre
		diccionario['fecha']=fila_sql.año_publicacion
		respuesta_final.append(diccionario)
	return JsonResponse(respuesta_final, safe=False)
