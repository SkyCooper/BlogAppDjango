from .serializer import CategorySerializer, PostSerializer
from .models import Category, Post
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
# Create your views here.

#! concreteAPIview
class CategoryList(ListCreateAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  
  #? filter
  filterset_fields = ["name"]
  
  #? search
  search_fields = ["name"]
  ordering_fields = ['id']

#! concreteAPIview
class CategoryDetail(RetrieveUpdateDestroyAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

#! ModelViewSet
class PostMVS(ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  
  #? filter
  filterset_fields = ["category"]
  
  #? search
  search_fields = ["title"]
  ordering_fields = ['id']
  
