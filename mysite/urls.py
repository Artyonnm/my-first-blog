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
    path('', views.login_view, name='login'),
    path('base.html', views.producto_view, name='base'),
    path('admin/', admin.site.urls),
    path('crear_producto', views.agregar_producto, name='crear_producto'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registration_view, name='registro'),
    
    path('producto.html', views.producto, name='producto'),
    path('agregar_producto.html', views.agregar_producto, name='agregar_producto'),
    path('editar_producto.html', views.editar_producto, name='editar_producto'),

    path('factura.html', views.factura_view, name='factura'),
    path('proveedor.html', views.proveedor_view, name='proveedor'),
    path('usuarios.html', views.usuarios_view, name='usuarios'),
    path('proveedor_ingresado.html', views.proveedor_ingresado_view, name='proveedor_ingresado'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('dashboard.html', views.dashboard_view, name='dashboard'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)