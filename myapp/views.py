from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Project,Task

def index(request):
    return HttpResponse("Index Page")

# Create your views here.
def hello(request,username):
    return HttpResponse("<h1>Hello  %s</h1>" % username)

# def hello(request,id):
#     # print(type(id))
#     result = id + 100 * 2
#     return HttpResponse("<h1>Hello %s</h1>" % result)
   
def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects,safe=False)

def tasks(request,id):
    tasks = Task.objects.get(id=id) #(pk)
    return HttpResponse('task: %s ' % tasks.title)

def about(request):
    return HttpResponse("About")