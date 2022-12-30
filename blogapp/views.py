from .serializer import CategorySerializer, PostSerializer
from .models import Category, Post
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
# Create your views here.

#! concreteAPIview
class CategoryList(ListCreateAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

#! concreteAPIview
class CategoryDetail(RetrieveUpdateDestroyAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

#! ModelViewSet
class PostMVS(ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  
