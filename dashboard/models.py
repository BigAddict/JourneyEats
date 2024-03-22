from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from datetime import datetime, time
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

# This is just dummy data
class Message(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_messages')
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.sender.email
    
class MessageItem(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='items')
    sender = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='related_name')
    body = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Message from {self.sender.email} to {self.receiver.email}"
        
    