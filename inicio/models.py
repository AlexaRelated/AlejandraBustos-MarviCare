from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Author(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='inicio_author')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=100, blank=True)  # Añade este campo si es necesario

    def __str__(self):
        return self.title
