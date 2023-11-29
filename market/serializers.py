from rest_framework import serializers
from .models import Crypt

class CryptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crypt
        fields = ("id", "name", "course", "description")
