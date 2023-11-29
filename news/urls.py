from django.urls import path
from .views import NewsListView, NewsDetailView
from . import views

urlpatterns = [
    path('', views.NewsListView.as_view(), name='news-list'),
    path("<int:pk>/", NewsDetailView.as_view(), name="news-detail"),
]
