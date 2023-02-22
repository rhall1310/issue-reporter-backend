from ast import Sub
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, TopCatViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'top', TopCatViewSet, basename='top')




urlpatterns = [
    path("", include(router.urls)),
    
    
]