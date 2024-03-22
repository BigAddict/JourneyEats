from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from PIL import Image

CustomUser = get_user_model()

class Chef(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    speciality = models.CharField(_("Speciality"), max_length=100, blank=True)
    experience = models.PositiveIntegerField(_("Experience (in years)"), default=0)
    availability = models.CharField(_("Availability"), max_length=100, blank=True)
    hourly_rate = models.DecimalField(_("Hourly Rate"), max_digits=8, decimal_places=2, default=0.00)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    class Meta:
        verbose_name = _("Chef")
        verbose_name_plural = _("Chefs")

    def __str__(self):
        return self.user.email

class Recipe(models.Model):
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE, related_name='recipes')
    thumbnail = models.ImageField(('Recipe Thumbnail'), upload_to='recipe_thumbnails/')
    title = models.CharField(_("Title"), max_length=100)
    description = models.TextField(_('Description'), blank=True)
    ingredients = models.TextField(_("Ingredients"))
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    class Meta:
        verbose_name = _("Recipe")
        verbose_name_plural = _("Recipes")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.thumbnail:
            img = Image.open(self.thumbnail.path)

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.thumbnail.path)

    def __str__(self):
        return f"{self.title} by {self.chef.user.email}"

class RecipePhotos(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(_("Photo"), upload_to="recipe_photos/")
    uploaded_at = models.DateTimeField(_("Uploaded At"), auto_now_add=True)

    class Meta:
        verbose_name = _("Recipe Photo")
        verbose_name_plural = _("Recipe Photos")
    
    def __str__(self):
        return f"Photo for {self.recipe.title}"