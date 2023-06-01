from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.views.generic.edit import CreateView
from .models import ProductoIngresado
from .forms import ProductForm
from django.contrib.auth import login
from .forms import ProductForm

# Create your views here.
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
    return render(request, 'base/base.html')

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

def proveedor_view(request):
    return render(request, 'proveedor.html')

def usuarios_view(request):
    return render(request, 'usuarios.html')

def producto_ingresado(request):
    productos = ProductoIngresado.objects.all()
    return render(request, 'producto.html', {'productos': productos})

def proveedor_ingresado_view(request):
    return render(request, 'proveedor_ingresado.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')

def agregar_producto(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'agregar_producto.html', {
        'form': ProductForm
    })
    else:
        form = ProductForm(request.POST)
        if form.is_valid():
            nuevo_producto = form.save(commit=False)
            nuevo_producto.user = request.user
            nuevo_producto.save()
            print(nuevo_producto)
            return redirect('producto.html')
        else:
            return render(request, 'agregar_producto.html', {'form': ProductForm})

@login_required
def producto(request):
    productos = ProductoIngresado.objects.filter()
    return render(request, 'producto.html', {'productos': productos})

def editar_producto(request, id):
    productos = get_object_or_404(productos, id=id)
    return render(request, 'editar_producto.html', {'form': form})