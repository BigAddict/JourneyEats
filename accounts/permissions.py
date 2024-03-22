from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from .models import CustomUser

def create_chef_permissions():
    chef_content_type = ContentType.objects.get_for_model(CustomUser)  # Assuming CustomUser is your user model
    chef_permissions = [
        Permission.objects.create(codename='can_add_recipe', name='Can add recipe', content_type=chef_content_type),
        Permission.objects.create(codename='can_edit_recipe', name='Can edit recipe', content_type=chef_content_type),
        Permission.objects.create(codename='can_delete_recipe', name='Can delete recipe', content_type=chef_content_type),
        # Add more permissions as needed
    ]
    return chef_permissions

def create_client_permissions():
    client_content_type = ContentType.objects.get_for_model(CustomUser)
    client_permissions = [
        Permission.objects.create(codename='')
    ]