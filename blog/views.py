from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegistrationForm

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('base')
        else:
            return render(request, 'login.html', {'error': 'Nombre de usuario o contraseña incorrectos'})
    else:
        return render(request, 'login.html')
    
def logout_view(request):
    logout(request)
    return redirect('base')

@login_required
def producto_view(request):
    return render(request, 'base.html')

@login_required
def inventarioVista(request):
    return render(request, 'producto.html')

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'registro.html', {'form': form})

def factura_view(request):
    return render(request, 'factura.html')

def clientes_view(request):
    return render(request, 'clientes.html')

def proveedor_view(request):
    return render(request, 'proveedor.html')

def usuarios_view(request):
    return render(request, 'usuarios.html')

def opciones_view(request):
    return render(request, 'opciones.html')

def pedido_view(request):
    return render(request, 'pedido.html')

def producto_ingresado_view(request):
    return render(request, 'producto_ingresado.html')

def proveedor_ingresado_view(request):
    return render(request, 'proveedor_ingresado.html')