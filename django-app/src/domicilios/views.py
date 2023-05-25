from django.shortcuts import render

# Create your views here.

from personas.models import Domicilio
from domicilios.forms import DomicilioForm
from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory

# Create your views here.
def detalleDomicilio(request, id):
    #persona_var = Persona.objects.get(pk=id)
    # metodo para validar el id de la persona y retonar no encontrado; en una variable se almacena la función
     # get_object_or_404, tipo de objeto y laave id
    domicilio_var = get_object_or_404(Domicilio, pk=id)
    return render(request, 'domicilios/detalle.html', {'domicilio': domicilio_var})

# variable co instacia del formulario modelo, SE VAN A MOSTRAR TODOS LOS CAMPOS
   #PersonaForm = modelform_factory(Persona, exclude=[])

#otra manera de crear un objeto



def nuevoDomicilio(request):
    #vallidación: si el objeto request en su atributo de metodo se envío info de tipo POST se debe procesar el formulario
     # de lo contrario es la primera vez que se hace petición a la pagina y por lo tanto se deve de crear un formulario tipo form
      # y ahcer el render hacia l pagina de nuevo.html
    if request.method == 'POST':
        # crear un onjet de tipo persona pero con información del formulario
        formaDomicilio = DomicilioForm(request.POST)
        #validación de formulario con django
        if formaDomicilio.is_valid():
        #luego se almacena en base de datos
            formaDomicilio.save()
            return redirect('index')
        # si no es valido se redirige hacia la misma pagina 
        else: 
            return render(request, 'domicilios/nuevo.html', {'formaDomicilio': formaDomicilio})   
    else:     
        #calse de django para crear un nuevo objetio delformulario con respecto al modelo
        formaDomicilio = DomicilioForm()
        # retornar el template html
        return render(request, 'domicilios/nuevo.html', {'formaDomicilio': formaDomicilio})


def editarDomicilio(request, id):
    #vallidación: si el objeto request en su atributo de metodo se envío info de tipo POST se debe procesar el formulario
     # de lo contrario es la primera vez que se hace petición a la pagina y por lo tanto se deve de crear un formulario tipo form
      # y ahcer el render hacia l pagina de nuevo.html
    domicilio_var = get_object_or_404(Domicilio, pk=id)
    if request.method == 'POST':
        # crear un onjet de tipo persona pero con información del formulario
        formaDomicilio= DomicilioForm(request.POST, instance=domicilio_var)
        #validación de formulario con django
        if formaDomicilio.is_valid():
        #luego se almacena en base de datos
            formaDomicilio.save()
            return redirect('index')
        # si no es valido se redirige hacia la misma pagina 
        #recuperar el objeto persona que queremos editas
        else: 
            return render(request, 'domicilios/nuevo.html', {'formaDomicilio': formaDomicilio})   
    else:     
        #calse de django para crear un nuevo objetio delformulario con respecto al modelo
        
       # return render(request, 'personas/detalle.html', {'persona': persona_var})
        formaDomicilio = DomicilioForm(instance=domicilio_var)
        # retornar el template html
        return render(request, 'domicilios/editar.html', {'formaDomicilio': formaDomicilio})


def eliminarDomicilio(request, id):
    #vallidación: si el objeto request en su atributo de metodo se envío info de tipo POST se debe procesar el formulario
     # de lo contrario es la primera vez que se hace petición a la pagina y por lo tanto se deve de crear un formulario tipo form
      # y ahcer el render hacia l pagina de nuevo.html
    domicilio_var = get_object_or_404(Domicilio, pk=id)
    if domicilio_var:
        domicilio_var.delete()
    return redirect ('index')
    