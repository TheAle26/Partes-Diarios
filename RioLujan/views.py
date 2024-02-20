from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from RioLujan.models import Estado_De_Aprobacion, Recinto ,Recinto ,Maquinaria , models
from django.http import HttpResponse, HttpResponseBadRequest
import datetime
import RioLujan.forms 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def seleccionar(request):

    return render(request,"RioLujan/seleccionar.html")

def carga_Estado_De_Aprobacion (request):

    if request.method == "POST":
        formulario = RioLujan.forms.Estado_De_Aprobacion_Form(request.POST, request.FILES)

        if formulario.is_valid():
            # Extraemos los datos del formulario
            info = formulario.cleaned_data

            # Creamos una instancia de Estado_De_Aporobacion y asignamos los valores !!!
            Estado_De_Aporobacion_nuevo = Estado_De_Aprobacion(
                restaurante=info["restaurante"],
                puntuacion=info["puntuacion"],
                
                fecha_de_visita=info["fecha_de_visita"],
                fecha_de_Estado_De_Aporobacion = datetime.datetime.now(),
                Estado_De_Aporobacion=info["Estado_De_Aporobacion"],
                foto=info["foto"],
                usuario=request.user,
            )

            # Guardamos la instancia del restaurante
            Estado_De_Aporobacion_nuevo.save()

            # Recargamos la lista de restaurantes después de la creación
          
            return redirect('Estado_De_Aporobacion_otro')
        else:
            mensaje="Formulario no valido"
            formulario = RioLujan .forms.Estado_De_Aprobacion_Form()
            return render(request, "RioLujan /crear_Estado_De_Aporobacion.html", {"form": formulario,'mensaje':mensaje})

    else:
        formulario = RioLujan .forms.Estado_De_Aprobacion_Form()

        return render(request, "RioLujan /crear_Estado_De_Aporobacion.html", {"form": formulario})
    

def Estado_De_Aprobacion_all(request):

    Estados = Estado_De_Aprobacion.objects.all()
    return render(request,"RioLujan/Estado_De_Aprobacion.html",{"Estados":Estados})


def Estado_De_Aporobacion_otro (request):

    return render(request,"RioLujan/Estado_De_Aporobacion_otro.html")

def update_Estado_De_Aprobacion (request, estado_id):


    Estado_De_Aprobacion_update = get_object_or_404(Estado_De_Aprobacion, id=estado_id)

    if request.method == "POST":
        formulario = RioLujan.forms.Estado_De_Aprobacion_Form(request.POST, request.FILES)
        if formulario.is_valid():
            info = formulario.cleaned_data

            Estado_De_Aprobacion_update.lote = info["lote"]
            Estado_De_Aprobacion_update.actualizacion = info["actualizacion"]
            Estado_De_Aprobacion_update.estado = info["estado"]
            Estado_De_Aprobacion_update.denminacion = info["denminacion"]
            Estado_De_Aprobacion_update.capacidad = info["capacidad"]
            

            
            # Recargamos la lista de restaurantes después de la actualizació

            return redirect('Restos')
    else:
        formulario = RioLujan.forms.Estado_De_Aprobacion_Form(initial={
            "nombre": Estado_De_Aprobacion_update.lote,
            "calificacion": Estado_De_Aprobacion_update.actualizacion,
            "descripcion": Estado_De_Aprobacion_update.estado,
            "instagram": Estado_De_Aprobacion_update.denminacion,
            "ubicacion": Estado_De_Aprobacion_update.capacidad, 
        })

    return render(request, "AppResto/update_restaurante.html", {"form": formulario})