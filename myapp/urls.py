from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('about/',views.about),
    path('hello/<str:username>',views.hello),
    path('projects/',views.projects),
    path('tasks/',views.tasks),
    path('create_task/',views.create_task)
            
]

# django.core.exceptions.ImproperlyConfigured: The included URLconf '<module 'myapp.urls' from 'C:\\Users\\matio\\OneDrive\\Documentos\\djangoproject\\DjangoProject\\myapp\\urls.py'>' 
# does not appear to have any patterns in it. If you see the 'urlpatterns' variable with valid patterns in the file then the issue is probably caused by a circular import.