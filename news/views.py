from rest_framework import generics
from .models import News
from .serializers import NewsSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

class NewsListView(generics.ListCreateAPIView):
    authentication_classes = (JWTAuthentication,)
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def perform_create(self, serializer):
        # Setting the author if news is manually created
        if serializer.validated_data['news_type'] == News.MANUAL:
            serializer.save(created_by=self.request.user)
        else:
            serializer.save()

class NewsDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (JWTAuthentication,)
    queryset = News.objects.all()
    serializer_class = NewsSerializer
