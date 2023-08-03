from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
    TokenAuthentication,
)
from .serializers import CategorySerializer
from .models import Category
from django_filters import rest_framework as filters

# Create your views here.


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filterset_fields = {"parent": ["exact", "isnull"]}


class TopCatViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(parent__isnull=True)
