from django.shortcuts import render
from rest_framework import viewsets
from.models import Post
from .serializer import BlogSerializer

# Create your views here.

class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer
