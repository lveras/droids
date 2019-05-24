from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from .models import Demanda
from django.contrib.auth.models import User
from .serializers import DemandaSerializer, UserSerializer


class DemandaList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Demanda.objects.all()
    serializer_class = DemandaSerializer

    def get_queryset(self):
        anunciante = self.request.user
        return Demanda.objects.filter(anunciante=anunciante.id)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DemandaDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Demanda.objects.all()
    serializer_class = DemandaSerializer

    def get_queryset(self):
        user = self.request.user
        return Demanda.objects.filter(user=user.id)


class UserList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
