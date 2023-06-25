from django.urls import path
from restaurantes import views

urlpatterns = [
        path('', views.listadoRestaurantes, name='listadoRestaurantes'),
 ]