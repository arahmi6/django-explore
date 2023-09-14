from rest_framework import serializers
from .models import Pelanggan

class PelangganSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelanggan
        fields = '__all__'
