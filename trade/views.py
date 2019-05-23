from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Demanda, Anunciante
from .serializers import DemandaSerializer, AnuncianteSerializer


class DemandaList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Demanda.objects.all()
    serializer_class = DemandaSerializer


class AnuncianteList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Anunciante.objects.all()
    serializer_class = AnuncianteSerializer
