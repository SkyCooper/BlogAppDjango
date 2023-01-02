from rest_framework import serializers
from .models import Category, Post, Author

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = ['id', 'name']
  
class PostSerializer(serializers.ModelSerializer):
  category = serializers.StringRelatedField() 
  #? artık field içinde category id olarak değil string olarak görünecek,
  #? fakat create ederken yukarıdaki kullanılamaz, onun için category_id tanımlanır. 
  category_id = serializers.IntegerField(write_only=True)
  #? write_only=True olduğu için create ederken yazılır, get yapınca çıktıda görünmez. 
  class Meta:
    model = Post
    fields = ['id', 'category', 'title', 'category_id', 'content', 'is_published', 'created_date']
    
class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Author
    fields = ['name']