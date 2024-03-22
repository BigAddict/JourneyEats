from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.http import HttpRequest
from typing import Any

from .models import Notification, NotificationItem

class NotificationTemplateView(TemplateView):

    template_name = "communications/notifications.html"