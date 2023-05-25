
#from django.http import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render
from  personas.models import Persona

# Create your views here.

def bienvenido (request):
    # mensajes para mostar templates como contenido dínamico en la vista, se crea un diccionario
    #mensajes = {'msg1':'valor mensaje 1'}
    #pasamos variable del diccionario en return
    #return render (request, 'bienvenido.html', mensajes)
    # utilizar la case de modelo de personas, concepto de manejador object, para este caso función que cuenta registros
    no_personas_var = Persona.objects.count()
    #recuperar listado de todas las personas DEL TIPO MODELO
    #personas_var = Persona.objects.all()
    personas_var = Persona.objects.order_by('-id', 'nombre')
    return render (request, 'bienvenido.html', {'no_personas':no_personas_var, 'personas': personas_var})