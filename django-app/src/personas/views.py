from personas.models import Persona
from personas.forms import PersonaForm
from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory

# Create your views here.
def detallePersona(request, id):
    #persona_var = Persona.objects.get(pk=id)
    # metodo para validar el id de la persona y retonar no encontrado; en una variable se almacena la función
     # get_object_or_404, tipo de objeto y laave id
    persona_var = get_object_or_404(Persona, pk=id)
    return render(request, 'personas/detalle.html', {'persona': persona_var})

# variable co instacia del formulario modelo, SE VAN A MOSTRAR TODOS LOS CAMPOS
   #PersonaForm = modelform_factory(Persona, exclude=[])

#otra manera de crear un objeto



def nuevaPersona(request):
    #vallidación: si el objeto request en su atributo de metodo se envío info de tipo POST se debe procesar el formulario
     # de lo contrario es la primera vez que se hace petición a la pagina y por lo tanto se deve de crear un formulario tipo form
      # y ahcer el render hacia l pagina de nuevo.html
    if request.method == 'POST':
        # crear un onjet de tipo persona pero con información del formulario
        formaPersona = PersonaForm(request.POST)
        #validación de formulario con django
        if formaPersona.is_valid():
        #luego se almacena en base de datos
            formaPersona.save()
            return redirect('index')
        # si no es valido se redirige hacia la misma pagina 
        else: 
            return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})   
    else:     
        #calse de django para crear un nuevo objetio delformulario con respecto al modelo
        formaPersona = PersonaForm()
        # retornar el template html
        return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})


def editarPersona(request, id):
    #vallidación: si el objeto request en su atributo de metodo se envío info de tipo POST se debe procesar el formulario
     # de lo contrario es la primera vez que se hace petición a la pagina y por lo tanto se deve de crear un formulario tipo form
      # y ahcer el render hacia l pagina de nuevo.html
    persona_var = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':
        # crear un onjet de tipo persona pero con información del formulario
        formaPersona = PersonaForm(request.POST, instance=persona_var)
        #validación de formulario con django
        if formaPersona.is_valid():
        #luego se almacena en base de datos
            formaPersona.save()
            return redirect('index')
        # si no es valido se redirige hacia la misma pagina 
        #recuperar el objeto persona que queremos editas
        else: 
            return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})   
    else:     
        #calse de django para crear un nuevo objetio delformulario con respecto al modelo
        
       # return render(request, 'personas/detalle.html', {'persona': persona_var})
        formaPersona = PersonaForm(instance=persona_var)
        # retornar el template html
        return render(request, 'personas/editar.html', {'formaPersona': formaPersona})


def eliminarPersona(request, id):
    #vallidación: si el objeto request en su atributo de metodo se envío info de tipo POST se debe procesar el formulario
     # de lo contrario es la primera vez que se hace petición a la pagina y por lo tanto se deve de crear un formulario tipo form
      # y ahcer el render hacia l pagina de nuevo.html
    persona_var = get_object_or_404(Persona, pk=id)
    if persona_var:
        persona_var.delete()
    return redirect ('index')
    