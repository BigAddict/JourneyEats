from django.http import HttpRequest

from accounts.models import Profile
from chef_regestry.models import Chef
from .models import Message, MessageItem
from communications.models import Notification, NotificationItem

def custom_context(request:HttpRequest):
    default_values = {}

    # default values values based on User
    if request.user.is_authenticated:
        default_values['profile'] = request.user
        # Notification Header
        notification, notification_created = Notification.objects.get_or_create(user=request.user)
        if notification_created:
            notification.save()
        default_values['notification_item'] = NotificationItem.objects.filter(
            notification=notification,
            is_opened = False
        )
        default_values['notification_item_count'] = NotificationItem.objects.filter(
            notification=notification,
            is_opened = False
        ).count()
        # Messages Header
        message, message_created = Message.objects.get_or_create(sender=request.user)
        if message_created:
            message.save()
        default_values['message_items'] = MessageItem.objects.filter(
            receiver = request.user,
            is_read = False
        )
        default_values['message_item_count'] = MessageItem.objects.filter(
            receiver = request.user,
            is_read = False
        ).count()
        default_values['profile_data'] = Profile.objects.filter(user = request.user).first()
        default_values['chef_data'] = Chef.objects.filter(user=request.user).first()
    return default_values