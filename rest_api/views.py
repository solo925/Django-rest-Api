from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import articleSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics,mixins,viewsets
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# --------------------------------------------------------------
# MODAL VIEWSETS
# --------------------------------------------------------------

class ArticlesViewset(viewsets.ModelViewSet):
    serializer_class = articleSerializer
    queryset = article.objects.all()

# --------------------------------------------------------------
# GENERIC VIEWS 
# ---------------------------------------------------------------
class GenericApIViews(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin):
    
    serializer_class = articleSerializer
    queryset = article.objects.all()
    
    lookup_field='id'
    
    authentication_classes=[SessionAuthentication,BasicAuthentication,TokenAuthentication]
    permission_classes=[IsAuthenticated]
    
    def get(self,request,id=None):
        if id:
            return self.retrieve(request,id)
        else:
            return self.list(request)
        
    
    def post(self,request,id=None):
        return self.create(request)
    
    def put(self,request,id=None):
        return self.update(request,id)
    
    def delete(self,request,id=None):
        return self.destroy(request,id)

# --------------------------------------------------------------
# CLASS BASED VIEWS
# ---------------------------------------------------------------
class ArticleAPIView(APIView):
    def get(self,request):
        artic = article.objects.all()
        serializer = articleSerializer(artic,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = articleSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class ArticleDetails(APIView):
    def get_object(self,id):
        try:
            return article.objects.get(id=id)
        
        except article.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        
    def get(self,request,id):
        artic = self.get_object(id)
        serializer = articleSerializer(artic)
        return Response(serializer.data)
    
    def put(self,request,id):
        artic = self.get_object(id)
        serializer = articleSerializer(artic,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        artic = self.get_object(id)
        artic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
        
            
# --------------------------------------------------------------
# FUNCTION VIEWS
# ---------------------------------------------------------------        
        
        

# @csrf_exempt
@api_view(['GET','POST'])
def article_list(request):
    if request.method =="GET":
        artic = article.objects.all()
        serializer = articleSerializer(artic,many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        # data = JSONParser().parse(request)
        serializer = articleSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
# @csrf_exempt
@api_view(["GET","PUT","DELETE"])
def article_details(request,pk):
    try:
        artic=article.objects.get(pk=pk)
        
    except article.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    if request.method =="GET":
        serializer = articleSerializer(artic)
        return Response(serializer.data)
    elif request.method=="PUT":
        # data = JSONParser().parse(request)
        serializer = articleSerializer(artic,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    
          
        




# Create your views here.
# def Home(request):
#     context={}
#     return render(request,"home.html",context)

