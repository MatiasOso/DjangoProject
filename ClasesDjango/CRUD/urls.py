"""
URL configuration for CRUD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from login import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.inicio, name = "inicio") ,
    path('AgregarReceta',views.AddRecipe, name="AddRecipe"),
    path('about',views.about, name="about"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('receta/<int:id>', views.ver_receta, name='ver_receta'),
]
# path('home',views.home),
# path('inicio',views.inicio, name = "inicio"),