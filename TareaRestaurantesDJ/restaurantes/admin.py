from django.contrib import admin

# Aqui se registran los modelos creados
from restaurantes.models import Restaurante

admin.site.register(Restaurante)