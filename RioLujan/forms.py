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


class Estado_De_Aprobacion_Form(forms.ModelForm):
    class Meta:
        model = Estado_De_Aprobacion
        fields = ['lote', 'actualizacion', 'estado', 'denominacion', 'capacidad']
        labels = {
            'lote': 'Lote - Parcela',
            'actualizacion': 'Fecha de Actualizacion',
            'estado': 'Estado',
            'denominacion': 'Denominacion',
            'capacidad': 'Capacidad'
        }
        widgets = {
            'actualizacion': forms.DateInput(attrs={'type': 'date'}),
            'estado': forms.Select(choices=[('Firmada', 'Firmada'), ('DPH', 'DPH'), ('Tratativas', 'Tratativas')]),
            'lote': forms.Select(choices=[(lote.id, lote.lote) for lote in Lote.objects.all()])
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.required = True






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