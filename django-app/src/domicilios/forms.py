
from personas.models import Domicilio
from  django.forms import  ModelForm 


#importación ddel modelo Persona

    

#definicion de la clase PersonForm que se extiende de la clase ModelForm

class DomicilioForm(ModelForm):
    #personalización de los atributos del formulario
    class Meta:
        model = Domicilio
        fields = '__all__'
        widgets = {
            #'email':EmailInput(attrs={'type':'email'})
        }