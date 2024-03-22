from django.contrib import admin
from django.contrib.auth.models import User
from .models import CustomUser, Profile

# Registering my CustomUser
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone_number', 'user_type', 'password', 'is_staff', 'is_superuser', 'is_active')
    list_filter = ('user_type', 'is_staff', 'is_superuser')
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(Profile)