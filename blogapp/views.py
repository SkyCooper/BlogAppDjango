from .serializer import CategorySerializer, PostSerializer
from .models import Category, Post

#! viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

#! permissions
from rest_framework.permissions import BasePermission, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly


#! concreteAPIview
class CategoryList(ListCreateAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  
  #? filter
  filterset_fields = ["name"]
  
  #? search
  search_fields = ["name"]
  ordering_fields = ['id']
  
  #? permission
  #* herkes CRUD yapabilir
  # permission_classes = [IsAuthenticated]
  
  #* sadece admin olan CRUD yapabilir
  permission_classes = [IsAdminUser]
  
  #* admin olan herşeyi yapar, olmayan sadece GET(read) yapar.
  # permission_classes = [IsAuthenticatedOrReadOnly]

#! concreteAPIview
class CategoryDetail(RetrieveUpdateDestroyAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  
  #? permissions
  # permission_classes = [IsAuthenticated]
  permission_classes = [IsAdminUser]
  

#! ModelViewSet
class PostMVS(ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  
  #? filter
  filterset_fields = ["category"]
  
  #? search
  search_fields = ["title"]
  ordering_fields = ['id']
  
  #? permission
  #* herkes CRUD yapabilir
  # permission_classes = [IsAuthenticated]
  
  #* sadece admin olan CRUD yapabilir
  permission_classes = [IsAdminUser]
  
  #* Authenticate olan (yani giriş yapan) herşeyi yapar, olmayan sadece GET(read) yapar.
  # permission_classes = [IsAuthenticatedOrReadOnly]
  