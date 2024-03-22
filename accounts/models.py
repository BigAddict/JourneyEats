from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from PIL import Image

from .managers import CustomUserManager

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('chef', 'Chef'),
        ('client', 'Client'),
    )

    username = None
    email = models.EmailField(_("email address"), unique=True)
    phone_number = PhoneNumberField(region='KE')
    user_type = models.CharField(_("user type"), max_length=10, choices=USER_TYPE_CHOICES)
    profile_complete = models.BooleanField(
        _("Profile completeness"),
        default=False,
        help_text=_("Designates whether the user has completed profile creation."),)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['user_type']

    objects = CustomUserManager()

    def is_chef(self):
        return self.user_type == 'chef'

    def __str__(self):
        return self.email
    
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    about = models.TextField(default="")
    instagram = models.CharField(default="", max_length=100, blank=True)
    facebook = models.CharField(default="", max_length=100, blank=True)
    twitter = models.CharField(default="", max_length=100, blank=True)
    linkedin = models.CharField(_("Linked In"), default="", max_length=100)
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=gender_choices)
    date_of_birth = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=100, blank=True)
    language = models.CharField(max_length=100, blank=True)
    currency = models.CharField(max_length=100, blank=True)
    public_profile_data = models.JSONField(default=dict)
    hobbies = models.TextField(blank=True)
    interest = models.TextField(blank=True)
    favourite_activities = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.profile_picture:
            img = Image.open(self.profile_picture.path)

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.profile_picture.path)

    def __str__(self):
        return f"Profile data for {self.user.email}"