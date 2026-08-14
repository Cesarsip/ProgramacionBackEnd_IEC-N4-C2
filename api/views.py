from rest_framework import viewsets
from .serializer import ProgrammerSerializer
from .models import programmer

# Create your views here.
class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = programmer.objects.all()
    serializer_class = ProgrammerSerializer