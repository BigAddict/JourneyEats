from django.urls import path
from .views import DashboardTemplateView

urlpatterns = [
    path("dashboard/", DashboardTemplateView.as_view(), name="dashboard")
]
