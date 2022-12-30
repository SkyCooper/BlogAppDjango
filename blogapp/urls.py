from django.urls import path, include
from .views import CategoryList, CategoryDetail, PostMVS
from rest_framework import routers

#! ModelViewSet(router)
router = routers.DefaultRouter()
router.register("post", PostMVS )

urlpatterns = [
  #! concreteAPIview(as_view)
    path('category/', CategoryList.as_view()),
    path('category/<int:pk>', CategoryDetail.as_view()),
    
  #! ModelViewSet(url)
  # path('', include(router.urls))
]

#! ModelViewSet(url)
urlpatterns += router.urls