from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppCoder.models import Avatar

class CursoFormulario(forms.Form):

    nombre = forms.CharField()
    camada =forms.IntegerField()
    comision = forms.IntegerField()


class EstudianteFormulario(forms.Form):

    nombre = forms.CharField(max_length=60)
    apellido = forms.CharField(max_length=60)
    correo = forms.EmailField()

class ProfesorFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion =forms.CharField()
    edad = forms.IntegerField()


class EntregablesFormulario(forms.Form):

    nombre = forms.CharField(max_length=60)
    fechaEntrega = forms.DateField()
    entregado = forms.BooleanField()

class UsuarioRegistro(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseñan", widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir la contrasñena", widget = forms.PasswordInput)

    class Meta:

        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]

class FormularioEditar(UserCreationForm):
    
    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseñan", widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir la contrasñena", widget = forms.PasswordInput)

    class Meta:

        model = User
        fields = ["email", "first_name", "last_name", "password1", "password2"]

class AvatarFormulario(forms.ModelForm):

    class Meta:

        model = Avatar
        fields = ["imagen"]