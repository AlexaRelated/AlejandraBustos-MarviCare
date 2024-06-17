from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models import Q
from django.shortcuts import render


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='blog_profile')
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='blog_author')
    bio = models.TextField()

    def __str__(self):
        return self.user.username


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_articles')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author}: {self.text}'



