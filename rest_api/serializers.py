from rest_framework import serializers
from .models import *


class articleSerializer(serializers.ModelSerializer):
    class Meta:
        model = article
        fields = ["id","title","author","email","date"]



# class articleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=200)
#     author = serializers.CharField(max_length=200)
#     email = serializers.EmailField(max_length=254)
#     date = serializers.DateField()
    
#     def __str__(self):
#         return self.title
    
    
#     def create(self,validated_data):
#         return article.objects.create(validated_data)
    
#     def update(self,instance,validated_data):
#         instance.title = validated_data.get("title",instance.title)
#         instance.author = validated_data.get("author",instance.author)
#         instance.email = validated_data.get("email",instance.email)
#         instance.date = validated_data.get("date",instance.date)
#         instance.save()
#         return instance
    