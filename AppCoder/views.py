from django.template import Template, Context, loader
from django.shortcuts import render, loader
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

#Usuario

def InicioSesion(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contra)

            if user:

                login(request, user)

                return render(request, "AppCoder/inicio.html", {"mensaje":f"Bienvenido {user}"})
            
        else:

            return render(request, "AppCoder/inicio.html", {"mensaje":f"Los datos son incorrectos"})

    else:

        form = AuthenticationForm()


    return render(request, "AppCoder/login.html", {"formulario": form})    



def registro(request):

    if request.method == "POST":

        form = UsuarioRegistro(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            form.save()
            return render(request, "AppCoder/inicio.html", {"mensaje": "Usuario creado."})

    else:

        form = UsuarioRegistro()

    return render(request, "AppCoder/registro.html", {"formulario": form})

@login_required
def editarUsuario(request):

    usuario = request.user

    if request.method == "POST":

        form = FormularioEditar(request.POST)

        if form.is_valid():

            info = form.cleaned_data

            usuario.email = info["email"]
            usuario.set_password(info["password1"])
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]

            usuario.save()

            return render(request, "/AppCoder/inicio.html")

    else:

        form = FormularioEditar(initial={    

            "email":usuario.email,
            "first_name":usuario.first_name,
            "last_name":usuario.last_name,

            })

    return render(request, "AppCoder/editarPerfil.html", {"formulario": form, "usuario": usuario})



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


#función para crear curso
def crear_curso(request): #Creando usando forms de Django

    if request.method == 'POST': #click al botón enviar: guardar los datos y crearse el curso

        miFormulario = CursoFormulario(request.POST)

        if miFormulario.is_valid(): #validar que los datos esten ok
            
            infoDict = miFormulario.cleaned_data #la info del formulario se pasa a tipi diccionario
            
            curso1 = Curso(nombre = infoDict["nombre"], camada = infoDict["camada"], comision = infoDict["comision"])

            curso1.save()

            return render(request, "AppCoder/inicio.html")            
    
    else: #si todavía no le doy click

        miFormulario = CursoFormulario()

    return render(request, "AppCoder/crearCurso.html", {"formulario1":miFormulario})



#Función para crear estudiantes
def crear_estudiantes(request): #Creando usando forms de Django

    if request.method == 'POST': #click al botón enviar: guardar los datos y crearse el curso

        miFormulario = EstudianteFormulario(request.POST)

        if miFormulario.is_valid(): #validar que los datos esten ok
            
            infoDict = miFormulario.cleaned_data #la info del formulario se pasa a tipi diccionario
            
            estudiante1 = Estudiante(nombre = infoDict["nombre"], apellido = infoDict["apellido"], correo = infoDict["correo"])

            estudiante1.save()

            return render(request, "AppCoder/inicio.html")            
    
    else: #si todavía no le doy click

        miFormulario = EstudianteFormulario()

    return render(request, "AppCoder/crearEstudiante.html", {"formulario1":miFormulario})



#Función para crear entregables
def crear_entregables(request): #Creando usando forms de Django

    if request.method == 'POST': #click al botón enviar: guardar los datos y crearse el curso

        miFormulario = EntregablesFormulario(request.POST)

        if miFormulario.is_valid(): #validar que los datos esten ok
            
            infoDict = miFormulario.cleaned_data #la info del formulario se pasa a tipi diccionario
            
            entregable1 = Entregables(nombre = infoDict["nombre"],  fechaEntrega = infoDict["fechaEntrega"], entregado = infoDict["entregado"])

            entregable1.save()

            return render(request, "AppCoder/inicio.html")            
    
    else: #si todavía no le doy click

        miFormulario = EntregablesFormulario()

    return render(request, "AppCoder/crearEntregable.html", {"formulario1":miFormulario})



def busquedaCamada(request):

    return render(request, "AppCoder/busquedaCamada.html")



def resultadosBusqueda(request):
   
    if request.method == "GET":

        camadaBusqueda = request.GET["camada"]
        cursosResultados = Curso.objects.filter(camada__icontains=camadaBusqueda)

        return render(request, "AppCoder/resultadosBusqueda.html", {"camada": camadaBusqueda, "resultado": cursosResultados})
    
    return render(request, "AppCoder/resultadosBusqueda.html", {"camada": camadaBusqueda, "resultado": cursosResultados})

    

