from django.urls import path
from AppCoder.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path("inicio/", inicio, name = "Inicio"), 
    path("cursos/", curso, name = "Cursos"),
    path("verEstudiante/", ver_estudiante, name = "Estudiantes"), 
    path("verProfesor/", ver_profesor, name = "Profesores"),
    path("verEntregables/", ver_entregables, name = "Entregables"),
    path("cursoFormulario/", cursoFormulario, name = "FormularioCurso"),
    path("buscarCamada/", busquedaCamada, name="BuscarCamada"),
    path("resultados/", resultados, name="ResultadosBusqueda"),
    
    #Usuario
    path("login/", InicioSesion, name="LogIn"),
    path("register/", registro, name="SingUp"),
    path("logout/", LogoutView.as_view(template_name=("AppCoder/logout.html")), name="LogOut"),
    path("editar/", editarUsuario, name="EditarUsuario"),
    path("agregar/", agregarAvatar, name="Avatar"),
    
    #Crear con formulario de Django
    path("crearCurso/", crear_curso, name="CrearCurso" ),
    path("crearEstudiante/", crear_estudiantes, name="Crear Estudiante" ),
    path("crearEntregable/", crear_entregables, name="Crear Entregables" ),

    #Buscar información
    path("buscarCamada/", busquedaCamada, name="Buscar Camadas"),
    path("resultados_busqueda/", resultadosBusqueda),
    path("buscar_profe/", buscar_profe),
    path("resultados_profe/", resultadosProfe),

    #CRUD de Profesores
    path("leerProfes/", leerProfesores, name="ProfeoresLeer"),
    path("crearProfes/", crearProfesores, name="ProfesoresCrear"),
    path("eliminarProfes/<profeNombre>", eliminarProfesores, name="ProfesoresEliminar"),
    path("editarProfes/<profeNombre>", editarProfesores, name="ProfesoresEditar"),

    #CRUD de cursos usando Clases
    path("curso/list/", ListaCurso.as_view(), name="CursosLeer"),
    path("curso/<int:pk>", DetalleCurso.as_view(), name="CursosDetalle"),
    path("curso/crear/", CrearCurso.as_view(), name="CursosCrear"),
    path("curso/editar/<int:pk>", ActualizarCurso.as_view(), name="CursosEditar"),
    path("curso/borrar/<int:pk>", BorrarCurso.as_view(), name="CursosBorrar"),


   
]

