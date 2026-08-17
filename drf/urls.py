# drf/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    # Solución al 404: Redirige la raíz directamente a la página Inicio
    path('', RedirectView.as_view(url='/api/v1/inicio/', permanent=False)),
    
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
]