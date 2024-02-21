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


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username= username, password=password)

            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                return render(request, "registro/login.html", {"mensaje":"Datos incorrectos"})
           
        else:
            formulario = AuthenticationForm()
            return render(request, "registro/login.html", {"mensaje":"Formulario erroneo","formulario": formulario})

    formulario = AuthenticationForm()

    return render(request, "registro/login.html", {"formulario": formulario})



# TODO LO DE ESTADO DE APROBACION

def carga_Estado_De_Aprobacion (request):

    if request.method == "POST":
        formulario = RioLujan.forms.Estado_De_Aprobacion_Form(request.POST)

        if formulario.is_valid():
            # Extraemos los datos del formulario
            info = formulario.cleaned_data
         
            # Creamos una instancia de Estado_De_Aporobacion y asignamos los valores !!!
            Estado_De_Aporobacion_nuevo = Estado_De_Aprobacion(
                lote=info["lote"],
                actualizacion=info["actualizacion"],
                estado=info["estado"],
                denominacion = info["denminacion"],
                capacidad=info["capacidad"],
                usuario=request.user
            )

            # Guardamos la instancia del restaurante
            Estado_De_Aporobacion_nuevo.save()

            # Recargamos la lista de restaurantes después de la creación
          
            return redirect('Estado_De_Aporobacion_otro')
        else:
            mensaje="Formulario no valido"
            formulario = RioLujan.forms.Estado_De_Aprobacion_Form()
            return render(request, "RioLujan/carga_Estado_De_Aprobacion.html", {"form": formulario,'mensaje':mensaje})

    else:
        formulario = RioLujan.forms.Estado_De_Aprobacion_Form()

        return render(request, "RioLujan/carga_Estado_De_Aprobacion.html", {"form": formulario})
    

def Estado_De_Aprobacion_all(request):

    estados = Estado_De_Aprobacion.objects.all()
    return render(request,"RioLujan/Estado_De_Aprobacion.html",{"estados":estados})


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
            Estado_De_Aprobacion_update.denominacion = info["denominacion"]
            Estado_De_Aprobacion_update.capacidad = info["capacidad"]
            Estado_De_Aprobacion_update.usuario=request.user

            
            # Recargamos la lista de restaurantes después de la actualizació

            return redirect('Estado_De_Aporobacion')
    else:
        formulario = RioLujan.forms.Estado_De_Aprobacion_Form(initial={
            "lote": Estado_De_Aprobacion_update.lote,
            "actualizacion": Estado_De_Aprobacion_update.actualizacion,
            "estado": Estado_De_Aprobacion_update.estado,
            "denominacion": Estado_De_Aprobacion_update.denominacion,
            "capacidad": Estado_De_Aprobacion_update.capacidad, 
        })

    return render(request, "RioLujan/update_Estado_De_Aprobacion.html", {"form": formulario,'estado':Estado_De_Aprobacion_update})

def delete_Estado_De_Aprobacion(request, estado_id):
     if request.method == "POST":
        estado = get_object_or_404(Estado_De_Aprobacion, id=estado_id)
        estado.delete()

        # Recargar la lista de reseñas después de la eliminación
        estados = Estado_De_Aprobacion.objects.all()
        return redirect('Estado_De_Aprobacion')
     else :
          return render(request, "RioLujan/delete_Estado_De_Aprobacion.html")
     

