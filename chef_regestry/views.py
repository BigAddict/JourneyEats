from typing import Any
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.http import HttpRequest
from django.shortcuts import redirect, render

from accounts.mixin import ChefRequiredMixin

class ChefRecipeEditView(ChefRequiredMixin, TemplateView):
    
    template_name = "chef_regestry/chef_recipe_edit_view.html"

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.user = request.user
        return super().get(request, *args, **kwargs)
    
    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        print(request.POST)
        return super().get(request, *args, **kwargs)