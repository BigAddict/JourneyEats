from django.urls import path

from .views import create_chef

urlpatterns = [
    path("details", create_chef, name="create_chef")
]
