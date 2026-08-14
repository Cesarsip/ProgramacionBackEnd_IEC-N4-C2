from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'programmers', views.ProgrammerViewSet)

urlpatterns = [
    path('home/', views.home, name='home'),       # <-- Nueva ruta HTML
    path('', include(router.urls))                # Rutas API
]