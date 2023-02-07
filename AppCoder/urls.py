from django.urls import path
from AppCoder.views import *

urlpatterns = [

    path("inicio/", inicio, name = "Inicio"), 
    path("cursos/", curso, name = "Cursos"),
    path("verEstudiante/", ver_estudiante, name = "Estudiantes"), 
    path("verProfesor/", ver_profesor, name = "Profesores"),
    path("verEntregables/", ver_entregables, name = "Entregables"),
    path("cursoFormulario/", cursoFormulario, name = "FormularioCurso"),
    path("buscarCamada/", busquedaCamada, name="BuscarCamada"),
    path("resultados/", resultados, name="ResultadosBusqueda"),
    
]
