from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
import requests



class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# If you want to fetch data directly from the API endpoint
def task_list(request):
    response = requests.get('http://localhost:8000/tasks/')  # Replace with your API endpoint
    tasks = response.json()  # Convert response to JSON format
    return render(request, 'tasks.html', {'tasks': tasks})

# Alternatively, if you want to fetch data directly from the database
def task_list_db(request):
    tasks = Task.objects.all()  # Query the database
    return render(request, 'tasks.html', {'tasks': tasks})
