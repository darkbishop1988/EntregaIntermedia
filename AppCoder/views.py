from django.shortcuts import render

from django.http import HttpResponse

from AppCoder.models import Adopcion
from django.core import serializers
from AppCoder.forms import AdopcionFormulario


def inicio(request):
    return render(request,'AppCoder/inicio.html')


def adopcionApi(request):
    Adopcion_todos =Adopcion.objects.all()
    return HttpResponse(serializers.serialize('json', Adopcion_todos))


def buscaradopcion(request):
    return render( request, 'AppCoder/busquedaAdopcion.html')

def buscar(request):
    codigo = request.GET['nombre_de_Mascota']
    mascotas_todas = Adopcion.objects.filter(nombre_de_Mascota=codigo)
    #return HttpResponse (f'Esta es la linea {codigo} que tiene estos destinos:')
    return render(request, 'AppCoder/resultadosAdopcion.html', {"Adopcion":codigo, "nombre_de_Mascota":mascotas_todas})


def Adopciones (request):
    if request.method == "POST":
            miFormulario = AdopcionFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                informacion = miFormulario.cleaned_data
                  #informacion = {"curso":"12313", "camada": 1223, "numero_dia":1}
                Adop = Adopcion(nombre_de_Mascota=informacion["nombre_de_Mascota"], edad=informacion["edad"], 
                genero=informacion["genero"], mail=informacion["mail"], tipo=informacion["tipo"],
                    castracion=informacion["castracion"], nombre_del_Tutelar=informacion["nombre_del_Tutelar"], 
                    telefono=informacion["telefono"])
                Adop.save()
                return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = AdopcionFormulario()
 
    return render(request, "AppCoder/Adopcion.html", {"miFormulario": miFormulario})

def Provisorios(request):
    return HttpResponse('Vista de Provisorios')

def Encontrados(request):
    return HttpResponse('Vista de Encontrados')

