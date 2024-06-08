# cuentas/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from blog.models import Post 
from django.contrib.auth.decorators import login_required
from django.conf import settings


@login_required
def blog_home(request):
    posts = Post.objects.all()
    blog_name = settings.BLOG_NAME
    return render(request, 'blog/blog_home.html', {'posts': posts, 'blog_name': blog_name})

@login_required
def article(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/article.html', {'post': post})

def login_view_cuentas(request):
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

def signup_view_cuentas(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('blog_home')
    else:
        form = UserCreationForm()
    return render(request, 'cuentas/signup.html', {'form': form})

def article_detail(request, article_id):
    article = get_object_or_404(Post, id=article_id)
    return render(request, 'blog/article_detail.html', {'article': article})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirige a la página de inicio de sesión después del logout
