from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializer import ProgrammerSerializer
from .models import programmer

# Vista para la API REST (JSON)
class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = programmer.objects.all()
    serializer_class = ProgrammerSerializer

# Vista protegida para el Dashboard CRUD
@login_required
def home(request):
    programmers = programmer.objects.all()
    return render(request, 'api/index.html', {'programmers': programmers})

# Vistas de navegación general
def inicio_view(request):
    return render(request, 'api/inicio.html')

def servicios_view(request):
    return render(request, 'api/servicios.html')

def contacto_view(request):
    return render(request, 'api/contacto.html')