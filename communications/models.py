from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

CustomUser = get_user_model()

class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Notification")
        verbose_name_plural = _("Notifications")

    def __str__(self):
        return f"Notifications for {self.user.email}"
    

class NotificationItem(models.Model):
    """
    Tag values are class names for templates. They include:
    1. bi-exclamation-circle text-warning - Warning icon
    2. bi-x-circle text-danger - Danger icon
    3. bi-check-circle text-success - Success icon
    4. bi-info-circle text-primary - Just a normal/neutral icon
    """
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
    tag = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    is_opened = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("NotificationItem")
        verbose_name_plural = _("NotificationsItems")

    def __str__(self):
        return f"{self.title} for {self.notification.user.email}"
