from django.shortcuts import render

#  Aqui se crea los views.
from restaurantes.models import Restaurante

def listadoRestaurantes(request):

   listado = Restaurante.objects.all()
   informacion ={"listadoRestaurantes":listado}
   return render(request, "restaurantesListado.html", informacion)