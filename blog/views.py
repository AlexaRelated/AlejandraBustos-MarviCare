from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Article

def blog_home(request):
    posts = Post.objects.all().order_by('-id')  # Cargar todos los posts y ordenarlos por el ID en orden descendente
    return render(request, 'index.html', {'posts': posts})

def article(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'article.html', {'post': post})

def article_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'article_detail.html', {'post': post})

def author_view(request, id):
    author = get_object_or_404(Author, id=id)
    return render(request, 'author.html', {'author': author})

def article_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article.html', {'article': article})

def category_view(request, category):
    posts = Post.objects.filter(category__iexact=category)
    return render(request, 'category.html', {'posts': posts, 'category': category})

def crear_publicacion(request):
    # Lógica para crear una nueva publicación
    return render(request, 'crear_publicacion.html')
