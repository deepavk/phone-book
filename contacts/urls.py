from .views import ContactViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'', ContactViewSet)
router.register(r'<int:pk>/', ContactViewSet)

urlpatterns = [
    path('', include(router.urls)),
]