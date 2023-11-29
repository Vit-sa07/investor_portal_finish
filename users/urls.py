from django.urls import path
from .views import UserListView, UserDetailView, UserRegistrationView, VerifyEmailView, LoginView

urlpatterns = [
    path("", UserListView.as_view(), name="user-list"),
    path("<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    path('verify-email/', VerifyEmailView.as_view(), name='verify-email'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]