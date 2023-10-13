from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Project,Task
from django.shortcuts import get_object_or_404

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

def tasks(request,title): #(request,id)
    # tasks = Task.objects.get(id=id) #(pk)
    # tasks = Task.objects.get(title=title) 
    tasks = get_object_or_404(Task, title = title) # I NEED TO FIX THIS
    return HttpResponse('task: %s ' % tasks.title)

def about(request):
    return HttpResponse("About")