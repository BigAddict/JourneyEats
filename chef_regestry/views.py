from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.http import HttpRequest
from django.shortcuts import redirect, render

from accounts.mixin import ChefRequiredMixin
from .forms import ChefForm

class ChefListingView(TemplateView):
    pass

class ChefDetailsEditView(ChefRequiredMixin, TemplateView):
    pass

class ChefRecipeView(TemplateView):
    pass

class ChefRecipeEditView(ChefRequiredMixin, TemplateView):
    pass

def create_chef(request:HttpRequest):
    if request.method == 'POST':
        form = ChefForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            redirect("dashboard")
    else:
        form = ChefForm(user=request.user)
    return render(request, "chef_regestry/update_details.html", {'form': form})