from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse, HttpResponse
from requests.exceptions import RequestException
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
            tabla_html += "<tr><th>id</th><th>usuario</th><th>clave</th></tr>"
            for clientes in data['listaclientes']:
                 tabla_html += f"<tr> <td>{clientes['ID']}</td> <td>{clientes['Nombre']} <td>{clientes['Password']} <td>{clientes['Email']} </td>  </tr>"
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
        # a futuro hare esto con una base de datos real (quizas db4free)
    title = 'Add Receta!!'    
    return render(request, 'addReceta.html',{
        # Diccionario
        'title' : title
    })
    
def about(request):
    return render(request,'about.html')
    
    
    
        
        
        




    
    
