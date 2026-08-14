from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ProgrammerSerializer
from .models import programmer

# Vista para la API REST
class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = programmer.objects.all()
    serializer_class = ProgrammerSerializer

# Vista para la plantilla HTML
def home(request):
    programmers = programmer.objects.all()
    return render(request, 'api/index.html', {'programmers': programmers})