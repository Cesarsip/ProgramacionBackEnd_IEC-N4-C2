from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from .views import ProgrammerViewSet, home, inicio_view, servicios_view, contacto_view

router = DefaultRouter()
router.register(r'programmers', ProgrammerViewSet)

urlpatterns = [
    # Rutas públicas
    path('inicio/', inicio_view, name='inicio'),
    path('servicios/', servicios_view, name='servicios'),
    path('contacto/', contacto_view, name='contacto'),

    # Autenticación Web
    path('login/', auth_views.LoginView.as_view(template_name='api/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Vista protegida (Dashboard / Index)
    path('home/', home, name='home'),

    # Rutas API REST
    path('', include(router.urls)),
]