from django.urls import path

from .views import ChefRecipeEditView

urlpatterns = [
    path("recipes", ChefRecipeEditView.as_view(), name="recipes")
]
