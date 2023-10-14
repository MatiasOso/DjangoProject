from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Project,Task
from django.shortcuts import get_object_or_404,render
from .forms import CreateNewTask

def index(request):
    # a futuro hare esto con una base de datos real (quizas db4free)
    title = 'Django Course!!'    
    return render(request, 'index.html',{
        # Diccionario
        'title' : title
    })


def about(request):
    username = '0somens'
    return render(request,'about.html', {
        'username' : username
    })

# Create your views here.
def hello(request,username):
    return HttpResponse("<h1>Hello  %s</h1>" % username)

# def hello(request,id):
#     # print(type(id))
#     result = id + 100 * 2
#     return HttpResponse("<h1>Hello %s</h1>" % result)
   
def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request,'projects.html',{
        'projects': projects
    })

def tasks(request): #(request,id)
    # tasks = Task.objects.get(id=id) #(pk)
    # tasks = Task.objects.get(title=title) 
    # tasks = get_object_or_404(Task, title = title) # I NEED TO FIX THIS
    tasks =  Task.objects.all()
    return render(request,'tasks.html',{
        'tasks' : tasks 
    })
    
def create_task(request):
    if request.method == 'GET':
        # show interface
        return render(request,'create_task.html',{
            'form':CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'],
                            description=request.POST['description'],project_id=2)
        return redirect('/tasks/')