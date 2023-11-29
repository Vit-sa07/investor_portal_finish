from rest_framework import generics
from .models import Project, Investment
from .serializers import ProjectSerializer, InvestmentSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

class ProjectListView(generics.ListCreateAPIView):
    authentication_classes = (JWTAuthentication,)
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (JWTAuthentication,)
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class InvestmentListView(generics.ListCreateAPIView):
    authentication_classes = (JWTAuthentication,)
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class InvestmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (JWTAuthentication,)
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer
