from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


def ContentGet(request):
    context ={'queryset':queryset}
    return render(request,'task.html',context)