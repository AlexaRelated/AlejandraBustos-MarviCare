from django.db import models
from django.urls import reverse

class MyModelName(models.Model):
    my_field_name = models.CharField(max_length=20, help_text="Enter field documentation")

    class Meta:
        ordering = ["-my_field_name"]

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.my_field_name

from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('dermatologia', 'Dermatología'),
        ('cosmetica', 'Cosmética'),
        ('maquillaje', 'Maquillaje'),
        ('estetica', 'Estética'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cuentas_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)

    def __str__(self):
        return self.title
