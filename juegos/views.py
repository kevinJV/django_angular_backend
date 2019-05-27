from rest_framework import generics
from .models import Juegos
from .serializers import JuegosSerializer


class JuegosList(generics.ListCreateAPIView):
    queryset = Juegos.objects.all()
    serializer_class = JuegosSerializer

class JuegosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Juegos.objects.all()
    serializer_class = JuegosSerializer
    