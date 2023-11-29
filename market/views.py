from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Crypt
from .serializers import CryptSerializer
import requests
from rest_framework_simplejwt.authentication import JWTAuthentication

class CryptListView(generics.ListCreateAPIView):
    authentication_classes = (JWTAuthentication,)
    queryset = Crypt.objects.all()
    serializer_class = CryptSerializer

class CryptDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (JWTAuthentication,)
    queryset = Crypt.objects.all()
    serializer_class = CryptSerializer


class CoinLoreTickerView(APIView):
    authentication_classes = (JWTAuthentication,)
    def get(self, request, *args, **kwargs):
        try:
            response = requests.get('https://api.coinlore.net/api/tickers/')
            response.raise_for_status()
            return Response(response.json(), status=status.HTTP_200_OK)
        except requests.RequestException as e:
            print(f"Error while fetching data from CoinLore: {e}")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

