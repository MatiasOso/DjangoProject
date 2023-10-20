from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name = "index"),
    path('about/',views.about, name = "about"),
    path('hello/<str:username>',views.hello , name = "hello"),
    path('projects/',views.projects , name = "projects"),
    path('projects/<int:id>',views.project_detail , name = "project_detail"),
    path('tasks/',views.tasks , name = "tasks"),
    path('create_task/',views.create_task , name = "create_task"),
    path('create_project/',views.create_project , name = "create_project")
    
            
]

# django.core.exceptions.ImproperlyConfigured: The included URLconf '<module 'myapp.urls' from 'C:\\Users\\matio\\OneDrive\\Documentos\\djangoproject\\DjangoProject\\myapp\\urls.py'>' 
# does not appear to have any patterns in it. If you see the 'urlpatterns' variable with valid patterns in the file then the issue is probably caused by a circular import.