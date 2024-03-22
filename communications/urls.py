from django.urls import path

from .views import NotificationTemplateView

urlpatterns = [
    path("notifications", NotificationTemplateView.as_view(), name="notifications")
]
