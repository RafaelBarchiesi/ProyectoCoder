from django.template import Template, Context, loader
from django.shortcuts import render, loader
from django.http import HttpResponse
from AppCoder.models import Curso, Estudiante, Profesor, Entregables
from AppCoder.forms import CursoFormulario


# Create your views here.

def inicio(request):

    return render(request, "AppCoder/inicio.html")

def curso(request):

    cur1 = Curso(nombre="Desarrollo Web", camada=11111) 
    cur1.save()

    return render(request, "AppCoder/cursos.html")

def ver_estudiante(request):

    estudiante1 = Estudiante(nombre = "Rafael", apellido = "Barchiesi")
    estudiante1.save()

    return render(request, "AppCoder/estudiantes.html")


def ver_profesor(request):

    profe1 = Profesor(nombre = "Pedro", apellido = "Perez", profesion = "Contador")
    profe1.save()

    return render(request, "AppCoder/profesores.html")

def ver_entregables(request):

    return render(request, "AppCoder/entregables.html")

def cursoFormulario(request):

    if request.method == "POST":

        formulario1 = CursoFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            curso = Curso(nombre=info["curso"], camada=info["camada"])
        
            curso.save()

            return render(request, "AppCoder/cursos.html")
        
    else:

        formulario1 = CursoFormulario()

    return render(request, "AppCoder/cursos.html", {"form1": formulario1})


def busquedaCamada(request):

    return render(request, "AppCoder/estudiantes.html")

def resultados(request):

    if request.GET["camada"]:

        camada = request.GET["camada"]
        cursos = Curso.objects.filter(camada__iexact=camada)

        return render(request, "AppCoder/estudiantes.html", {"cursos": cursos, "camada": camada})
    
    else: 

        respuesta = "No enviaste datos"

        return HttpResponse(respuesta)

