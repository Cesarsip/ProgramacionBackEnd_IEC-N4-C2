# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'programmers', views.ProgrammerViewSet)

urlpatterns = [
    # API endpoints
    path('', include(router.urls)),
    
    # Vistas HTML personalizadas
    path('inicio/', views.inicio_view, name='inicio'),
    path('servicios/', views.servicios_view, name='servicios'),
    path('contacto/', views.contacto_view, name='contacto'),
]