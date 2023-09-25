from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def holaMundo(request):
    return render(request,'login.html',{
        'form':UserCreationForm
    })


    
    
