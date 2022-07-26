import json
import requests
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from .models import Contato
from .serializers import ContatoSerializer


# Create your views here.

class ContatoView(viewsets.ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer

    def get(self, request, format=None):
        queryset = Contato.objects.all
        result = ContatoSerializer(queryset, many=True).data
        return Response(result)

    def post(self, request, formt=None):
        url = 'https://unimedsaocarlos.http.msging.net/messages?='
        headers = {'Content-Type':'application/json', 'Key':'YXRpdm92ZW5kYXM6Vlhyak5FekxsbUpxUnR6enpuRFQ'}
        payload = {request.data}

        print(payload)

        r = requests.post(url, headers=headers, json=payload)
        return payload
