from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Author(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='inicio_author')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    # Asegúrate de tener estos campos si los estás usando en el admin
    category = models.CharField(max_length=100)  # o un ForeignKey si usas un modelo de categorías
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title