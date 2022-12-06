from django.urls import path
from AppCoder import views

urlpatterns = [
    path("", views.inicio, name="Inicio"),
    path("Adopciones/", views.Adopciones,name="Adopciones"),
    path("adopcionApi/", views.adopcionApi ), 
    path("Encontrados/", views.Encontrados ),
    path("Provisorio/", views.Provisorios ),
    path("busquedaAdopcion/", views.buscaradopcion, name="Buscar"),
    path("buscar/", views.buscar),

]