def resultados(request):

    if request.method == "GET":

        camadaBusqueda = request.GET["camada"]
        cursosResultados = Curso.objects.filter(camada__icontains=camadaBusqueda)

        return render(request, "AppCoder/resultadosBusqueda.html", {"camada": camadaBusqueda, "resultado": cursosResultados})
    
    return render(request, "AppCoder/resultadosBusqueda.html", {"camada": camadaBusqueda, "resultado": cursosResultados})

 

def buscar_profe(request):

    return render(request, "AppCoder/busquedaProfe.html")



def resultadosProfe(request):
   
    if request.method == "GET":

        profesionBusqueda= request.GET["profesion"]
        profesResultados = Profesor.objects.filter(profesion__icontains=profesionBusqueda)

        return render(request, "AppCoder/resultadosProfes.html", {"profesion": profesionBusqueda, "resultado": profesResultados})
    
    return render(request, "AppCoder/resultadosProfes.html")


#Profesores

@login_required
def leerProfesores(request): 

    profesores = Profesor.objects.all()

    contexto = {"teachers": profesores }

    return render(request, "AppCoder/leerProfes.html", contexto)

def crearProfesores(request):

     if request.method == "POST":

        miFormulario = ProfesorFormulario(request.POST)

        if miFormulario.is_valid():

            info = miFormulario.cleaned_data

            profesor = Profesor(nombre=info["nombre"], apellido=info["apellido"], email=info["email"], profesion=info["profesion"])
        
            profesor.save()

            return render(request, "AppCoder/inicio.html")
        
     else:
        
         miFormulario = ProfesorFormulario()

     return render(request, "AppCoder/profeFormulario.html", {"miFormulario": miFormulario})

def eliminarProfesores(request, profeNombre):
    
    profesor = Profesor.objects.get(nombre=profeNombre)
    
    profesor.delete()

    profesores = Profesor.objects.all()

    contexto = {"teachers": profesores}

    return render(request, "AppCoder/leerProfesores.html", contexto)

def editarProfesores(request, profeNombre):

    profesor = Profesor.objects.get(nombre=profeNombre)
     
    if request.method == "POST":

        miFormulario = ProfesorFormulario(request.POST)

        if miFormulario.is_valid():

            info = miFormulario.cleaned_data

            profesor.nombre = info["nombre"]
            profesor.apellido = info["apellido"]
            profesor.email = info["email"]
            profesor.profesion = info["profesion"]
        
            profesor.save()

            return render(request, "AppCoder/inicio.html")
        
    else:
        
        miFormulario = ProfesorFormulario(initial={"nombre":profesor.nombre, "apellido":profesor.apellido,
                                                   "email":profesor.email, "profesion":profesor.profesion})

    return render(request, "AppCoder/editarProfe.html", {"miFormulario": miFormulario, "nombre": profeNombre})



@login_required
def agregarAvatar(request):

    if request.method =="POST":

        form = AvatarFormulario(request.POST, request.FILES)

        if form.is_valid():

            #usuarioActual = User.objects.get(username=request.user)

            usuarioActual = User.objects.get(username=request.user)

            avatar = Avatar(usuario=usuarioActual, imagen=form.cleaned_data["imagen"])

            avatar.save()

            return render(request, "AppCoder/inicio.html")
        
    else:

        form = AvatarFormulario()

    return render(request, "AppCoder/agregarAvatar.html", {"formulario":form})



class ListaCurso(LoginRequiredMixin, ListView):

    model = Curso

class DetalleCurso(LoginRequiredMixin, DetailView):

    model = Curso

class CrearCurso(LoginRequiredMixin, CreateView):

    model = Curso
    success_url ="AppCoder/curso/list"
    fields = ["nombre", "camada"]

class ActualizarCurso(LoginRequiredMixin, UpdateView):

    model = Curso
    success_url ="AppCoder/curso/list"
    fields = ["nombre", "camada"]

class BorrarCurso(LoginRequiredMixin, DeleteView):
    
    model = Curso
    success_url ="AppCoder/curso/list"
  