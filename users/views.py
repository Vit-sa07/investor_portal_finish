from rest_framework import generics

from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.utils import timezone

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import User
from .serializers import UserSerializer, UserRegistrationSerializer


class UserListView(generics.ListCreateAPIView):
    authentication_classes = (JWTAuthentication,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (JWTAuthentication,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRegistrationView(APIView):
    authentication_classes = (JWTAuthentication,)
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.email_verification_token = get_random_string(length=6)
            user.save()

            # Отправить письмо с кодом верификации
            send_mail(
                'Your Verification Code',
                f'Your verification code is: {user.email_verification_token}',
                'from@example.com',
                [user.email],
                fail_silently=False,
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyEmailView(APIView):
    authentication_classes = (JWTAuthentication,)
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        token = request.data.get('token')
        try:
            user = User.objects.get(email=email, email_verification_token=token)
            user.email_verified = True
            user.email_verification_token = ''
            user.save()
            return Response({'message': 'Email verified successfully'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'Invalid email or token'}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    authentication_classes = (JWTAuthentication, )
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(username=email, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)

            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })

        return Response({'error': 'Invalid Credentials'}, status=400)


