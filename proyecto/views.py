from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from .models import Post, Article
from .forms import PostForm
from django.contrib.auth.decorators import login_required

@login_required
def blog_home(request):
    posts = Post.objects.all()
    blog_name = settings.BLOG_NAME
    return render(request, 'blog/blog_home.html', {'posts': posts, 'blog_name': blog_name})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog_home')
        else:
            error_message = "Credenciales incorrectas. Por favor, inténtalo de nuevo."
            return render(request, 'cuentas/login.html', {'error_message': error_message})
    return render(request, 'cuentas/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def crear_publicacion(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_home')
    else:
        form = PostForm()
    return render(request, 'blog/crear_publicacion.html', {'form': form})

@login_required
def article_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/article.html', {'article': article})

@login_required
def category_view(request, category):
    posts = Post.objects.filter(category__iexact=category)
    return render(request, 'blog/category.html', {'posts': posts, 'category': category})
