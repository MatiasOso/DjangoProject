from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from requests.exceptions import RequestException
from .models import Receta,Usuario,Imagen
from .forms import CreateNewRecipe
# from .google_auth_API import upload_file, get_recipe_image_url

import requests




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
    urlApiRecetas = "http://localhost:3000/recetas"
    urlApiImagenes = "http://localhost:3000/imagenes"  # Nueva URL para obtener las imágenes

    try:
        responseRecetas = requests.get(urlApiRecetas)
        responseImagenes = requests.get(urlApiImagenes)  # Obtener las URLs de las imágenes desde la API

        if responseRecetas.status_code == 200 and responseImagenes.status_code == 200:
            dataRecetas = responseRecetas.json()
            dataImagenes = responseImagenes.json()

            cards_html = ""
            for receta, imagen_receta in zip(dataRecetas['listarecetas'], dataImagenes['listaimg']):       
                         
                card = f"""
                <div class="col">
                    <div class="card shadow-sm">
                        <img src="{imagen_receta['IMG']}" class="card-img-top" alt="Imagen de la receta">
                        <div class="card-body">
                            <h5 class="card-title text-center">{receta['Nombre']}</h5>
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
            
            return render(request, 'inicio.html', {
                'cards_html': cards_html,
                })
        else:
            return HttpResponse("Error en la solicitud a la API", status=500)
    except Exception as e:
        return HttpResponse(str(e), status=500)

def obtener_categorias(request):
    url_api = 'http://localhost:3000/categorias'

    try:
        response = requests.get(url_api)

        if response.status_code == 200:
            categorias = response.json()
            return categorias
        else:
            print("Error en la solicitud a la API", status=500)
            return []
    except Exception as e:
        print(str(e))
        return []  

def header(request):
    categorias = obtener_categorias(request)
    print(categorias)
    return render(request, 'header.html', {
        'categorias': categorias,
    })
    
    
def buscar_por_categoria(request):
    categoria = request.GET.get('Categoria')  # Mantener 'Categoria' con mayúscula

    if not categoria:
        return render(request, 'plantilla_sin_categoria.html')

    url_api = f'http://localhost:3000/buscar/?Categoria={categoria}'  # Actualizar la URL a 'Categoria'

    try:
        response = requests.get(url_api)

        if response.status_code == 200:
            recetas = response.json()
            return render(request, 'Categoria.html', {'recetas': recetas, 'categoria': categoria})
        else:
            return render(request, 'error_solicitud_api.html')
    except requests.RequestException as e:
        return render(request, 'error_excepcion.html')

    
    


def AddRecipe(request):
    if request.method == 'POST':
        # Obtén los datos del formulario
        categoria = request.POST['categoria']
        nombre = request.POST['nombre']
        ingredientes = request.POST['ingredientes']
        preparacion = request.POST['preparacion']
        calificacion = request.POST['calificacion']
        img = request.POST['img']
        # autor_id = request.POST['autor']

        # Obtiene el objeto Usuario correspondiente al ID proporcionado en el formulario
        # autor = Usuario.objects.get(pk=autor_id) # Que no se me olvide que todavia no necesito que sea un usuario existente el que agregue la receta

        receta_data = {
            'categoria': categoria,
            'nombre': nombre,
            'ingredientes': ingredientes,
            'preparacion': preparacion,
            'calificacion': calificacion,
        }
        img_data = {
            'img' : img
        }

        # URL de tu endpoint para agregar recetas en la API en Node.js
        url_api = 'http://localhost:3000/recetas/add'
        url_api_imagenes = 'http://localhost:3000/imagenes/add'
        
        try:
            # Realiza una solicitud POST a tu API en Node.js
            response = requests.post(url_api, json=receta_data)
            
            if response.status_code == 200:
                # Redirige a la página de inicio si la receta se agregó correctamente
                return redirect('inicio')
            else:
                # Maneja el caso si hay un error al agregar la receta
                return HttpResponse("Error al agregar la receta a la API", status=500)
        except Exception as e:
            return HttpResponse(str(e), status=500)
    else:
        return render(request, 'addReceta.html', {
            'form': CreateNewRecipe(),
            'formsimg' : Imagen
        })
    
def about(request):
    return render(request,'about.html')

# Ver recetas
# Ver recetas
# Ver recetas
# Ver recetas
# Ver recetas
# Ver recetas
# Ver recetas

def comentar_receta(request):
    if request.method == 'POST':
        usuario = request.POST['Usuario']
        receta_id = request.POST['Receta_ID']
        comentario = request.POST['Comentario']
        
        comentario_data = {
            'usuario': usuario,
            'receta_id': receta_id,
            'comentario': comentario,
        }
        url_api = 'http://localhost:3000/recetas/comentarios/add'
        
        try:
            response = requests.post(url_api, json=comentario_data)
            
            if response.status_code == 200:
                return redirect('localhost:8000/receta/{receta_id}')
            else:
                return HttpResponse("Error al agregar el comentario a la API", status=500)
        except Exception as e:
            return HttpResponse(str(e), status=500)
    else:
        return render(request, 'receta/{id}', {
            'form': CreateNewRecipe()  #HELP AQUI   
        })
                      
        
        

def ver_receta(request, id):
    urlApi = f"http://localhost:3000/recetas/{id}"
    urlComents = f"http://localhost:3000/recetas/comentarios/{id}"
    urlComentarios = f"http://localhost:3000/recetas/comentarios/add"

    if request.method == 'POST':
        comentario = request.POST.get('Comentario')
        usuario = request.POST.get('Usuario')

        if usuario is None or usuario == "":
            usuario = 1

        datos_comentario = {
            'Usuario': usuario,
            'Receta_ID': id,
            'comentario': comentario,
        }

        try:
            responseComentar = requests.post(urlComentarios, json=datos_comentario)
            
            if responseComentar.status_code != 200:
                return HttpResponse("Error al agregar el comentario a la API", status=500)
        except Exception as e:
            return HttpResponse(str(e), status=500)

        # Si se agregó correctamente el comentario, podrías redirigir a alguna vista
        return redirect('inicio')  # Reemplaza 'nombre_de_la_vista' por tu vista deseada

    try:
        response = requests.get(urlApi)
        responseComents = requests.get(urlComents)
        
        if response.status_code == 200:
            receta = response.json()
            
            if responseComents.status_code == 200:
                coments = responseComents.json()
            else:
                coments = []

            cards_html = ""
            for rec in receta:  # Cambia el nombre de la variable para no reemplazar la lista `receta`
                ingredientes = rec['Ingredientes'].split(", ")
                ingredientes_html = "<ul>"
                for ingrediente in ingredientes:
                    ingredientes_html += f"<li>{ingrediente}</li>"
                ingredientes_html += "</ul>"
                card = f"""
                <div class="col">
                    <div class="card shadow-sm">
                        <div class="card-body">
                            <h5 class="card-title">{rec['Nombre']}</h5>
                            <p class="card-text">Ingredientes:</p>
                            {ingredientes_html}
                            <p class="card-text">Preparacion: {rec['Preparacion']}</p>
                            <p class="card-text">Calificación: {rec['Calificacion']}</p>
                            <div class="d-flex justify-content-between align-items-center">
                            </div>
                        </div>
                    </div>
                </div>
                """
                cards_html += card

            for coment in coments:
                card = f"""
                <div class="col">
                    <div class="card shadow-sm">
                        <div class="card-body">
                            <p class="card-text">Usuario: {coment['Usuario']}</p>
                            <p class="card-text">{coment['Comentario']}</p>
                            <div class="d-flex justify-content-between align-items-center">
                            </div>
                        </div>
                    </div>
                </div>
                """
                cards_html += card

            return render(request, 'receta.html', {
                'receta': receta, 
                'cards_html': cards_html,
                'coments': coments,
                'receta_id': id,
            })
        else:
            return HttpResponse("Error en la solicitud a la API", status=500)
    except Exception as e:
        return HttpResponse(str(e), status=500)
    
# LOGIN N REGISTER LOGIN N REGISTER LOGIN N REGISTER LOGIN N REGISTER
# LOGIN N REGISTER LOGIN N REGISTER LOGIN N REGISTER LOGIN N REGISTER
# LOGIN N REGISTER LOGIN N REGISTER LOGIN N REGISTER LOGIN N REGISTER
# LOGIN N REGISTER LOGIN N REGISTER LOGIN N REGISTER LOGIN N REGISTER
# LOGIN N REGISTER LOGIN N REGISTER LOGIN N REGISTER LOGIN N REGISTER


def register(request): #Yo del futuro: Quizas no necesites usar UserCreationForm ya que puede que al hacer migraciones jodas los modelos y con ello las demas paginas asi que prueba con solo usar lo creado por ti (register con el forms hecho por ti)
                       # Y que tal si no uso el forms? puede que eso me de el error al registrar usuarios :////
    if request.method == 'POST':
            nombre = request.POST.get('user')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            email = request.POST.get('email')

            # Crea el diccionario con los datos del usuario
            if password1 == password2:
                usuario_data = {
                    'nombre': nombre,
                    'password': password1,
                    'email': email,
                }
            else:
                return HttpResponse("Las contraseñas no coinciden")
            
            # URL de tu endpoint para agregar usuarios en la API en Node.js
            url_api = 'http://localhost:3000/usuarios/add'
            
            try:
                # Realiza una solicitud POST a tu API en Node.js
                response = requests.post(url_api, json=usuario_data)
                
                if response.status_code == 200:
                    # Redirige a la página de inicio si el usuario se registró correctamente
                    return redirect('inicio') # Funcionó pero me lo entrego NULL D:
                else:
                    # Maneja el caso si hay un error al agregar el usuario
                    return HttpResponse("Error al agregar el usuario a la API", status=500)
            except Exception as e:
                return HttpResponse(str(e), status=500)
    else:
        form = UserCreationForm()
    #
    return render(request, 'register.html', {'form': form})
      
    
    
def login(request):
    if request.method == 'POST':
        user = request.POST['username']
        password = request.POST['password']
    
        url_auth = 'http://localhost:3000/usuarios'
        try:
            response = requests.get(url_auth)

            if response.status_code == 200:
                data = response.json()
                # Iterar a través de cada usuario para verificar credenciales
                for user_data in data.get('listaclientes', []):
                    if user_data['Nombre'] == user and user_data['Password'] == password:
                        return redirect('inicio')
                # Si el bucle termina sin retornar, significa que las credenciales no coinciden
                return HttpResponse("Error al encontrar al usuario", status=500)
            else:
                return HttpResponse("Error al encontrar al usuario", status=500)
        except Exception as e:
            return HttpResponse(str(e), status=500)
    else:
        return render(request, 'login.html', {})

