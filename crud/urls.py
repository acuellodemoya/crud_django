"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from usuarios.views import index, UserCreate, UserList, UserUpdate, UserDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('crear_usuario/', UserCreate.as_view(), name='crear_usuario'),
    path('listar_usuarios/', UserList.as_view(), name='listar_usuarios'),
    path('modificar_usuarios/<int:pk>', UserUpdate.as_view(), name='modificar_usuarios'),
    path('eliminar_usuario/<int:pk>', UserDelete.as_view(), name='eliminar_usuario'),
]
