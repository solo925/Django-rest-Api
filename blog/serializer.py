from rest_framework import serializers
from .models import Post

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model =Post
        fields=['id','title','content','author','created_at']

