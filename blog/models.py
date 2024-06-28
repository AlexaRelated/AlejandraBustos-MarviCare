from django.db import models
from django import forms
from usuarios.models import Author  # Importar el modelo Author de la app usuarios
from django.utils import timezone



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    categories = models.ManyToManyField(Category)  # Relación ManyToMany con Category

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    categories = models.ManyToManyField('Category')
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'categories', 'slug', 'image']

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


