from socket import fromshare
from django import forms

class CursoFormulario(forms.Form):

    curso = forms.CharField()
    camada =forms.IntegerField()