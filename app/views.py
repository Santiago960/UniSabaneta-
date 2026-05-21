from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from .models import Materia, Ingles, Horario, Perfil


# INICIO
def inicio(request):

    return render(request, 'app/inicio.html')


# LOGIN
def login_view(request):

    error = ""

    if request.method == "POST":

        username = request.POST["username"]

        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("inicio")

        else:

            error = "Usuario o contraseña incorrectos"

    return render(request, "app/login.html", {

        "error": error

    })


# REGISTRO
def registro(request):

    form = UserCreationForm()

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("login")

    return render(request, "app/registro.html", {

        "form": form

    })


# LOGOUT
def logout_view(request):

    logout(request)

    return redirect("inicio")


# MATERIAS
def materias(request):

    materias = Materia.objects.all()

    return render(request, 'app/materias.html', {

        'materias': materias

    })


# INGLES
def ingles(request):

    cursos = Ingles.objects.all()

    return render(request, 'app/ingles.html', {

        'cursos': cursos

    })


# RECOMENDACION
def recomendacion(request):

    materias = Materia.objects.filter(semestre=1)

    return render(request, 'app/recomendacion.html', {

        'materias': materias

    })


# HORARIOS
def horarios(request):

    horarios = Horario.objects.all()

    return render(request, 'app/horarios.html', {

        'horarios': horarios

    })


# PERFIL
def perfil(request):

    perfil_usuario, creado = Perfil.objects.get_or_create(

        usuario=request.user

    )

    mensaje = ""

    if request.method == "POST":

        nombre = request.POST.get("nombre")

        if nombre:

            perfil_usuario.nombre_completo = nombre

        if 'foto' in request.FILES:

            perfil_usuario.foto = request.FILES['foto']

        perfil_usuario.save()

        mensaje = "Perfil actualizado correctamente"

    return render(request, 'app/perfil.html', {

        'perfil': perfil_usuario,

        'mensaje': mensaje

    })

    # REPORTE MATERIAS
def reporte_materias(request):

    materias = Materia.objects.all()

    return render(request, 'app/reporte_materias.html', {

        'materias': materias

    })


# REPORTE HORARIOS
def reporte_horarios(request):

    horarios = Horario.objects.all()

    return render(request, 'app/reporte_horarios.html', {

        'horarios': horarios

    })