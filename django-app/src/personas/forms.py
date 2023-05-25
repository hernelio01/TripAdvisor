
from personas.models import Persona
from  django.forms import  ModelForm, EmailInput


#importación ddel modelo Persona

    

#definicion de la clase PersonForm que se extiende de la clase ModelForm

class PersonaForm(ModelForm):
    #personalización de los atributos del formulario
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'email':EmailInput(attrs={'type':'email'})
        }