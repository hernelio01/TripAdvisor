from django.db import models

# Create your models here.


# modelo de la tabla domicilio
class Domicilio(models.Model):
  calle = models.IntegerField()
  no_calle = models.CharField(max_length=255)
  pais = models.CharField(max_length=255)
    # sobre escribir el metodo str para visualizar los datos en consola

  def __str__(self):
    return f'Domicilio {self.id}: {self.calle}{self.no_calle}{self.pais}'



class Persona(models.Model):  
  nombre = models.CharField(max_length=255)
  apellido = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  #Relación  entre tablas, cuando se borre un dato asociado a persona poner null en el registro de persona
  domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)

  # sobre escribir el metodo str para visualizar los datos en consola
  def __str__(self):
    return f'Persona {self.id}: {self.nombre}{self.apellido}{self.email} {self.domicilio}'
   


