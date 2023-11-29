from rest_framework import serializers
from .models import Project, Investment

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class InvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investment
        fields = '__all__'
