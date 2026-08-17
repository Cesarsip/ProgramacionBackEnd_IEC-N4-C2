from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    # Redirige la raíz (/) directamente a la vista HTML de DevHub
    path('', RedirectView.as_view(url='/api/v1/home/', permanent=False)),
    
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]