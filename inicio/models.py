from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    published_date = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=200)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Author(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='inicio_author')
    bio = models.TextField()

    def __str__(self):
        return self.user.username
