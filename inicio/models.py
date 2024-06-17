# inicio/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models import Q
from django.shortcuts import render

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inicio_posts')
    categories = models.ManyToManyField(Category, related_name='inicio_posts')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='inicio_profile')
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='inicio_author')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

def search_posts(request):
    query = request.GET.get('q')
    if query:
        inicio_posts = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        blog_posts = BlogPost.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        posts = list(inicio_posts) + list(blog_posts)
    else:
        posts = []
    return render(request, 'search_results.html', {'posts': posts, 'query': query})

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inicio_articles')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


