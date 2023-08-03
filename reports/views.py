from django.shortcuts import render
from rest_framework import viewsets, generics, authentication
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
    TokenAuthentication,
)
from .serializers import ReportSerializer
from .models import Report
from django_filters import rest_framework as filters

# Create your views here.


class ReportViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]

    parser_classes = (FormParser, MultiPartParser)
    serializer_class = ReportSerializer
    queryset = Report.objects.all()


class ResolvedViewSet(viewsets.ModelViewSet):
    parser_classes = (FormParser, MultiPartParser)
    serializer_class = ReportSerializer
    queryset = Report.objects.filter(resolved=True)


class OpenViewSet(viewsets.ModelViewSet):
    parser_classes = (FormParser, MultiPartParser)
    serializer_class = ReportSerializer
    queryset = Report.objects.filter(resolved=False)
