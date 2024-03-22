from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.http import HttpRequest
from typing import Any

@method_decorator(login_required, name='dispatch')
class DashboardTemplateView(TemplateView):

    template_name = "dashboard/index.html"
    