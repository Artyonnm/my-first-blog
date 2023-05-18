"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.producto, name='producto')
Class-based views
    1. Add an import:  from other_app.views import producto
    2. Add a URL to urlpatterns:  path('', producto.as_view(), name='producto')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog import views
from blog.views import producto_view
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('base.html', producto_view, name='base'),
    path('registro/', views.registration_view, name='registro'),
    path('producto.html', views.inventarioVista, name='producto'),
   
    path('pedido.html', views.pedido_view, name='pedido'),
    path('factura.html', views.factura_view, name='factura'),
    path('clientes.html', views.clientes_view, name='clientes'),
    path('proveedor.html', views.proveedor_view, name='proveedor'),
    path('usuarios.html', views.usuarios_view, name='usuarios'),
    path('opciones.html', views.opciones_view, name='opciones'), 
    path('producto_ingresado.html', views.producto_ingresado_view, name='producto_ingresado'), 
    path('proveedor_ingresado.html', views.proveedor_ingresado_view, name='proveedor_ingresado'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)