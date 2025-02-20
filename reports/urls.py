from ast import Sub
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReportViewSet, ResolvedViewSet, OpenViewSet, PublicViewSet


router = DefaultRouter()


router.register(r"all", ReportViewSet, basename="all/")
router.register(r"resolved", ResolvedViewSet, basename="resolved")
router.register(r"open", OpenViewSet, basename="open")
router.register(r"public", PublicViewSet, basename="public")


urlpatterns = [
    path("", include(router.urls)),
]
