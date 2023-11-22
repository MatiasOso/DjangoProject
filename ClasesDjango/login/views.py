from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse, HttpResponse
from requests.exceptions import RequestException
from .models import Receta,Usuario
from .forms import CreateNewRecipe

import requests

# Create your views here.

def register(request):
    return render(request,'register.html',{
        'form':UserCreationForm
    })    
def login(request):
    return render(request,'login.html')



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
    urlImg = [
        'https://drive.google.com/file/d/1RB0qxvAv6P9YOLChdo5QPfR_pNB5C0gT/view', #Lasaña
        'https://drive.google.com/file/d/1tC4CGkjcXK2Jc9qllft9Y5xzXK7EJQea/view', #Pollo
        'https://drive.google.com/file/d/1IDt-nal_hFgGC5yiYKyhI6MWgmNIJmpe/view', #arrozknleche
        'https://drive.google.com/file/d/1qDO_y5Z7Z4DsX4Wj2ijW4EcBhnTEwm53/view', #Manzana
        'https://drive.google.com/file/d/1EJWkD5ToPBodQaAW8rm3KjwAJvxwTFot/view', #Pollo al vino
        'https://drive.google.com/file/d/1k8jgqWfawJwDmmD68UXHe1QyY5WZKmUO/view', #Sopa de tomate
        'https://drive.google.com/file/d/1NpIW-5kRu0_PCaD_30fcvzPdAw9JGNNy/view', #Tortilla chips
        'https://drive.google.com/file/d/15CWF9cBA6irI33EgrY2Pnnce6SWF4XJW/view' #Canape
    ]
    
    try:
        response = requests.get(urlApi)
    
        if response.status_code == 200:
            data = response.json()
            cards_html = ""
            for receta, imagen_receta in zip(data['listarecetas'], urlImg):       
                         
                card = f"""
                <div class="col">
                    <div class="card shadow-sm">
                        <img src="{imagen_receta}" class="card-img-top" alt="Imagen de la receta">
                        <div class="card-body">
                            <h5 class="card-title">{receta['Nombre']}</h5>
                            <p class="card-text">Calificación: {receta['Calificacion']}</p>
                            <div class="d-flex justify-content-between align-items-center">
                                <div class="btn-group">
                                    <a href="/receta/{receta['ID']}" class="btn btn-sm btn-outline-secondary">Ver</a>
                                    <button type="button" class="btn btn-sm btn-outline-secondary">Compartir</button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                """
                cards_html += card
            
            return render(request, 'inicio.html', {'cards_html': cards_html,'imagenes': urlImg})
        else:
            return HttpResponse("Error en la solicitud a la API", status=500)
    except Exception as e:
        return HttpResponse(str(e), status=500)

def AddRecipe(request):
    if request.method == 'POST':
        # Obtén los datos del formulario
        categoria = request.POST['categoria']
        nombre = request.POST['nombre']
        ingredientes = request.POST['ingredientes']
        preparacion = request.POST['preparacion']
        calificacion = request.POST['calificacion']
        autor_id = request.POST['autor']

        # Obtiene el objeto Usuario correspondiente al ID proporcionado en el formulario
        autor = Usuario.objects.get(pk=autor_id)

        # Crea un diccionario con los datos de la receta
        receta_data = {
            'categoria': categoria,
            'nombre': nombre,
            'ingredientes': ingredientes,
            'preparacion': preparacion,
            'calificacion': calificacion,
            'autor': autor_id
        }

        # URL de tu endpoint para agregar recetas en la API en Node.js
        url_api = 'http://localhost:3000/recetas/add'

        try:
            # Realiza una solicitud POST a tu API en Node.js
            response = requests.post(url_api, json=receta_data)

            if response.status_code == 200:
                # Redirige a la página de inicio si la receta se agregó correctamente
                return redirect('home')
            else:
                # Maneja el caso si hay un error al agregar la receta
                return HttpResponse("Error al agregar la receta a la API", status=500)
        except Exception as e:
            return HttpResponse(str(e), status=500)
    else:
        return render(request, 'addReceta.html', {
            'form': CreateNewRecipe()
        })
    
def about(request):
    return render(request,'about.html')

# Ver recetas

def ver_receta(request, id):
    urlApi = f"http://localhost:3000/recetas/{id}"

    try:
        response = requests.get(urlApi)
        print(response.status_code)
        
        if response.status_code == 200:
            receta = response.json()
            cards_html = ""
            for receta in receta:       
                    
                card = f"""
                <div class="col">
                    <div class="card shadow-sm">
                        <div class="card-body">
                            <h5 class="card-title">{receta['Nombre']}</h5>
                            <p class="card-text">Ingredientes: {receta['Ingredientes']}</p>
                            <p class="card-text">Preparacion: {receta['Preparacion']}</p>
                            <p class="card-text">Calificación: {receta['Calificacion']}</p>
                            
                            <div class="d-flex justify-content-between align-items-center">
                            </div>
                        </div>
                    </div>
                </div>
                """
                cards_html += card
            
            return render(request, 'receta.html', {
                'receta': receta, 
                'cards_html': cards_html})
        else:
            return HttpResponse("Error en la solicitud a la API", status=500)
    except Exception as e:
        return HttpResponse(str(e), status=500)
