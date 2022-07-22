from rest_framework import viewsets
from .models import Contato
from .serializers import ContatoSerializer

# Create your views here.

class ContatoView(viewsets.ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
