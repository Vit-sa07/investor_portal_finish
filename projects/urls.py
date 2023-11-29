from django.urls import path
from .views import ProjectListView, ProjectDetailView, InvestmentListView, InvestmentDetailView

urlpatterns = [
    path("", ProjectListView.as_view(), name="project-list"),
    path("<int:pk>/", ProjectDetailView.as_view(), name="project-detail"),
    path("investments/", InvestmentListView.as_view(), name="investments-list"),
    path("investments/<int:pk>/", InvestmentDetailView.as_view(), name="investments-detail"),
]
