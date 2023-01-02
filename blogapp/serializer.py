from rest_framework import serializers
from .models import Category, Post, Author

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ['id', 'name']
  
class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = ['id', 'category', 'title']
    
class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Author
    fields = ['name']