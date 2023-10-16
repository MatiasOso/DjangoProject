from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse, HttpResponse
import requests
# Create your views here.

def holaMundo(request):
    return render(request,'login.html',{
        'form':UserCreationForm
    })
def Home(request):
    urlAPI = "http://127.0.0.1:8000/" #Despues del / se debe agregar algo
    
    try:
        response = requests.get(urlAPI)
        if response.status_code == 200:
            data = response.json()
            
            tabla_html = "<table>"
            tabla_html += "<tr> <td>ID</td> <td>USUARIO</td> <td>CLAVE</td> </tr>"
            for cliente in data['lista']: #Cambiar lista pro lo que esta en mi DB
                tabla_html += f"<tr> <td>{cliente['ID']}</td>  <td>{cliente['USUARIO']}</td>  <td>{cliente['PASSWORD']}</td>   </tr>"
                
        
                tabla_html += "</table>"
                return render(request,'home.html',{'tabla_html': tabla_html})
    except Exception as e:
        return HttpResponse(str(e), status=500)


    
    
