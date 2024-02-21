from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from .models import Lote, Recinto, Estado_De_Aprobacion

# poner las preguntas en el orden margen, lote propietario ydatos

class Lote_Form(forms.ModelForm):
    class Meta:
        model = Lote
        fields = ['margen', 'lote', 'propietario', 'volfirme']
       

class Recinto_Form(forms.ModelForm):
    class Meta:
        model = Recinto
        fields = ['lote', 'nombre', 'margen', 'capacidad']


class Estado_De_Aprobacion_Form(forms.Form):
    # Definir opciones para el campo estado
    ESTADO_CHOICES = [('',''),
        ('Firmada', 'Firmada'),
        ('DPH', 'DPH'),
        ('Tratativas', 'Tratativas'),
    ]
    
    # Definir los campos del formulario
    lote = forms.ModelChoiceField(queryset=Lote.objects.all(),  empty_label=None, to_field_name="lote", widget=forms.Select(attrs={'class': 'form-control'}),required=True) #quiero que sea una lista despegable de los que ya existen
    puntuacion = forms.FloatField(min_value=0,max_value=5,required=True) 
    actualizacion = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),required=True)
    estado = forms.ChoiceField(choices=ESTADO_CHOICES,required=True)
    denominacion = forms.CharField(label="Nombre",required=False)
    capacidad = forms.CharField(label="Nombre",required=False)






class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    dni = forms.CharField(label="DNI")  # Cambié 'usuario' a 'username'
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'dni', 'password1', 'password2']
        help_texts = {k: "" for k in fields}

        
class UserEditForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    dni = forms.CharField(label="DNI")  # Cambié 'usuario' a 'username'
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'dni', 'password1', 'password2']
        help_texts = {k: "" for k in fields}