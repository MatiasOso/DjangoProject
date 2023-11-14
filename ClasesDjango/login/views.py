from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse, HttpResponse
from requests.exceptions import RequestException
from .models import Receta,Usuario
from .forms import CreateNewRecipe

import requests

# Create your views here.

def index(request):
    return render(request,'login.html',{
        'form':UserCreationForm
    })    
def home(request):
    urlAPI = "http://localhost:3000/usuarios" #Despues del / se debe agregar algo
    
    try:
        response = requests.get(urlAPI)
        
        if response.status_code == 200:
            data = response.json()
            
            tabla_html = "<table>"
            tabla_html += "<tr><th>usuario</th><th>clave</th></tr>"
            for clientes in data['listaclientes']:
                 tabla_html += f"<tr>  <td>{clientes['Nombre']} <td>{clientes['Password']} <td>{clientes['Email']} </td>  </tr>"
            tabla_html += "</table>"
            return render(request,'home.html',{'tabla_html': tabla_html})
        else:
            return HttpResponse("Error en la solicitud a la API", status=500)
    except Exception as e:
        return HttpResponse(str(e), status=500)

def inicio(request):
    urlApi = "http://localhost:3000/recetas"
    
    try:
        response = requests.get(urlApi)
    
        if response.status_code == 200:
            data = response.json()
            tabla_html = "<table>"
            tabla_html += "<tr><th>ID</th> <th>Nombre</th> <th>Ingredientes</th> <th>Preparacion</th> <th>Calificacion</th> <th>Autor</th></tr>"
            for recetas in data['listarecetas']:
                 tabla_html += f"<tr> <td>{recetas['ID']}</td> <td>{recetas['Nombre']} <td>{recetas['Ingredientes']} <td>{recetas['Preparacion']}</td> <td>{recetas['Calificacion']}</td> <td>{recetas['Autor']}</td>  </tr>"
            tabla_html += "</table>"
            return render(request,'inicio.html',
                          {'tabla_html': tabla_html})
        else:
            return HttpResponse("Error en la solicitud a la API", status=500)
    except Exception as e:
        return HttpResponse(str(e), status=500)
    
def AddRecipe(request):
    if request.method == 'GET':        
        return render(request, 'addReceta.html', {
            'form': CreateNewRecipe()
        })
    else:
        # Obtén el usuario correspondiente al ID proporcionado en el formulario
        autor_id = int(request.POST['autor'])
        autor = Usuario.objects.get(pk=autor_id)

        # Crea una nueva receta con el objeto de usuario como autor
        Receta.objects.create(
            categoria=request.POST['categoria'],
            nombre=request.POST['nombre'],
            ingredientes=request.POST['ingredientes'],
            preparacion=request.POST['preparacion'],
            calificacion=request.POST['calificacion'],
            autor=autor
        )
        return redirect('home')
    
def about(request):
    return render(request,'about.html')