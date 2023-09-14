from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Pelanggan
from .serializers import PelangganSerializer

class PelangganListCreateView(generics.ListCreateAPIView):
    queryset = Pelanggan.objects.all()
    serializer_class = PelangganSerializer

class PelangganDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pelanggan.objects.all()
    serializer_class = PelangganSerializer
