from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.parsers import FormParser, MultiPartParser


from .serializers import ReportSerializer, PublicSerializer
from .models import Report
from django_filters import rest_framework as filters

# Create your views here.


class ReportViewSet(viewsets.ModelViewSet):

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


class PublicViewSet(viewsets.ModelViewSet):
    parser_classes = (FormParser, MultiPartParser)
    serializer_class = PublicSerializer
    queryset = Report.objects.filter(resolved=False)
