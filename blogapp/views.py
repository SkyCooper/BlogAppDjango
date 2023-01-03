from .serializer import CategorySerializer, PostSerializer, AuthorSerializer
from .models import Category, Post, Author

#! viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

#! permissions
from rest_framework.permissions import BasePermission, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

#? permission.py dosyası oluşturup orada tanımlandı, burası çok kalabalık olmasın diye.
from .permissions import (
  IsAdminOrReadOnly,        #? biz yazdık (yapay zeka)
  IsAdminUserOrReadOnly     #? sinan hoca yazdı
  )


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
  # permission_classes = [IsAdminUser]
  
  #* authenticate olan herşeyi yapar, olmayan sadece GET(read) yapar.
  # permission_classes = [IsAuthenticatedOrReadOnly]
  
  #todo, admin olan herşeyi yapar, olmayan sadece GET(read) yapar. (BUNU biz kendimiz yazdık)
  # permission_classes = [IsAdminUserOrReadOnly]

#! concreteAPIview
class CategoryDetail(RetrieveUpdateDestroyAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  
  #? permissions
  # permission_classes = [IsAuthenticated]
  # permission_classes = [IsAdminUser]
  

#! ModelViewSet
class PostMVS(ModelViewSet):
  # queryset = Post.objects.filter(is_published=True) #? böylede yazılabilir.
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  
  #? filter
  filterset_fields = ["category"] #? category id'ye göre filitreler,
  # filterset_fields = ["category__name"] 
  #? şimdi Post modelden category gider, o da Category modelden name ile bağlantılı olduğundan name alır, 
  #? ve name'e göre filitreler
  
  #? search
  search_fields = ["title"]
  ordering_fields = ['id']
  
  #? permission
  #* herkes CRUD yapabilir
  # permission_classes = [IsAuthenticated]
  
  #* sadece admin olan CRUD yapabilir
  # permission_classes = [IsAdminUser]
  
  #* Authenticate olan (yani giriş yapan) herşeyi yapar, olmayan sadece GET(read) yapar.
  # permission_classes = [IsAuthenticatedOrReadOnly]


class AuthorMVS(ModelViewSet):
  queryset = Author.objects.all()
  serializer_class = AuthorSerializer