from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')  # Cambiado a 'posts'
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # Resto de campos y métodos


def search_posts(request):
    query = request.GET.get('q')
    if query:
        # Filtrar tanto los posts de inicio como los del blog
        inicio_posts = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        blog_posts = BlogPost.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        # Unir los resultados en una única lista
        posts = list(inicio_posts) + list(blog_posts)
    else:
        posts = []
    return render(request, 'search_results.html', {'posts': posts, 'query': query})



class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return self.user.username

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')  # Cambiado a 'blog_posts'
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
