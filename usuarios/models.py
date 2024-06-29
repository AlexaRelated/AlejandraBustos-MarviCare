from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.jpg')
    bio = models.TextField(max_length=500, blank=True)
    numero_tienda = models.CharField(max_length=50, blank=True)
    ciudad = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='author')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

